#!/usr/bin/env python
# -*- encoding: utf-8 -*-

from . import Request
from pygithub3.resources.users import User

__all__ = ('List',)


class List(Request):

    resource = User

    def validate(self):
        pass

    def set_uri(self):
        if self.user:
            return 'users/%s/followers' % self.user
        else:
            return 'user/followers'


class Listfollowing(Request):

    resource = User

    def validate(self):
        pass

    def set_uri(self):
        if self.user:
            return 'users/%s/following' % self.user
        else:
            return 'user/following'

class Unfollow(Request):

    resource = User

    def validate(self):
        if not self.user:
            raise Exception('unfollow ened user')  # TODO: validate exception

    def set_uri(self):
        return 'user/following/%s' % self.user
