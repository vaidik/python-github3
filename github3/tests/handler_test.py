#!/usr/bin/env python
# -*- encoding: utf-8 -*-

from mock import Mock, patch
from unittest import TestCase
from github3 import api
from github3.handlers.base import Handler
from github3.exceptions import *
from github3.converters import *
import json
import requests


class TestHandler(TestCase):

    def setUp(self):
        self.gh = api.Github()
        self.handler = Handler(self.gh)

    def test_get_converter(self):
        self.assertIsInstance(self.handler._get_converter(), Modelizer)
        self.assertIsInstance(self.handler._get_converter(converter=Rawlizer),
                              Rawlizer)
        self.handler.converter = Modelizer
        self.assertIsInstance(self.handler._get_converter(), Modelizer)

    def test_bool(self):
        with patch.object(api.Github, 'head') as head:
            response = head.return_value
            response.status_code = 204
            bool1 = self.handler._bool('test')
            head.side_effect = NotFound()
            bool2 = self.handler._bool('test')
        head.assert_called_with('test')
        self.assertTrue(bool1)
        self.assertFalse(bool2)

        with patch.object(api.Github, 'put') as put:
            response = put.return_value
            response.status_code = 204
            booll = self.handler._put('test')
        put.assert_called_with('test', method='put')
        self.assertTrue(booll)

        with patch.object(api.Github, 'delete') as delete:
            response = delete.return_value
            response.content = self.gh._parser.dumps({'data': 'test'})
            response.status_code = 204
            bool1 = self.handler._bool('test', method='delete')
            bool2 = self.handler._bool('test', method='delete',
                                       data={'some': 'data'})
        self.assertTrue(bool1)
        self.assertTrue(bool2)
