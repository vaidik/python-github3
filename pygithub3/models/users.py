#!/usr/bin/env python
# -*- encoding: utf-8 -*-

from .base import Model

__all__ = ('Plan', 'User')


class Plan(Model):

    def __str__(self):
        return '<Plan (%s)>' % getattr(self, 'name', '')


class User(Model):
    """ """

    maps = {'plan': Plan}
    dates = ('created_at', )

    def __str__(self):
        return '<User (%s)>' % getattr(self, 'login', '')
