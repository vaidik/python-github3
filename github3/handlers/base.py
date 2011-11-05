#!/usr/bin/env python
# -*- encoding: utf-8 -*-
#
# author: David Medina

class Paginate:
    """ Paginate resources """

    def __init__(self, resource, requester):
        self.resource = resource
        self.requester = requester
        self.page = 1

    def _last_page(self, link):
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

    #TODO: if limit is multiple of per_page... it do another request for nothing
    def _get_resources(self, resource, model=None, limit=None):
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
