#!/usr/bin/env python
# -*- encoding: utf-8 -*-

from . import Service


class Collaborators(Service):

    def list(self, user=None, repo=None):
        request = self.make_request('repos.collaborators.list',
            user=user, repo=repo)
        return self._get_result(request)

    def add(self, collaborator, user=None, repo=None):
        request = self.make_request('repos.collaborators.add',
            collaborator=collaborator, user=user, repo=repo)
        return self._put(request)

    def is_collaborator(self, collaborator, user=None, repo=None):
        request = self.make_request('repos.collaborators.is_collaborator',
            collaborator=collaborator, user=user, repo=repo)
        return self._bool(request)

    def delete(self, collaborator, user=None, repo=None):
        request = self.make_request('repos.collaborators.delete',
            collaborator=collaborator, user=user, repo=repo)
        self._delete(request)
