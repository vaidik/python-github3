#!/usr/bin/env python
# -*- encoding: utf-8 -*-

from .base import Resource
from .users import User
from .repos import Repo
from .orgs import Org


class Event(Resource):

    _dates = ('created_at', )
    _maps = {'actor': User, 'repo': Repo, 'org': Org}

    def __str__(self):
        return '<Event (%s)>' % getattr(self, 'type', '')


class RepoEvent(Resource):

    _dates = ('created_at', )
    _maps = {'actor': User, 'repo': Repo, 'org': Org}

    def __str__(self):
        return '<Event (%s)>' % getattr(self, 'type', '')


class NetworkEvent(Resource):

    _dates = ('created_at', )
    _maps = {'actor': User, 'repo': Repo, 'org': Org}

    def __str__(self):
        return '<Event (%s)>' % getattr(self, 'type', '')


class OrgEvent(Resource):

    _dates = ('created_at', )
    _maps = {'actor': User, 'repo': Repo, 'org': Org}

    def __str__(self):
        return '<Event (%s)>' % getattr(self, 'type', '')


class UserEvent(Resource):

    _dates = ('created_at', )
    _maps = {'actor': User, 'repo': Repo, 'org': Org}

    def __str__(self):
        return '<Event (%s)>' % getattr(self, 'type', '')
