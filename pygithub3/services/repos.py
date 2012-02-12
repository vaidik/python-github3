#!/usr/bin/env python
# -*- encoding: utf-8 -*-

from .base import Base


class Repo(Base):

    def __init__(self, **config):
        super(Repo, self).__init__(**config)

    def list(self, user=None, type='all'):
        request = self.make_request('repos.list',
                user=user or self.get_user())
        return self._get_result(request, type=type)

    def list_by_org(self, org, type='all'):
        request = self.make_request('repos.list_by_org', org=org)
        return self._get_result(request, type=type)

    def create(self, data, in_org=None):
        request = self.make_request('repos.create', org=in_org, body=data)
        return self._post(request)

    def get(self, user=None, repo=None):
        request = self.make_request('repos.get',
            user=user or self.get_user(),
            repo=repo or self.get_repo())
        return self._get(request)

    def update(self, data, user=None, repo=None):
        request = self.make_request('repos.update',
            body=data,
            user=user or self.get_user(),
            repo=repo or self.get_repo())
        return self._patch(request)

    def __list_contributors(self, user=None, repo=None, **kwargs):
        request = self.make_request('repos.list_contributors',
            user=user or self.get_user(),
            repo=repo or self.get_repo())
        return self._get_result(request, **kwargs)

    def list_contributors(self, user=None, repo=None):
        return self.__list_contributors(user, repo)

    def list_contributors_with_anonymous(self, user=None, repo=None):
        return self.__list_contributors(user, repo, anom=True)

    def list_languages(self, user=None, repo=None):
        request = self.make_request('repos.list_languages',
            user=user or self.get_user(),
            repo=repo or self.get_repo())
        return self._get(request)

    def list_teams(self, user=None, repo=None):
        request = self.make_request('repos.list_teams',
            user=user or self.get_user(),
            repo=repo or self.get_repo())
        return self._get_result(request)

    def list_tags(self, user=None, repo=None):
        request = self.make_request('repos.list_tags',
            user=user or self.get_user(),
            repo=repo or self.get_repo())
        return self._get_result(request)

    def list_branches(self, user=None, repo=None):
        request = self.make_request('repos.list_branches',
            user=user or self.get_user(),
            repo=repo or self.get_repo())
        return self._get_result(request)
