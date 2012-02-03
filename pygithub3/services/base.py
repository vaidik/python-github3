#!/usr/bin/env python
# -*- encoding: utf-8 -*-

from pygithub3.core.client import Client


class Base(object):

    def __init__(self, **config):
        self.client = Client(**config)

    def get_user(self):
        return self.client.user

    def set_user(self, user):
        self.client.user = user

    def get_repo(self):
        return self.client.repo

    def set_repo(self, repo):
        self.client.repo = repo

    def _get_result(self, resource, **kwargs):
        return Result(self.client.get, resource, **kwargs)


class Result(object):  # move

    def __init__(self, method, resource, **kwargs):
        self.method = method
        self.resource = resource
        self.args = kwargs

    def __repr__(self):
        pass

    def process(self):
        model = self.resource.get_model()
        raw = self.method(self.resource, **self.args)
        if model:
            import json
            return model.loads(json.loads(raw.content))
