#!/usr/bin/env python
# -*- encoding: utf-8 -*-

import re
from importlib import import_module
try:
    import simplejson as json
except ImportError:
    import json

from pygithub3.exceptions import DoesNotExists, UriInvalid, ValidationError
from pygithub3.resources.base import Raw

ABS_IMPORT_PREFIX = 'pygithub3.requests'


class Body(object):

    def __init__(self, content, schema):
        self.content = content
        self.schema = schema

    def dumps(self):
        if not self.content:
            return None
        return json.dumps(self.parse())

    def parse(self):
        if not self.schema:
            return self.content
        if not hasattr(self.content, 'items'):
            raise ValidationError("'%s' needs a content dictionary"
                                   % self.__class__.__name__)
        return {key: self.content[key] for key in self.schema
                if key in self.content}


class Request(object):
    """ """

    uri = ''
    resource = Raw
    body_schema = ()

    def __init__(self, args):
        """ """
        self.body = args.pop('body', None)
        self.args = args
        self.clean()

    def clean(self):
        self.uri = self.clean_uri() or self.uri
        self.body = Body(self.clean_body(), self.body_schema)

    def clean_body(self):
        return self.body

    def clean_uri(self):
        return None

    @property
    def resource(self):
        return self.resource

    def __getattr__(self, name):
        return self.args.get(name)

    def __str__(self):
        return self.populate_uri()

    def populate_uri(self):
        try:
            populated_uri = self.uri.format(**self.args)
        except KeyError:
            raise ValidationError(
                "'%s' request wasn't be able to populate the uri '%s' with "
                "'%s' args" % (self.__class__.__name__, self.uri, self.args))
        return str(populated_uri).strip('/')

    def get_body(self):
        return self.body.dumps()


class Factory(object):
    """ """

    import_pattern = re.compile(r'^(\w+\.)+\w+$')

    def __validate(func):
        """ """

        def wrapper(self, request_uri, **kwargs):
            if not Factory.import_pattern.match(request_uri):
                raise UriInvalid("'%s' isn't valid form" % request_uri)
            return func(self, request_uri.lower(), **kwargs)
        return wrapper

    def __dispatch(func):
        """ """

        def wrapper(self, request_uri, **kwargs):
            module_chunk, s, request_chunk = request_uri.rpartition('.')
            try:
                #  TODO: CamelCase and under_score support, now only Class Name
                module = import_module('%s.%s'
                                        % (ABS_IMPORT_PREFIX, module_chunk))
                request = getattr(module, request_chunk.capitalize())
            except ImportError:
                raise DoesNotExists("'%s' module does not exists"
                                       % module_chunk)
            except AttributeError:
                raise DoesNotExists(
                    "'%s' request doesn't exists into '%s' module"
                    % (request_chunk.capitalize(), module_chunk))
            return func(self, request, **kwargs)
        return wrapper

    @__validate
    @__dispatch
    def __call__(self, request='', **kwargs):
        request = request(kwargs)
        assert isinstance(request, Request)
        return request
