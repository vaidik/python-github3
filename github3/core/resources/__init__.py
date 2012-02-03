#!/usr/bin/env python
# -*- encoding: utf-8 -*-

import re

class UriNotFound(Exception):
    pass


class UriInvalid(Exception):
    pass


class Resource(object):
    """ """

    def __init__(self, args):
        """ """
        self.args = args
        self.validate()
        self.uri = self.set_uri()

    def validate(self, args):
        raise NotImplementedError

    def set_uri(self):
        raise NotImplementedError

    def get_uri(self):
        return str(self.uri).strip('/')

    def get_model(self):
        return getattr(self, 'model', '')

    def __getattr__(self, name):
        return self.args.get(name)

    def __str__(self):
        return self.get_uri()


class Factory(object):
    """ """
    import_pattern = re.compile(r'^(\w+\.)+\w+$')

    def __init__(self, **kwargs):
        self.args = kwargs

    def __validate(func):
        """ """

        def wrapper(self, resource_path):
            if not Factory.import_pattern.match(resource_path):
                raise UriInvalid("'%s' isn't valid form" % resource_path)
            return func(self, resource_path.lower())
        return wrapper

    def __dispatch(func):
        """ """

        from importlib import import_module
        def wrapper(self, resource_path):
            module_chunk, s, uri_chunk = resource_path.rpartition('.')
            try:
                #  TODO: CamelCase and under_score support, now only Class Name
                module = import_module('core.resources.%s' % module_chunk)
                uri = getattr(module, uri_chunk.capitalize())
            except ImportError:
                raise UriNotFound("'%s' module does not exists" % module_chunk)
            except AttributeError:
                raise UriNotFound("'%s' uri doesn't exists into '%s' module"
                                 % (uri_chunk.capitalize(), module_chunk))
            return func(self, uri)
        return wrapper

    @__validate
    @__dispatch
    def __call__(self, resource_class=''):
        resource = resource_class(self.args)
        assert isinstance(resource, Resource)
        return resource 
