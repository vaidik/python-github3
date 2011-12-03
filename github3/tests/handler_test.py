#!/usr/bin/env python
# -*- encoding: utf-8 -*-

from mock import Mock, patch
from unittest import TestCase
from github3 import api
from github3.handlers.base import Handler, MimeTypeMixin
from github3.exceptions import *
from github3.converters import *
from github3.models.user import User
from fixtures import *
import json
import requests


class TestMimeTypeMixin(TestCase):

    def setUp(self):
        self.mixin = MimeTypeMixin()

    def _parse_mime_type(self, type):
        return 'application/vnd.github.%s.%s+json' % (
            MimeTypeMixin.VERSION, type)

    def test_header(self):
        self.assertEquals(self.mixin.mime_header(), None)

    def test_add_mimetypes(self):
        self.mixin.add_raw()
        self.mixin.add_text()
        self.mixin.add_html()
        self.mixin.add_full()
        self.assertEquals(sorted(self.mixin.mime_header()), sorted({
            'Accept': '%s, %s, %s, %s' % (
            self._parse_mime_type('raw'),
            self._parse_mime_type('text'),
            self._parse_mime_type('html'),
            self._parse_mime_type('full'))}))


class TestHandler(TestCase):

    def setUp(self):
        self.gh = api.Github()
        self.handler = Handler(self.gh)

    def test_get_converter(self):
        self.assertIsInstance(self.handler._get_converter(), Modelizer)
        kwargs = {'converter': Rawlizer}
        self.assertIsInstance(self.handler._get_converter(kwargs),
                              Rawlizer)
        self.assertEquals(kwargs, {})
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

    @patch.object(api.Github, '_request')
    def test_get_resources(self, request):
        #  Simulating per_page=2 with STUB (it returns two resources)
        response = request.return_value
        response.status_code = 200
        response.headers = {'link': GET_LINK}
        response.content = self.gh._parser.dumps(GET_RESOURCES)
        resources = self.handler._get_resources('users', model=User)
        self.assertFalse(request.called)
        resources = list(resources)
        self.assertTrue(request.call_count, 5)
        request_args = ('GET', 'users')
        self.assertEquals(request.call_args_list, [
            (request_args, {'page': 1}),
            (request_args, {'page': 2}),
            (request_args, {'page': 3}),
            (request_args, {'page': 4}),
            (request_args, {'page': 5})])
        self.assertEquals(len(resources), 10)
        self.assertEquals(resources[0].login, 'octocat')

        request.reset_mock()
        resources = self.handler._get_resources('users', model=User, limit=5)
        resources = list(resources)
        self.assertEquals(request.call_count, 3)
        self.assertEquals(len(resources), 5)
        request.reset_mock()
        resources = self.handler._get_resources('users', model=User, limit=4)
        resources = list(resources)
        self.assertEquals(request.call_count, 2)
        self.assertEquals(len(resources), 4)
        request.reset_mock()
        resources = self.handler._get_resources('users', model=User, limit=-5)
        resources = list(resources)
        self.assertEquals(request.call_count, 3)
        self.assertEquals(len(resources), 5)

    @patch.object(api.Github, 'get')
    def test_get_resource(self, get):
        #  Converter test + api(get) test. Half trivial
        get.return_value = {'login': 'octocat'}
        model = self.handler._get_resource('test', model=User)
        self.assertEquals(model.login, 'octocat')

    @patch.object(api.Github, 'post')
    def test_post_resource(self, post):
        post.return_value = {'data': 'posted'}
        data = {'data': 'to_post'}
        user_new = self.handler._post_resource('test', data=data, model=User)
        post.assert_called_with('test', data=data)
