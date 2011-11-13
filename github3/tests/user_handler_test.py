#!/usr/bin/env python
# -*- encoding: utf-8 -*-

from unittest import TestCase
from mock import Mock, patch
from github3 import api
from fixtures import *
from github3.models.user import User, AuthUser
from github3.exceptions import *


class TestUserHandler(TestCase):
    """ Test public api about users """

    def setUp(self):
        self.gh = api.Github()
        self.handler = self.gh.users

    def test_set_username(self):
        handler = self.handler.set_username('test')
        self.assertEquals(id(handler), id(self.handler))
        self.assertEquals(handler.username, 'test')
        model_user = Mock()
        model_user.login = 'test'
        handler = self.handler.set_username(model_user)
        self.assertEquals(handler.username, 'test')

    def test_parse_user(self):
        model_user = Mock()
        model_user.login = 'test'
        self.assertRaises(UserIsAnonymous, self.handler._parse_user, None)
        user = self.handler._parse_user(model_user)
        self.assertEquals(user, 'test')
        user = self.handler._parse_user('test')
        self.assertEquals(user, 'test')
        self.assertRaises(UserIsAnonymous, self.handler._parse_user, Mock())
        self.handler.set_username('octocat')
        self.assertEquals('octocat', self.handler._parse_user(None))
        self.assertEquals('octocat', self.handler._parse_user(Mock()))
        self.assertEquals('test', self.handler._parse_user('test'))
        self.assertEquals('test', self.handler._parse_user(model_user))

    @patch.object(api.Github, 'get')
    def test_get(self, get):
        get.return_value = GET_USER
        self.assertRaises(UserIsAnonymous, self.handler.get)
        user = self.handler.get('octocat')
        self.assertIsInstance(user, User)
        get.assert_called_with('users/octocat')

    @patch.object(api.Github, '_request')
    def test_get_followers(self, request):
        response = request.return_value
        response.headers = {'link': GET_LINK} #  5 pages
        response.content = self.gh._parser.dumps(GET_FOLLOWERS)
        followers = list(self.handler.get_followers('test'))
        self.assertIsInstance(followers[0], User)
        pass
