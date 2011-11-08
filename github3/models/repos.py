#!/usr/bin/env python
# -*- encoding: utf-8 -*-
#
# author: David Medina

from .base import BaseResource
from .user import User
from .orgs import Org

class Repo(BaseResource):
    """ Repo model """

    @classmethod
    def idl(self):
        return {
            'strs': [
                'url', 'html_url', 'clone_url', 'git_url', 'ssh_url', 'svn_url',
                'name', 'description', 'homepage', 'language', 'master_branch'],
            'ints': ['forks', 'watchers', 'size', 'open_issues'],
            'dates': ['created_at', 'pushed_at'],
            'bools': ['private', 'fork', 'has_issues', 'has_wiki', 'has_downloads'],
            'maps': {
                'owner': User,
                'organization': Org,
                'parent': 'self',
                'source': 'self',
            }
        }

    def __repr__(self):
        return '<Repo %s/%s>' % (self.owner.login, self.name)
