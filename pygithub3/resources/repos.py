#!/usr/bin/env python
# -*- encoding: utf-8 -*-

from .base import Resource
from .users import User
from .orgs import Org

__all__ = ('Repo', )


class Repo(Resource):

    _dates = ('created_at', 'pushed_at')
    _maps = {'owner': User, 'organization': Org, 'parent': 'self',
             'source': 'self'}

    def __str__(self):
        return '<Repo (%s)>' % getattr(self, 'name', '')


class Team(Resource):

    def __str__(self):
        return '<Team (%s)>' % getattr(self, 'name', '')


class Commit(Resource):

    def __str__(self):
        return '<Commit (%s:%s)>' % (
            getattr(self, 'sha', ''),
            getattr(self, 'message', ''))


class Tag(Resource):

    _maps = {'commit': Commit}

    def __str__(self):
        return '<Tag (%s)>' % getattr(self, 'name', '')


class Branch(Resource):

    _maps = {'commit': Commit}

    def __str__(self):
        return '<Branch (%s)>' % getattr(self, 'name', '')
