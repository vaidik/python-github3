#!/usr/bin/env python
# -*- encoding: utf-8 -*-

from . import Request, ValidationError
from pygithub3.resources.users import User

__all__ = ('Get', 'Update')


class Get(Request):

    resource = User
    uri = 'users/{user}'

    def clean_uri(self):
        if not self.user:
            return 'user'


class Update(Request):

    resource = User
    uri = 'user'
    body_schema = (
        'name', 'email', 'blog', 'company', 'location','hireable', 'bio')
