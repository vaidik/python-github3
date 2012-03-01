#!/usr/bin/env python
# -*- encoding: utf-8 -*-

from . import Service


class Watchers(Service):

    def list(self, user=None, repo=None):
        request = self.make_request('repos.watchers.list',
            user=user, repo=repo)
        return self._get_result(request)

    def list_repos(self, user=None):
        request = self.make_request('repos.watchers.list_repos', user=user)
        return self._get_result(request)

    def is_watching(self, user=None, repo=None):
        request = self.make_request('repos.watchers.is_watching',
            user=user, repo=repo)
        return self._bool(request)

    def watch(self, user=None, repo=None):
        request = self.make_request('repos.watchers.watch',
            user=user, repo=repo)
        self._put(request)

    def unwatch(self, user=None, repo=None):
        request = self.make_request('repos.watchers.unwatch',
            user=user, repo=repo)
        self._delete(request)
