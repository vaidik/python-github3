#!/usr/bin/env python
# -*- encoding: utf-8 -*-
#
# author: David Medina

import github3.exceptions as ghexceptions

class Paginate:
    """ Paginate resource iterator

    :param resource: URL resource
    :param requester: Bound method to request. See `GithubCore.get`
    """

    def __init__(self, resource, requester):
        self.resource = resource
        self.requester = requester
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

    def __iter__(self):
        return self

    def initial(self):
        """ First request. Force requester to paginate returning link header """
        link, content = self.requester(self.resource, paginate=True, page=1)
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
                content = self.requester(self.resource, page=self.page)
                self.page += 1
                return content

class Handler(object):
    """ Handler base. Requests to API and modelize responses """

    def __init__(self, gh):
        self._gh = gh
        super(Handler, self).__init__()

    def _bool(self, resource, **kwargs):
        """ Handler request to boolean response """
        try:
            response = self._gh.head(resource, **kwargs)
        except ghexceptions.NotFound:
            return False
        assert response.status_code == 204
        return True

    #TODO: if limit is multiple of per_page... it do another request for nothing
    def _get_resources(self, resource, model=None, limit=None):
        """ Hander request to multiple resources """
        page_resources = Paginate(resource, self._gh.get)
        counter = 1
        for page in page_resources:
            for raw_resource in page:
                if limit and counter > limit: break
                counter += 1
                yield raw_resource
            else:
                continue
            break
