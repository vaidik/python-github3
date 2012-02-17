#!/usr/bin/env python
# -*- encoding: utf-8 -*-

from .base import Service


class Collaborator(Service):

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


class Repo(Service):

    def __init__(self, **config):
        self.collaborators = Collaborator(**config)
        super(Repo, self).__init__(**config)

    def list(self, user=None, type='all'):
        request = self.make_request('repos.list', user=user)
        return self._get_result(request, type=type)

    def list_by_org(self, org, type='all'):
        request = self.make_request('repos.list_by_org', org=org)
        return self._get_result(request, type=type)

    def create(self, data, in_org=None):
        request = self.make_request('repos.create', org=in_org, body=data)
        return self._post(request)

    def get(self, user=None, repo=None):
        request = self.make_request('repos.get', user=user, repo=repo)
        return self._get(request)

    def update(self, data, user=None, repo=None):
        request = self.make_request('repos.update', body=data,
            user=user, repo=repo)
        return self._patch(request)

    def __list_contributors(self, user=None, repo=None, **kwargs):
        request = self.make_request('repos.list_contributors',
            user=user, repo=repo)
        return self._get_result(request, **kwargs)

    def list_contributors(self, user=None, repo=None):
        return self.__list_contributors(user, repo)

    def list_contributors_with_anonymous(self, user=None, repo=None):
        return self.__list_contributors(user, repo, anom=True)

    def list_languages(self, user=None, repo=None):
        request = self.make_request('repos.list_languages',
            user=user, repo=repo)
        return self._get(request)

    def list_teams(self, user=None, repo=None):
        request = self.make_request('repos.list_teams', user=user, repo=repo)
        return self._get_result(request)

    def list_tags(self, user=None, repo=None):
        request = self.make_request('repos.list_tags', user=user, repo=repo)
        return self._get_result(request)

    def list_branches(self, user=None, repo=None):
        request = self.make_request('repos.list_branches',
            user=user, repo=repo)
        return self._get_result(request)
