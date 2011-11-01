#!/usr/bin/env python
# -*- encoding: utf-8 -*-
#
# author: David Medina

from .base import BaseResource

class Plan(BaseResource):
    """Github Plan object model."""

    _strs = ['name']
    _ints = ['space', 'collaborators', 'private_repos']

    def __repr__(self):
        return '<Plan {0}>'.format(str(self.name))

class Key(BaseResource):
    """Github Key object model."""

    _strs = ['url', 'title', 'key']
    _ints = ['id']

    def __repr__(self):
        return '<Key {0}>'.format(str(self.title))

class User(BaseResource):
    """Github User object model."""

    _strs = [
        'login','avatar_url', 'url', 'name', 'company', 'blog', 'location',
        'email', 'bio', 'html_url', 'type']

    _ints = ['id', 'public_repos', 'public_gists', 'followers', 'following']
    _dates = ['created_at',]
    _bools = ['hireable', ]

    @property
    def ri(self):
        return ('users', self.login)

    def __repr__(self):
        return '<model.User {0}>'.format(self.login)

    def handler(self):
        return self._gh.user_handler(self.login, force=True)

class AuthUser(User):
    """Github Current User object model."""

    _ints = [
        'id', 'public_repos', 'public_gists', 'followers', 'following',
        'total_private_repos', 'owned_private_repos', 'private_gists',
        'disk_usage', 'collaborators']
    _map = {'plan': Plan}
    _writeable = ['name', 'email', 'blog', 'company', 'location', 'hireable', 'bio']

    def handler(self):
        return self._gh.user_handler(self.login, force=True, private=True)

    @property
    def ri(self):
        return ('user',)

    def __repr__(self):
        return '<model.AuthUser {0}>'.format(self.login)

