#!/usr/bin/env python
# -*- encoding: utf-8 -*-
#
# author: David Medina

from .base import BaseResource
from .user import User
from .orgs import Org

class Repo(BaseResource):
    _strs = [
        'url', 'html_url', 'clone_url', 'git_url', 'ssh_url', 'svn_url',
        'name', 'description', 'homepage', 'language', 'master_branch']
    _bools = ['private', 'fork', 'has_issues', 'has_wiki', 'has_downloads']
    _ints = ['forks', 'watchers', 'size', 'open_issues']
    _dates = ['pushed_at', 'created_at']
    _map = {
        'owner': User,
        'organization': Org,
        'parent': 'self',
        'source': 'self',
    }

    @property
    def ri(self):
        return ('repos', self.owner.login, self.name)

    def __repr__(self):
        return '<Repo {0}/{1}>'.format(self.owner.login, self.name)
    # owner
