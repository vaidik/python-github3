#!/usr/bin/env python
# -*- encoding: utf-8 -*-

from . import Service


class Forks(Service):

    def list(self, user=None, repo=None, sort='newest'):
        request = self.make_request('repos.forks.list', user=user, repo=repo)
        return self._get_result(request, sort=sort)

    def create(self, user=None, repo=None, org=None):
        request = self.make_request('repos.forks.create', user=user, repo=repo)
        #org = {'org': org} if org else {}
        org = org and {'org': org} or {}
        return self._post(request, **org)
