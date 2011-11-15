#!/usr/bin/env python
# -*- encoding: utf-8 -*-
#
# author: David Medina

from .base import BaseResource


class Plan(BaseResource):
    """Github Plan object model."""

    @classmethod
    def idl(self):
        return {
            'strs': ['name'],
            'ints': ['space', 'collaborators', 'private_repos'],
        }

    def __repr__(self):
        return '<Plan %s>' % self.name


class Key(BaseResource):
    """Github Key object model."""

    @classmethod
    def idl(self):
        return {
            'strs': ['url', 'title', 'key'],
            'ints': ['id'],
        }

    def __repr__(self):
        return '<Key %s>' % self.title


class User(BaseResource):
    """Github User object model."""

    @classmethod
    def idl(self):
        return {
            'strs': [
                'login', 'avatar_url', 'gravatar_id', 'url', 'name',
                'company', 'blog', 'location', 'email', 'bio', 'html_url',
                'type'],
            'ints': [
                'id', 'public_repos', 'public_gists', 'followers', 'following',
                'total_private_repos', 'owned_private_repos', 'private_gists',
                'disk_usage', 'collaborators'],
            'maps': {'plan': Plan},
            'dates': ['created_at', ],
            'bools': ['hireable', ],
        }

    def __repr__(self):
        return '<User %s>' % self.login

    #def handler(self):
    #    return self._gh.user_handler(self.login, force=True)


class AuthUser(User):
    """Github Authenticated User object model."""

    #def handler(self):
    #    return self._gh.user_handler(self.login, force=True, private=True)

    def __repr__(self):
        return '<AuthUser %s>' % self.login
