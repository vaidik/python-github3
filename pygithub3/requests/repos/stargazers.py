#!/usr/bin/env python
# -*- encoding: utf-8 -*-

from . import Request
from pygithub3.resources.users import User
from pygithub3.resources.repos import Repo


class List(Request):

    uri = 'repos/{user}/{repo}/stargazers'
    resource = User


class List_repos(Request):

    uri = 'users/{user}/starred'
    resource = Repo

    def clean_uri(self):
        if not self.user:
            return 'user/starred'


class Is_starring(Request):

    uri = 'user/starred/{user}/{repo}'


class Star(Request):

    uri = 'user/starred/{user}/{repo}'


class Unstar(Request):

    uri = 'user/starred/{user}/{repo}'
