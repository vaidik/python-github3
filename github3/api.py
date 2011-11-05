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
    base_url = 'https://api.github.com/'

    def __init__(self):
        self.session = requests.session()
        self.session.params = {'per_page': RESOURCES_PER_PAGE}
        self._parser = json

    def get(self, request, paginate=False, **kwargs):
        print '\nGET %s %s\n' % (request, kwargs)
        response = self._request('GET', request, **kwargs)
        content = self._parser.loads(response.content)
        if paginate:
            return response.headers.get('link'), content
        else:
            return content

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

    def _parse_args(self, request_args):
        request_core = (
            'params','data','headers','cookies','files','auth','tiemout',
            'allow_redirects','proxies','return_response','config')
        request_params = request_args.get('params')
        extra_params = {}
        for k, v in request_args.items():
            if k in request_core: continue
            extra_params.update({k: v})
            del request_args[k]
        if request_params:
            request_args['params'].update(extra_params)
        else:
            request_args['params'] = extra_params

        return request_args

    def _request(self, verb, request, **kwargs):

        request = self.base_url + request
        parsed_args = self._parse_args(kwargs)
        response = self.session.request(verb, request, **parsed_args)
        self.requests_remaining = response.headers.get(
            'x-ratelimit-remaining',-1)
        error = GithubError(response)
        error.process()

        return response
