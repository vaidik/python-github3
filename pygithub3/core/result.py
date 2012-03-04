#!/usr/bin/env python
# -*- encoding: utf-8 -*-

from urlparse import urlparse, parse_qs

from .link import Link


class Method(object):
    """ Lazy support """

    def __init__(self, method, request, **method_args):
        self.method = method
        self.request = request
        self.args = method_args
        self.cache = {}

    def cached(func):
        """ Decorator to don't do a request if it's cached """
        def wrapper(self, page=1):
            if str(page) in self.cache:
                return self.cache[str(page)]
            return func(self, page)
        return wrapper

    def if_needs_lastpage(func):
        """ Decorator to set last page only if it can and it hasn't retrieved
        before """
        def wrapper(self, has_link):
            has_last_page = hasattr(self, 'last_page')
            if not has_last_page and has_link:
                return func(self, has_link)
            elif not has_last_page and not has_link:
                self.last_page = 1
        return wrapper

    @if_needs_lastpage
    def __set_last_page_from(self, link_header):
        """ Get and set last_page form link header """
        link = Link(link_header)
        self.last_page = int(link.last.params.get('page'))

    @cached
    def __call__(self, page=1):
        """ Call a real request """
        response = self.method(page=page)
        self.__set_last_page_from(response.headers.get('link'))
        self.cache[str(page)] = self.resource.loads(response.content)
        return self.cache[str(page)]

    @property
    def last(self):
        if not hasattr(self, 'last_page'):
            self()
        return self.last_page


class Page(object):
    """ Iterator of resources """

    def __init__(self, getter, page=1):
        self.getter = getter
        self.page = page

    def __iter__(self):
        return self

    def __add__(self, number):
        return self.page + number

    def __radd__(self, number):
        return number + self.page

    def __sub__(self, number):
        return self.page - number

    def __rsub__(self, number):
        return number - self.page

    def __lt__(self, number):
        return self.page < number

    def __le__(self, number):
        return self.page <= number

    def __eq__(self, number):
        return self.page == number

    def __ne__(self, number):
        return self.page != number

    def __gt__(self, number):
        return self.page > number

    def __ge__(self, number):
        return self.page >= number

    @property
    def resources(self):
        return getattr(self, '_count', None) or u"~"

    def get_content(func):
        def wrapper(self):
            if not hasattr(self, '_count'):
                content = self.getter(self.page)
                self._count = len(content)
                self.iterable = iter(content)
            return func(self)
        return wrapper

    @get_content
    def __next__(self):
        try:
            return self.iterable.next()
        except StopIteration:
            self.iterable = iter(self.getter(self.page))
            raise StopIteration

    def next(self):
        return self.__next__()

    def __str__(self):
        return '<{name}{page} resources={resources}>'.format(
                name=self.__class__.__name__,
                page=self.page,
                resources=self.resources)

    def __repr__(self):
        return "%s[%d]" % (self.__str__(), id(self))


class Result(object):
    """
    Result is a very **lazy** paginator beacuse only do a real request when is
    needed, besides it's **cached**, so never repeats a request.

    You have several ways to consume it

    #. Iterating over the result::

        result = some_request()
        for page in result:
            for resource in page:
                print resource

    #. With a generator::

        result = some_request()
        for resource in result.iterator():
            print resource

    #. As a list::

        result = some_request()
        print result.all()

    #. Also you can request some page manually

        .. autoattribute:: pygithub3.core.result.Result.pages
        .. automethod:: pygithub3.core.result.Result.get_page

        Each ``Page`` is an iterator and contains resources::

            result = some_request()
            assert result.pages > 3
            page3 = result.get_page(3)
            page3_resources = list(page3)
    """

    def __init__(self, client, request, **kwargs):
        self.getter = Method(client.get, request, **kwargs)
        self.page = Page(self.getter)

    def __iter__(self):
        return self

    def __next__(self):
        if self.page <= self.pages:
            page_to_return = self.page
            self.page = Page(self.getter, page_to_return + 1)
            return page_to_return
        self.page = Page(self.getter)
        raise StopIteration

    def next(self):
        return self.__next__()

    @property
    def pages(self):
        """ Total number of pages in request """
        return self.getter.last

    def get_page(self, page):
        """ Get ``Page`` of resources

        :param int page: Page number
        """
        if page in xrange(1, self.pages + 1):
            return Page(self.getter, page)
        return None

    def iterator(self):
        for page in self:
            for resource in page:
                yield resource

    def all(self):
        return list(self.iterator())
