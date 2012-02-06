#!/usr/bin/env python
# -*- encoding: utf-8 -*-

from . import Request, RequestValidationError
from pygithub3.resources.users import User
from pygithub3.resources.base import Raw


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


class Isfollowing(Request):

    resource = Raw

    def validate(self):
        if not self.user:
            raise RequestValidationError(
                "'%s' request needs a user" % self.__class__.__name__)

    def set_uri(self):
        return 'user/following/%s' % self.user


class Follow(Request):

    resource = Raw

    def validate(self):
        if not self.user:
            raise RequestValidationError(
                "'%s' request needs a user" % self.__class__.__name__)

    def set_uri(self):
        return 'user/following/%s' % self.user


class Unfollow(Request):

    resource = User

    def validate(self):
        if not self.user:
            raise RequestValidationError(
                "'%s' request needs a user" % self.__class__.__name__)

    def set_uri(self):
        return 'user/following/%s' % self.user

    def get_data(self):
        pass
