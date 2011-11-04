#!/usr/bin/env python
# -*- encoding: utf-8 -*-
#
# author: David Medina

import requests
import json
from errors import GithubError
import github3.exceptions as ghexceptions

RESOURCES_PER_PAGE = 100

class GithubCore(object):
    """ Wrapper for requests """

    requests_remaining = None

    def __init__(self):
        self.session = requests.session()
        self.session.params = {'per_page': RESOURCES_PER_PAGE}
        self._parser = json

    #@paginate to slice a generator after
    def get(self, request, **kwargs):
        response = self._request('GET', request, **kwargs)
        return self._parser.loads(response.content)

    def head(self, request, **kwargs):
        return self._request('HEAD', request, **kwargs).headers

    def post(self, request, data=None, **kwargs):
        kwargs['data'] = self._parser.dumps(data)
        response = self._request('POST', request, **kwargs)
        assert response.status_code == 201
        return self._parser.loads(response.content)

    def patch(self, request, data=None, **kwargs):
        kwargs['data'] = self._parser.dumps(data)
        response = self._request('PATCH', request, **kwargs)
        assert response.status_code == 200
        return self._parser.loads(response.content)

    def put(self, request, **kwargs):
        response = self._request('PUT', request, **kwargs)
        assert response.status_code == 204

    def bool(self, request, **kwargs):
        try:
            response = self._request('GET', request, **kwargs)
        except ghexceptions.NotFound:
            return False
        assert response.status_code == 204
        return True

    def delete(self, request, **kwargs):
        response = self._request('DELETE', request, **kwargs)
        assert response.status_code == 204

    def _request(self, verb, request, **kwargs):

        request = settings.base_url + request
        response = self.session.request(verb, request, **kwargs)
        self.requests_remaining = response.headers.get(
            'x-ratelimit-remaining',-1)
        error = GithubError(response)
        error.process()

        return response
