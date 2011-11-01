#!/usr/bin/env python
# -*- encoding: utf-8 -*-
#
# author: David Medina

from .base import BaseResource
from .user import Plan

class Org(BaseResource):
    """Github Organization object model."""

    _strs = [
        'login', 'url', 'avatar_url', 'name', 'company', 'blog', 'location', 'email'
        'html_url', 'type', 'billing_email']
    _ints = [
        'id', 'public_repos', 'public_gists', 'followers', 'following',
        'total_private_repos', 'owned_private_repos', 'private_gists', 'disk_usage',
        'collaborators']
    _dates = ['created_at']
    _map = {'plan': Plan}
    _writable = ['billing_email', 'blog', 'company', 'email', 'location', 'name']

    @property
    def ri(self):
        return ('orgs', self.login)

    def __repr__(self):
        return '<org {0}>'.format(self.login)
