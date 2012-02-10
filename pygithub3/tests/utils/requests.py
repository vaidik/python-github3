#!/usr/bin/env python
# -*- encoding: utf-8 -*-

from .base import Request, DummyResource, DummyRequest, mock_json
from pygithub3.exceptions import ValidationError


class RequestWithArgs(Request):

    uri = 'URI/{arg1}/{arg2}'


class RequestCleanedUri(Request):

    uri = 'URI/{arg1}/{arg2}'

    def clean_uri(self):
        if not self.arg1:
            return 'URI'


class RequestBodyWithSchema(Request):
    uri = 'URI'
    body_schema = ('arg1', 'arg2')


class RequestCleanedBody(Request):

    uri = 'URI'

    def clean_body(self):
        raise ValidationError('test')
