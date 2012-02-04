#!/usr/bin/env python
# -*- encoding: utf-8 -*-

from . import Request
from pygithub3.resources.users import User

__all__ = ('Get', 'Update')


class Get(Request):

    resource = User

    def validate(self):
        pass

    def set_uri(self):
        if self.user:
            return 'users/%s' % self.user
        else:
            return 'user'


class Update(Request):
    pass
