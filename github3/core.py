#!/usr/bin/env python
# -*- encoding: utf-8 -*-
#
# author: David Medina

class Paginate:
    """ Paginate resource iterator

    :param resource: URL resource
    :param requester: Bound method to request. See `GithubCore.get`
    :param kwargs: Args to request (params)
    """

    def __init__(self, resource, requester, **kwargs):
        self.resource = resource
        self.requester = requester
        self.kwargs = kwargs
        self.page = 1

    def _last_page(self, link):
        """ Get and cached last page from link header """
        if not getattr(self, 'last', False):
            from github3.packages.link_header import parse_link_value
            from urlparse import urlparse, parse_qs
            for link, rels in parse_link_value(link).items():
                if rels.get('rel') == 'last':
                    query = urlparse(link).query
                    self.last = int(parse_qs(query).get('page').pop())

        return self.last

    # TODO: reset iterators... multiple?
    def __iter__(self):
        return self

    def initial(self):
        """ First request. Force requester to paginate returning link header """
        link, content = self.requester(self.resource, paginate=True,
                                       page=1, **self.kwargs)
        self.last = self._last_page(link) if link else 1
        return content

    def next(self):
        if self.page == 1:
            content = self.initial()
            self.page += 1
            return content
        else:
            if self.page > self.last:
                raise StopIteration
            else:
                content = self.requester(self.resource, page=self.page,
                                         **self.kwargs)
                self.page += 1
                return content

class Converter(object):
    """ Abstract converter class """

    def loads(self):
        raise NotImplementedError("%s needs define '%s' method" %
            (self.__class__.__name__, 'loads'))

    def dumps(self):
        raise NotImplementedError("%s needs define '%s' method" %
            (self.__class__.__name__, 'dumps'))

    def inject(self):
        raise NotImplementedError("%s needs define '%s' method" %
            (self.__class__.__name__, 'inject'))
