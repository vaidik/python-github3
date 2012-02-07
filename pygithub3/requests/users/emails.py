#!/usr/bin/env python
# -*- encoding: utf-8 -*-

import re

from . import Request, ValidationError


class List(Request):

    uri = 'user/emails'


class Add(Request):

    uri = 'user/emails'

    def clean_body(self):
        def is_email(email):
            return re.match(r'.*', email)  # TODO: email regex ;)
        if not self.body:
            raise ValidationError("'%s' request needs emails"
                                  % (self.__class__.__name__))

        return filter(is_email, self.body)


class Delete(Request):

    uri = 'user/emails'
