#!/usr/bin/env python
# -*- encoding: utf-8 -*-
#
# author: David Medina

from .base import BaseResource

class User(BaseResource):
    """Github User object model."""

    _strs = [
        'login','avatar_url', 'url', 'name', 'company', 'blog', 'location',
        'email', 'bio', 'html_url']

    _ints = ['id', 'public_repos', 'public_gists', 'followers', 'following']
    _dates = ['created_at',]
    _bools = ['hireable', ]
    # _map = {}
    # _writeable = []

    @property
    def ri(self):
        return ('users', self.login)

    def __repr__(self):
        return '<User {0}>'.format(self.login)

    @property
    def handler(self):
        return self._gh.user_handler(self.login)

    def get_followers(self, limit=None):
        return self.handler.followers(limit)

    def get_following(self, limit=None):
        return self.handler.following(limit)

    def repos(self, limit=None):
        return self._gh._get_resources(('users', self.login, 'repos'), Repo, limit=limit)
    def repo(self, reponame):
         return self._gh._get_resource(('repos', self.login, reponame), Repo)

    def orgs(self):
        return self._gh._get_resources(('users', self.login, 'orgs'), Org)

    def gists(self):
        return self._gh._get_resources(('users', self.login, 'gists'), Gist)

class AuthUser(User):
    """Github Current User object model."""

    _ints = [
        'id', 'public_repos', 'public_gists', 'followers', 'following',
        'total_private_repos', 'owned_private_repos', 'private_gists',
        'disk_usage', 'collaborators']
    _map = {'plan': Plan}
    _writeable = ['name', 'email', 'blog', 'company', 'location', 'hireable', 'bio']

    @property
    def ri(self):
        return ('user',)

    def __repr__(self):
        return '<current-user {0}>'.format(self.login)

    def repos(self, limit=None):
         return self._gh._get_resources(('user', 'repos'), Repo, limit=limit)

    def repo(self, reponame):
         return self._gh._get_resource(('repos', self.login, reponame), Repo)

    def orgs(self, limit=None):
        return self._gh._get_resources(('user', 'orgs'), Org,  limit=limit)

    def org(self, orgname):
        return self._gh._get_resource(('orgs', orgname), Org)

    def gists(self, limit=None):
        return self._gh._get_resources('gists', Gist, limit=limit)
