#!/usr/bin/env python
# -*- encoding: utf-8 -*-

from .base import Base
from pygithub3.core.resources import Factory


class Keys(Base):

    def list(self):
        return self.get_resource('user/keys')


class Followers(Base):

    def list(self, user):
        pass


class Emails(Base):

    def list(self):
        pass

    def add(self):
        pass

    def delete(self):
        pass


class User(Base):

    def __init__(self, **kwargs):
        self.keys = Keys(**kwargs)
        self.emails = Emails(**kwargs)
        self.followers = Followers(**kwargs)
        super(User, self).__init__(**kwargs)

    def get(self, user):
        resource = Factory(user=user or self.client.user)
        return self._get_result(resource('users.get'))

    def update(self):
        pass
