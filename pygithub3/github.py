#!/usr/bin/env python
# -*- encoding: utf-8 -*-

from pygithub3.services.users import User
from pygithub3.services.repos import Repo


class Github(object):
    """ Main entrance """

    def __init__(self, **config):
        self._users = User(**config)
        self._repos = Repo(**config)

    @property
    def users(self):
        return self._users

    @property
    def repos(self):
        return self._repos
