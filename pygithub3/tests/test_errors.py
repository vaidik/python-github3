#!/usr/bin/env python
# -*- encoding: utf-8 -*-

from unittest import TestCase
from requests.exceptions import HTTPError
from core import client
import errors
import json

class TestErrorsWithoutAuth(TestCase):
    """docstring for TestRequestsLibrary"""

    def setUp(self):
        self.client = client.Client()

    def test_malformed_url(self):
        self.assertRaises(HTTPError, self.client.request, 'get', 'fake')

class TestErrorsAuthenticated(TestCase):
    """docstring for TestErrorsAuthenticaed"""

    def setUp(self):
        self.client = client.Client(
            login='pygit',
            password='pygithub3'
        )

    def test_400_parsing_json(self):
        data = 'strinf'
        self.assertRaises(errors.BadRequest, self.client.request,
            'post', 'user/repos', data=data)

    def test_400_json_hash(self):
        data = json.dumps({'names': 'david'})
        with self.assertRaises(errors.UnprocessableEntity) as cm:
            self.client.request('post', 'user/repos', data=data)
