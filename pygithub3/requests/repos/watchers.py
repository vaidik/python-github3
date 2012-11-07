#!/usr/bin/env python
# -*- encoding: utf-8 -*-

from . import Request
from pygithub3.resources.users import User
from pygithub3.resources.repos import Repo


class List(Request):

    uri = 'repos/{user}/{repo}/subscribers'
    resource = User


class List_repos(Request):

    uri = 'users/{user}/subscriptions'
    resource = Repo

    def clean_uri(self):
        if not self.user:
            return 'user/subscriptions'


class Is_watching(Request):

    uri = 'user/subscriptions/{user}/{repo}'


class Watch(Request):

    uri = 'user/subscriptions/{user}/{repo}'


class Unwatch(Request):

    uri = 'user/subscriptions/{user}/{repo}'
