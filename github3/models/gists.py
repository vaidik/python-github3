#!/usr/bin/env python
# -*- encoding: utf-8 -*-
#
# author: David Medina

from .base import BaseResource
from .user import User

class File(BaseResource):
    _strs = ['filename', 'raw_url', 'content', 'language', 'type']
    _ints = ['size']

    def __repr__(self):
        return '<File gist> %s' % self.filename

class GistFork(BaseResource):
    _strs = ['url']
    _dates = ['created_at']
    _map = {'user': User}

    def __repr__(self):
        return '<Gist fork> %s>' % self.user.login

class ChangeStatus(BaseResource):
    _ints = ['deletions', 'additions', 'total']

    def __repr__(self):
        return '<Gist history> change_status>'

class GistHistory(BaseResource):
    _strs = ['url', 'version']
    _map = {'user': User, 'change_status': ChangeStatus}
    _dates = ['committed_at']

class Gist(BaseResource):
    _strs = ['url', 'description', 'html_url', 'git_pull_url', 'git_push_url']
    _ints = ['id', 'comments']
    _bools = ['public']
    _dates = ['created_at']
    _map = {'user': User}
    _list_map = {'files': File, 'forks': GistFork, 'history': GistHistory}

    @property
    def ri(self):
        return ('users', self.user.login, self.id)

    def __repr__(self):
        return '<gist %s/%s>' % (self.user.login, self.description)

