#!/usr/bin/env python
# -*- encoding: utf-8 -*-

from github3.converters import *
from github3.models.base import BaseResource
from unittest import TestCase
from datetime import datetime

API_STUB = {
    'test_str': 'string',
    'test_int': 1,
    'test_date': '2008-01-14T04:33:35Z',
    'test_bool': True,
    'map': {'test_str': 'string'},
    'dict_map': {
        'map1': {
            'test_str': 'string',
            'test_int': 1
        },
        'map2': {
            'test_str': 'string',
            'test_int': 2
        },
    },
    'list_map': [
        {'test_str': 'string', 'test_int': 1},
        {'test_str': 'string', 'test_int': 2},
    ],
    'fake_map': 9,
}


class Model(BaseResource):

    @classmethod
    def idl(self):
        return {
            'strs': ['test_str'],
            'ints': ['test_int'],
            'dates': ['test_date'],
            'bools': ['test_bool'],
            'maps': {'map': Model, 'fake_map': Model},
            'collection_maps': {
                'dict_map': Model,
                'list_map': Model,
                'fake_map': Model,
            },
        }


class TestModelizer(TestCase):

    def setUp(self):
        model = Model
        self.modelizer = Modelizer()
        self.modelizer.inject(model)

    def test_loads(self):
        parsed_model = self.modelizer.loads(API_STUB)
        self.assertEquals(len(parsed_model), len(API_STUB))
        self.assertEquals(parsed_model.test_str, 'string')
        self.assertEquals(parsed_model.test_int, 1)
        self.assertEquals(
            parsed_model.test_date,
            datetime(2008, 1, 14, 4, 33, 35))
        self.assertTrue(parsed_model.test_bool)
        self.assertTrue(isinstance(parsed_model.map, Model))
        self.assertEquals(parsed_model.map.test_str, 'string')
        self.assertTrue(isinstance(parsed_model.dict_map, dict))
        map1 = parsed_model.dict_map['map1']
        map2 = parsed_model.dict_map['map2']
        self.assertTrue(isinstance(map1, Model))
        self.assertTrue(isinstance(map2, Model))
        self.assertEquals(map1.test_str, 'string')
        self.assertEquals(map1.test_int, 1)
        self.assertEquals(map2.test_str, 'string')
        self.assertEquals(map2.test_int, 2)

        list_map = parsed_model.list_map
        self.assertTrue(isinstance(list_map, list))
        self.assertEquals(list_map[0].test_str, 'string')
        self.assertEquals(list_map[0].test_int, 1)
        self.assertEquals(list_map[1].test_str, 'string')
        self.assertEquals(list_map[1].test_int, 2)


class TestRawlizer(TestCase):

    def setUp(self):
        model = Model
        self.rawlizer = Rawlizer()

    #  Trivial, I know it
    def test_loads(self):
        raw = self.rawlizer.loads(API_STUB)
        self.assertEquals(raw, API_STUB)
