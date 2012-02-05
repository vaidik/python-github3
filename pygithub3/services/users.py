#!/usr/bin/env python
# -*- encoding: utf-8 -*-

from .base import Base


class Keys(Base):

    def list(self):
        return self._get_result('users.keys.list')

    def get(self, key_id):
        self._config_request(key_id=key_id)
        return self._get('users.keys.get')

    def add(self, data):
        self._config_request(add_data=data)
        return self._post('users.keys.add')

    def update(self, key_id, data):
        self._config_request(key_id=key_id, update_with=data)
        return self._patch('users.keys.update')

    def delete(self, key_id):
        self._config_request(key_id=key_id)
        self._delete('users.keys.delete')


class Followers(Base):

    def list(self, user=None):
        self._config_request(user=user or self.get_user())
        return self._get_result('users.followers.list')

    def list_following(self, user=None):
        self._config_request(user=user or self.get_user())
        return self._get_result('users.followers.listfollowing')

    def is_following(self, user):
        self._config_request(user=user)
        return self._bool('users.followers.isfollowing')

    def follow(self, user):
        self._config_request(user=user)
        self._put('users.followers.follow')

    def unfollow(self, user):
        self._config_request(user=user)
        self._delete('users.followers.unfollow')


class Emails(Base):

    def list(self):
        return self._get_result('users.emails.list')

    def add(self, *args):
        self._config_request(emails=args)
        return self._post('users.emails.add')

    def delete(self, *args):
        self._config_request(emails=args)
        self._delete('users.emails.delete')


class User(Base):

    def __init__(self, **kwargs):
        self.keys = Keys(**kwargs)
        self.emails = Emails(**kwargs)
        self.followers = Followers(**kwargs)
        super(User, self).__init__(**kwargs)

    def get(self, user=None):
        self._config_request(user=user or self.get_user())
        return self._get('users.get')

    def update(self, data):
        self._config_request(update_with=data)
        return self._patch('users.update')
