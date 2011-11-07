#!/usr/bin/env python
# -*- encoding: utf-8 -*-
#
# author: David Medina

from github3.core import Paginate, Modelizer

class Handler(object):
    """ Handler base. Requests to API and modelize responses """

    def __init__(self, gh):
        self._gh = gh
        super(Handler, self).__init__()

    def _bool(self, resource, **kwargs):
        """ Handler request to boolean response """

        from github3.exceptions import NotFound
        try:
            response = self._gh.head(resource, **kwargs)
        except NotFound:
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
                yield Modelizer(model or self.model).loads(raw_resource)
                #yield raw_resource
            else:
                continue
            break

    def _get_resource(self, resource, model=None):
        """ Handler request to single resource """

        raw_resource = self._gh.get(resource)
        return Modelizer(model or self.model).loads(raw_resource)
