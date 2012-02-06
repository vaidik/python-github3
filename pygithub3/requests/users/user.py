#!/usr/bin/env python
# -*- encoding: utf-8 -*-

from . import Request, json
from pygithub3.resources.users import User

__all__ = ('Get', 'Update')


class Get(Request):

    resource = User

    def validate(self):
        pass

    def set_uri(self):
        if self.user:
            return 'users/%s' % self.user
        else:
            return 'user'


class Update(Request):

    resource = User
    valid = ('name', 'email', 'blog', 'company', 'location', 'hireable', 'bio')

    def validate(self):
        self.update_params = self._parse_simple_dict(self.update_with)

    def get_data(self):
        return json.dumps(self.update_params)

    def set_uri(self):
        return 'user'
