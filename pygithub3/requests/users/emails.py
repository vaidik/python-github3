#!/usr/bin/env python
# -*- encoding: utf-8 -*-

import re

from . import Request


class List(Request):

    uri = 'users/emails'


class Add(Request):

    uri = 'user/emails'

    def clean_body(self):

        def is_email(email):
            return re.match(r'.*', email)  # TODO: email regex ;)

        return filter(is_email, self.body)


class Delete(Request):

    uri = 'user/emails'
