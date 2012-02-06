#!/usr/bin/env python
# -*- encoding: utf-8 -*-

from . import Request, json, RequestValidationError
from pygithub3.resources.users import Key
from pygithub3.resources.base import Raw


class List(Request):

    resource = Key

    def validate(self):
        pass

    def set_uri(self):
        return 'user/keys'


class Get(Request):

    resource = Key

    def validate(self):
        if not self.key_id:
            raise RequestValidationError("'%s' needs key_id"
                                         % self.__class__.__name__)

    def set_uri(self):
        return 'user/keys/%s' % self.key_id


class Add(Request):

    resource = Key
    valid = ('title', 'key')

    def validate(self):
        self.add_data = self._parse_simple_dict(self.add_data)

    def set_uri(self):
        return 'user/keys'

    def get_data(self):
        return json.dumps(self.add_data)


class Update(Request):

    resource = Key
    valid = ('title', 'key')

    def validate(self):
        if not self.key_id:
            raise RequestValidationError("'%s' needs key_id"
                                         % self.__class__.__name__)
        self.update_params = self._parse_simple_dict(self.update_with)

    def set_uri(self):
        return 'user/keys/%s' % self.key_id

    def get_data(self):
        return json.dumps(self.update_params)


class Delete(Request):

    resource = Raw

    def validate(self):
        if not self.key_id:
            raise RequestValidationError("'%s' needs key_id"
                                         % self.__class__.__name__)

    def set_uri(self):
        return 'user/keys/%s' % self.key_id

    def get_data(self):
        return None
