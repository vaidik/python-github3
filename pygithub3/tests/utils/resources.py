#!/usr/bin/env python
# -*- encoding: utf-8 -*-

from pygithub3.resources.base import Resource


class Simple(Resource):
    pass


class HasSimple(Resource):
    _maps = {'simple': Simple}


class Nested(Resource):
    _dates = ('date', )
    _maps = {'simple': Simple}
    _collection_maps = {
        'list_collection': HasSimple,
        'items_collections': HasSimple
    }
