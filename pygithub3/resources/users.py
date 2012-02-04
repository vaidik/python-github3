#!/usr/bin/env python
# -*- encoding: utf-8 -*-

from .base import Resource

__all__ = ('Plan', 'User')


class Plan(Resource):

    def __str__(self):
        return '<Plan (%s)>' % getattr(self, 'name', '')


class User(Resource):
    """ """

    _maps = {'plan': Plan}
    _dates = ('created_at', )

    def __str__(self):
        return '<User (%s)>' % getattr(self, 'login', '')
