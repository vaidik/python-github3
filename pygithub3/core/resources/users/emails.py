#!/usr/bin/env python
# -*- encoding: utf-8 -*-

from . import Resource
from pygithub3.models.base import Raw


class List(Resource):

    model = Raw

    def validate(self):
        pass

    def set_uri(self):
        return 'user/emails'
