#!/usr/bin/env python
# -*- encoding: utf-8 -*-

from .base import Resource
from .users import User

class Issue(Resource):

    _dates = ('created_at', 'updated_at')
    _maps = {'assignee': User}

    def __str__(self):
        return '<Issue (%s)>' % getattr(self, 'number', '')


class Comment(Resource):

    _dates = ('created_at', 'update_at')
    _maps = {'user': User}

    def __str__(self):
        return '<Comment (%s)>' % (getattr(self, 'user', ''))


class Event(Resource):

    _dates = ('created_at', )
    _maps = {'actor': User}

    def __str__(self):
        return '<Event (%s)>' % (getattr(self, 'commit_id', ''))