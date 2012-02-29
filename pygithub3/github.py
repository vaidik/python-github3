#!/usr/bin/env python
# -*- encoding: utf-8 -*-

from pygithub3.services.users import User
from pygithub3.services.repos import Repo


class Github(object):
    """
    You can preconfigure all services globally with a ``config`` dict. See
    :attr:`~pygithub3.services.base.Service`

    Example::

        gh = Github(user='kennethreitz', token='ABC...', repo='requests')
    """

    def __init__(self, **config):
        self._users = User(**config)
        self._repos = Repo(**config)

    @property
    def users(self):
        """
        :ref:`User service <User service>`
        """
        return self._users

    @property
    def repos(self):
        """
        :ref:`Repos service <Repos service>`
        """
        return self._repos
