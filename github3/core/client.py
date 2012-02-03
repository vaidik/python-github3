#!/usr/bin/env python
# -*- encoding: utf-8 -*-

import requests
from errors import GithubError


VALID_REQUEST_ARGS = set((
    'params', 'data', 'headers', 'cookies', 'files', 'auth', 'timeout',
    'allow_redirects', 'proxies', 'return_response', 'config',
    'prefetch', 'verify'))


class Client(object):
    """ Client to send configurated requests"""

    def __init__(self, **kwargs):
        """
        It can be configurated

        :login, :password, :user, :repo, :token, :per_page, :base_url
        """

        self.requester = requests.session()
        self.config = {
            'per_page': 100,
            'base_url': 'https://api.github.com/'
        }
        self.config.update(kwargs)
        self.set_credentials(self.config.get('login'),
                             self.config.get('password'))
        self.set_token(self.config.get('token'))
        self.__set_params(self.config)

    @property
    def user(self):
        return self.config.get('user')

    @user.setter
    def set_user(self, user):
        self.config['user'] = user

    @property
    def repo(self):
        return self.config.get('repo')

    @repo.setter
    def set_repo(self, repo):
        self.config['repo'] = repo

    def set_credentials(self, login, password):
        if login and password:
            self.requester.auth = (login, password)

    def set_token(self, token):
        if token:
            self.requester.params['access_token'] = token

    def __set_params(self, config):
        self.requester.params['per_page'] = config.get('per_page')

    def __parse_kwargs(func):
        """ Decorator to put extra args into requests.params """

        def wrapper(self, verb, resource, **kwargs):
            diffs = kwargs.viewkeys() - VALID_REQUEST_ARGS
            new_params = kwargs.get('params') or {}
            new_params.update({key:kwargs[key] for key in diffs})
            kwargs['params'] = new_params
            return func(self, verb, resource, **kwargs)
        return wrapper

    @__parse_kwargs
    def request(self, verb, resource, **kwargs):
        resource = "%s%s" % (self.config['base_url'], resource)
        response = self.requester.request(verb, resource, **kwargs)
        GithubError(response).process()
        return response

    def get(self, resource, **kwargs):
        return self.request('get', resource, **kwargs)

    def post(self, resource, **kwargs):
        return self.request('post', resource, **kwargs)

    def patch(self, resource, **kwargs):
        return self.request('patch', resource, **kwargs)

    def put(self, resource, **kwargs):
        return self.request('put', resource, **kwargs)

    def delete(self, resource, **kwargs):
        return self.request('delete', resource, **kwargs)

    def head(self, resource, **kwargs):
        return self.request('head', resource, **kwargs)
