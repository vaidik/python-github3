#!/usr/bin/env python
# -*- encoding: utf-8 -*-

from .base import Service


class Keys(Service):

    def list(self):
        request = self.make_request('users.keys.list')
        return self._get_result(request)

    def get(self, key_id):
        request = self.make_request('users.keys.get',
            key_id=key_id)
        return self._get(request)

    def add(self, data):
        request = self.make_request('users.keys.add',
            body=data)
        return self._post(request)

    def update(self, key_id, data):
        request = self.make_request('users.keys.update',
            key_id=key_id, body=data)
        return self._patch(request)

    def delete(self, key_id):
        request = self.make_request('users.keys.delete',
            key_id=key_id)
        self._delete(request)


class Followers(Service):

    def list(self, user=None):
        request = self.make_request('users.followers.list', user=user)
        return self._get_result(request)

    def list_following(self, user=None):
        request = self.make_request('users.followers.listfollowing', user=user)
        return self._get_result(request)

    def is_following(self, user):
        request = self.make_request('users.followers.isfollowing', user=user)
        return self._bool(request)

    def follow(self, user):
        request = self.make_request('users.followers.follow', user=user)
        self._put(request)

    def unfollow(self, user):
        request = self.make_request('users.followers.unfollow', user=user)
        self._delete(request)


class Emails(Service):

    def list(self):
        request = self.make_request('users.emails.list')
        return self._get_result(request)

    def add(self, *emails):
        request = self.make_request('users.emails.add', body=emails)
        return self._post(request)

    def delete(self, *emails):
        request = self.make_request('users.emails.delete', body=emails)
        self._delete(request)


class User(Service):

    def __init__(self, **config):
        self.keys = Keys(**config)
        self.emails = Emails(**config)
        self.followers = Followers(**config)
        super(User, self).__init__(**config)

    def get(self, user=None):
        request = self.make_request('users.get', user=user)
        return self._get(request)

    def update(self, data):
        request = self.make_request('users.update', body=data)
        return self._patch(request)
