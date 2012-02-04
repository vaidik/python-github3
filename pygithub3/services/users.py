#!/usr/bin/env python
# -*- encoding: utf-8 -*-

from .base import Base


class Keys(Base):

    def list(self):
        return self.get_resource('user/keys')


class Followers(Base):

    def list(self, user=None):
        self.config_request(user=user or self.client.user)
        return self._get_result('users.followers.list')

    def list_following(self, user=None):
        self.config_request(user=user or self.client.user)
        return self._get_result('users.followers.listfollowing')

    def unfollow(self, user):
        self.config_request(user=user)
        self._delete('users.followers.unfollow')

class Emails(Base):

    def list(self):
        return self._get_result('users.emails.list')

    def add(self, *args):
        self.config_request(emails=args)
        return self._post('users.emails.add')

    def delete(self, *args):
        self.config_request(emails=args)
        self._delete('users.emails.delete')


class User(Base):

    def __init__(self, **kwargs):
        self.keys = Keys(**kwargs)
        self.emails = Emails(**kwargs)
        self.followers = Followers(**kwargs)
        super(User, self).__init__(**kwargs)

    def get(self, user=None):
        self.config_request(user=user or self.client.user)
        return self._get('users.get')

    def update(self):
        pass
