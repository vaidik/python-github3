#!/usr/bin/env python
# -*- encoding: utf-8 -*-

from .base import BaseResource
from .user import User

class File(BaseResource):
    """ File model """

    @classmethod
    def idl(self):
        return {
            'strs': ['filename', 'raw_url', 'content', 'language', 'type'],
            'ints': ['size'],
        }

    def __repr__(self):
        return '<File gist> %s' % self.filename

class GistFork(BaseResource):
    """ GistFork model """

    @classmethod
    def idl(self):
        return {
            'strs': ['url'],
            'dates': ['created_at'],
            'maps': {'user': User}
        }

    def __repr__(self):
        return '<Gist fork> %s>' % self.user.login

class ChangeStatus(BaseResource):
    """ ChangeStatus model """

    @classmethod
    def idl(self):
        return {
            'ints': ['deletions', 'additions', 'total'],
        }

    def __repr__(self):
        return '<Gist history> change_status>'

class GistHistory(BaseResource):
    """ """

    @classmethod
    def idl(self):
        return {
            'strs': ['url', 'version'],
            'maps': {'user': User, 'change_status': ChangeStatus},
            'dates': ['committed_at'],
        }

    def __repr__(self):
        return '<GistHistory %s/%s>' % (self.user, self.committed_at)

class Gist(BaseResource):
    """ """

    @classmethod
    def idl(self):
        return {
            'strs': ['url', 'description', 'html_url', 'git_pull_url', 'git_push_url'],
            'ints': ['id', 'comments'],
            'bools': ['public'],
            'dates': ['created_at'],
            'maps': {'user': User},
            'collection_maps': {'files': File, 'forks': GistFork, 'history': GistHistory},
        }

    def __repr__(self):
        return '<Gist %s/%s>' % (self.user, self.description)
