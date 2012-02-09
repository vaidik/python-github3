#!/usr/bin/env python
# -*- encoding: utf-8 -*-

from unittest import TestCase
from mock import Mock

from pygithub3.requests import Factory, Body, json, Request
from pygithub3.exceptions import UriInvalid, DoesNotExists, ValidationError
from pygithub3.tests.utils.requests import (
    RequestWithArgs, RequestCleanedUri, RequestBodyWithSchema, mock_json,
    DummyRequest, RequestCleanedBody)

json.dumps = Mock(side_effect=mock_json)
json.loads = Mock(side_effect=mock_json)


class TestFactory(TestCase):

    def setUp(self):
        self.f = Factory()

    def test_BUILDER_with_invalid_action(self):
        self.assertRaises(UriInvalid, self.f, 'invalid')
        self.assertRaises(UriInvalid, self.f, 'invalid.')
        self.assertRaises(UriInvalid, self.f, '.invalid')

    def test_BUILDER_with_fake_action(self):
        self.assertRaises(DoesNotExists, self.f, 'users.fake')
        self.assertRaises(DoesNotExists, self.f, 'fake.users')

    def test_BUILDER_builds_users(self):
        """ Users.get as real test because it wouldn't be useful mock
        the import-jit process """
        request = self.f('users.get')
        self.assertIsInstance(request, Request)

class TestRequestUri(TestCase):

    def test_SIMPLE_with_correct_args(self):
        request = RequestWithArgs(arg1='arg1', arg2='arg2')
        self.assertEqual(str(request), 'URI/arg1/arg2')

    def test_SIMPLE_without_needed_args(self):
        request = RequestWithArgs()
        self.assertRaises(ValidationError, str, request)

    def test_with_cleaned_uri(self):
        """ Its real uri has args but I override `clean_uri` method, so
        if `nomatters` arg exists, change uri to `URI` """
        request = RequestCleanedUri(notmatters='test')
        self.assertEqual(str(request), 'URI')


class TestRequestBody(TestCase):

    def test_with_schema_with_valid(self):
        request = RequestBodyWithSchema(body=dict(
            arg1='only', fake='t', fake1='t'))
        self.assertEqual(request.get_body(), dict(arg1='only'))

    def test_with_schema_with_invalid(self):
        request = RequestBodyWithSchema(body='invalid_data')
        self.assertRaises(ValidationError, request.get_body)

    def test_with_schema_without_body(self):
        request = RequestBodyWithSchema()
        self.assertIsNone(request.get_body())

    def test_without_schema(self):
        request = DummyRequest(body=dict(arg1='test'))
        self.assertEqual(request.get_body(), dict(arg1='test'))

    def test_without_schema_without_body(self):
        request = DummyRequest()
        self.assertIsNone(request.get_body())

    def test_with_clean_body(self):
        self.assertRaises(ValidationError, RequestCleanedBody)


class TestBodyParsers(TestCase):

    def setUp(self):
        self.b = Body(
            dict(arg1='arg1', arg2='arg2', arg3='arg3', arg4='arg4'),
            ('arg1', 'arg3', 'arg4'))

    def test_RETURN_only_valid_keys(self):
        get_body_returns = self.b.parse()
        self.assertEqual(get_body_returns, dict(arg1='arg1', arg3='arg3',
            arg4='arg4'))
