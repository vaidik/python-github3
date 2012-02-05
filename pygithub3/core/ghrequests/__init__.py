#!/usr/bin/env python
# -*- encoding: utf-8 -*-

import re
from importlib import import_module
try:
    import simplejson as json
except ImportError:
    import json

ABS_IMPORT_PREFIX = 'pygithub3.core.ghrequests'


class RequestNotFound(Exception):
    pass


class RequestUriInvalid(Exception):
    pass


class RequestValidationError(Exception):
    pass


class Request(object):
    """ """

    def __init__(self, args):
        """ """
        self.args = args
        self.validate()
        self.uri = self.set_uri()

    def validate(self):
        raise NotImplementedError

    def set_uri(self):
        raise NotImplementedError

    def get_data(self):
        raise NotImplementedError

    def get_uri(self):
        return str(self.uri).strip('/')

    def get_resource(self):
        return getattr(self, 'resource', '')

    def __getattr__(self, name):
        return self.args.get(name)

    def __str__(self):
        return self.get_uri()

    def _parse_simple_dict(self, to_parse):
        if not hasattr(to_parse, 'items'):
            raise RequestValidationError("'%s' needs a data dictionary"
                                         % self.__class__.__name__)
        update_params = {
                valid_key: to_parse[valid_key]
                for valid_key in self.valid
                if to_parse.has_key(valid_key)}
        return update_params


class Factory(object):
    """ """

    import_pattern = re.compile(r'^(\w+\.)+\w+$')

    def __init__(self):
        """ """
        self.args = {} 

    def config_with(self, **kwargs):
        self.args = kwargs

    def clear_config(self):
        self.args = {}

    def __validate(func):
        """ """

        def wrapper(self, request_uri):
            if not Factory.import_pattern.match(request_uri):
                raise RequestUriInvalid("'%s' isn't valid form" % request_uri)
            return func(self, request_uri.lower())
        return wrapper

    def __dispatch(func):
        """ """

        def wrapper(self, request_uri):
            module_chunk, s, request_chunk = request_uri.rpartition('.')
            try:
                #  TODO: CamelCase and under_score support, now only Class Name
                module = import_module('%s.%s'
                                        % (ABS_IMPORT_PREFIX, module_chunk))
                request = getattr(module, request_chunk.capitalize())
            except ImportError:
                raise RequestNotFound("'%s' module does not exists"
                                       % module_chunk)
            except AttributeError:
                raise RequestNotFound(
                    "'%s' request doesn't exists into '%s' module"
                    % (request_chunk.capitalize(), module_chunk))
            return func(self, request)
        return wrapper

    @__validate
    @__dispatch
    def __call__(self, request=''):
        request = request(self.args)
        self.clear_config()
        assert isinstance(request, Request)
        return request
