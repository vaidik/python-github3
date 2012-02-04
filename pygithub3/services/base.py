#!/usr/bin/env python
# -*- encoding: utf-8 -*-

from pygithub3.core.client import Client
from pygithub3.core.result import Result
from pygithub3.core.ghrequests import Factory


class Base(object):

    def __init__(self, **config):
        self.client = Client(**config)
        self.get_request = Factory()

    def get_user(self):
        return self.client.user

    def set_user(self, user):
        self.client.user = user

    def get_repo(self):
        return self.client.repo

    def set_repo(self, repo):
        self.client.repo = repo

    def config_request(self, **kwargs):
        self.get_request.config_with(**kwargs)

    def _delete(self, request_uri, **kwargs):
        request = self.get_request(request_uri)
        input_data = request.get_data()
        self.client.delete(request, data=input_data)

    def _post(self, request_uri, **kwargs):
        request = self.get_request(request_uri)
        resource = request.get_resource()
        input_data = request.get_data()
        response = self.client.post(request, data=input_data)
        return resource.loads(response.content)

    def _get(self, request_uri, **kwargs):
        request = self.get_request(request_uri)
        resource = request.get_resource()
        response = self.client.get(request, **kwargs)
        return resource.loads(response.content)

    def _get_result(self, request_uri, **kwargs):
        request = self.get_request(request_uri)
        return Result(self.client, request, **kwargs)
