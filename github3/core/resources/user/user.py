#!/usr/bin/env python
# -*- encoding: utf-8 -*-

from . import Resource
from models.user import User

__all__ = ('Get', 'Update')

class Get(Resource):

    model = User

    def validate(self):
        pass

    def set_uri(self):
        if self.user:
            return 'users/%s' % self.user
        else:
            return 'user'

class Update(Resource):
    pass
