#!/usr/bin/env python
# -*- encoding: utf-8 -*-

from . import Service


class Keys(Service):

    def list(self, user=None, repo=None):
        request = self.make_request('repos.keys.list', user=user, repo=repo)
        return self._get_result(request)

    def get(self, id, user=None, repo=None):
        request = self.make_request('repos.keys.get',
            id=id, user=user, repo=repo)
        return self._get(request)

    def create(self, data, user=None, repo=None):
        request = self.make_request('repos.keys.create',
            body=data, user=user, repo=repo)
        return self._post(request)

    def update(self, id, data, user=None, repo=None):
        request = self.make_request('repos.keys.update',
            id=id, body=data, user=user, repo=repo)
        return self._patch(request)

    def delete(self, id, user=None, repo=None):
        request = self.make_request('repos.keys.delete',
            id=id, user=user, repo=repo)
        self._delete(request)
