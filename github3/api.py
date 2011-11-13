#!/usr/bin/env python
# -*- encoding: utf-8 -*-
#
# author: David Medina

import requests
import json
from errors import GithubError
from handlers import users, gists

RESOURCES_PER_PAGE = 100


class GithubCore(object):
    """
    Wrapper to github api requests

    Methods: get, head, post, patch, put, delete
    """

    requests_remaining = None
    base_url = 'https://api.github.com/'

    def __init__(self):
        """
        Init `requests.session`
        Init JSON parser
        """
        self.session = requests.session()
        self.session.params = {'per_page': RESOURCES_PER_PAGE}
        self._parser = json

    def get(self, request, paginate=False, **kwargs):
        """
        GET request

        :param paginate: Boolean to return link header to paginate
        """
        response = self._request('GET', request, **kwargs)
        content = self._parser.loads(response.content)
        if paginate:
            return response.headers.get('link'), content
        else:
            return content

    def head(self, request, **kwargs):
        """ HEAD request """
        return self._request('HEAD', request, **kwargs)

    def post(self, request, data=None, **kwargs):
        """
        POST request

        :param data: raw python object to send
        """
        kwargs['data'] = self._parser.dumps(data)
        response = self._request('POST', request, **kwargs)
        assert response.status_code == 201
        return self._parser.loads(response.content)

    def patch(self, request, data=None, **kwargs):
        """
        PATCH request

        :param data: raw python object to send
        """
        kwargs['data'] = self._parser.dumps(data)
        response = self._request('PATCH', request, **kwargs)
        assert response.status_code == 200
        return self._parser.loads(response.content)

    def put(self, request, **kwargs):
        """ PUT request """
        # Content-length: 0 to headers ?
        response = self._request('PUT', request, **kwargs)
        assert response.status_code == 204
        return response

    def delete(self, request, **kwargs):
        """ DELETE request """

        data = kwargs.get('data')
        if data:
            kwargs['data'] = self._parser.dumps(data)
        response = self._request('DELETE', request, **kwargs)
        assert response.status_code == 204
        return response

    def _parse_args(self, request_args):
        """
        Arg's parser to `_request` method

        Put extra request_args in params
        """
        request_core = (
            'params', 'data', 'headers', 'cookies', 'files', 'auth', 'tiemout',
            'allow_redirects', 'proxies', 'return_response', 'config')
        request_params = request_args.get('params')
        extra_params = {}
        for k, v in request_args.items():
            if k in request_core:
                continue
            extra_params.update({k: v})
            del request_args[k]
        if request_params and getattr(request_params, 'update'):
            request_args['params'].update(extra_params)
        elif extra_params:
            request_args['params'] = extra_params

        return request_args

    def _request(self, verb, request, **kwargs):
        """
        Http request wrapper

        :param verb: Http method
        :param request : Url query request
        :param kwargs: Keyword args to request
        """
        request = self.base_url + request
        self._parse_args(kwargs)
        response = self.session.request(verb, request, **kwargs)
        self.requests_remaining = response.headers.get(
            'x-ratelimit-remaining', -1)
        error = GithubError(response)
        error.process()

        return response


class Github(GithubCore):
    """ Library enter """

    def __init__(self, *args):
        super(Github, self).__init__()
        self.authenticated = False
        auth = len(args)
        if auth == 2:  # Basic auth
            self.session.auth = tuple(map(str, args))
            self.authenticated = True
        elif auth == 1:  # Token oauth
            raise NotImplementedError
        elif auth > 2:
            raise TypeError("user, password or token")

    @property
    def users(self):
        if self.authenticated:
            return users.AuthUser(self)
        else:
            return users.User(self)

    @property
    def gists(self):
        if self.authenticated:
            return gists.AuthGist(self)
        else:
            return gists.Gist(self)
