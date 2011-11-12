#!/usr/bin/env python
# -*- encoding: utf-8 -*-

from mock import Mock, patch
from unittest import TestCase
from github3 import api
from github3.exceptions import *
import json
import requests


@patch.object(requests.sessions.Session, 'request')
class TestGithubCore(TestCase):

    def setUp(self):
        self.gh = api.GithubCore()
        self.assertEquals(self.gh.base_url, 'https://api.github.com/')
        self.assertEquals(self.gh._parser, json)
        self.base_url = self.gh.base_url
        self.parser = self.gh._parser

    def test_parse_args(self, request_method):
        args = {
            'data': {'some': 'data'},
            'params': {'arg0': 'some'},
            'headers': 'out',
            'auth': 'out',
            'arg1': 'some',
            'arg2': 'some',
            'arg3': {'some': 'data', 'are': {'nested': 'true'}},
        }
        self.gh._parse_args(args)
        self.assertEquals(args, {
            'data': {'some': 'data'},
            'params': {'arg0': 'some', 'arg1': 'some', 'arg2': 'some',
                       'arg3': {'some': 'data', 'are': {'nested': 'true'}}},
            'headers': 'out',
            'auth': 'out',
        })

    def test_raise_errors(self, request_method):
        real_request = (self.gh._request, 'GET', 'test')
        request_method.return_value.status_code = 404
        self.assertRaises(NotFound, *real_request)

        request_method.return_value.status_code = 400
        self.assertRaises(BadRequest, *real_request)

        request_method.return_value.status_code = 422
        self.assertRaises(UnprocessableEntity, *real_request)

        request_method.return_value.status_code = 401
        self.assertRaises(Unauthorized, *real_request)

    def test_get(self, request_method):
        response = request_method.return_value
        response.content = self.parser.dumps({'test': 'test'})
        content = self.gh.get('core')
        request_method.assert_called_with('GET', self.base_url + 'core')
        self.assertEquals(content, {'test': 'test'})

        response = request_method.return_value
        response.headers = {'link': 'url_with_links'}
        response.content = self.parser.dumps({'test': 'test'})
        header, content = self.gh.get('core', paginate=True)
        request_method.assert_called_with('GET', self.base_url + 'core')
        self.assertEquals(header, 'url_with_links')
        self.assertEquals(content, {'test': 'test'})

    def test_head(self, request_method):
        pass  # It has no sense using mocks

    def test_post_and_patch(self, request_method):
        data = {'login': 'test', 'bio': 'test'}
        response = request_method.return_value
        response.status_code = 201
        response.content = self.parser.dumps({'post': 'done'})

        content = self.gh.post('core', data=data)
        request_method.assert_called_with(
            'POST', self.base_url + 'core',
            data=self.parser.dumps(data))
        self.assertEquals(content, {'post': 'done'})

        content = self.gh.post('core')
        request_method.assert_called_with(
            'POST', self.base_url + 'core',
            data=self.parser.dumps(None))
        self.assertEquals(content, {'post': 'done'})

        response.status_code = 200
        content = self.gh.patch('core', data=data)
        request_method.assert_called_with(
            'PATCH', self.base_url + 'core',
            data=self.parser.dumps(data))
        self.assertEquals(content, {'post': 'done'})

        content = self.gh.patch('core')
        request_method.assert_called_with(
            'PATCH', self.base_url + 'core',
            data=self.parser.dumps(None))
        self.assertEquals(content, {'post': 'done'})

    def test_delete(self, request_method):
        data = {'test': 'test'}
        response = request_method.return_value
        response.status_code = 204
        response.content = self.parser.dumps({'delete': 'done'})
        delete = self.gh.delete('core', data=data)
        request_method.assert_called_with(
            'DELETE', self.base_url + 'core',
            data=self.parser.dumps(data))
        delete = self.gh.delete('core')
        request_method.assert_called_with(
            'DELETE', self.base_url + 'core')
