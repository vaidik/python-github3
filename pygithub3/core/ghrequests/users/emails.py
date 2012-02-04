#!/usr/bin/env python
# -*- encoding: utf-8 -*-

from . import Request, json
from pygithub3.resources.base import Raw


class List(Request):

    resource = Raw

    def validate(self):
        pass

    def set_uri(self):
        return 'user/emails'

class Add(Request):

    resource  = Raw

    def validate(self):
        pass

    def get_data(self):
        return json.dumps(self.emails)

    def set_uri(self):
        return 'user/emails'

class Delete(Request):

    resource = Raw

    def validate(self):
        pass

    def get_data(self):
        return json.dumps(self.emails)

    def set_uri(self):
        return 'user/emails'
