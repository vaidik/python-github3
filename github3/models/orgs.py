#!/usr/bin/env python
# -*- encoding: utf-8 -*-
#
# author: David Medina

from .base import BaseResource
from .user import Plan

class Org(BaseResource):
    """Github Organization object model."""

    @classmethod
    def idl(self):
        return {
            'strs': ['login', 'url', 'avatar_url', 'name', 'company', 'blog',
                     'location', 'email', 'html_url', 'type', 'billing_email'],
            'ints': ['id', 'public_repos', 'public_gists', 'followers',
                     'following', 'total_private_repos', 'owned_private_repos',
                     'private_gists', 'disk_usage', 'collaborators'],
            'dates': ['created_at'],
            'maps': {'plan': Plan}
        }

    def __repr__(self):
        return '<Org %s>' % self.login
