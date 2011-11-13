#!/usr/bin/env python
# -*- encoding: utf-8 -*-

from unittest import TestCase
from mock import Mock, patch
from github3 import api
from fixtures import *
from github3.models import User, AuthUser, Repo, Gist, Org
from github3.exceptions import *


class TestAuthUserHandler(TestCase):
    """ Test private api about user logged """

    def setUp(self):
        pass


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
        response.headers = {'link': GET_LINK}
        response.content = self.gh._parser.dumps(GET_SHORT_USERS)  # 2 users
        followers = list(self.handler.get_followers('test'))
        request.assert_called_with('GET', 'users/test/followers', page=5)
        self.assertIsInstance(followers[0], User)
        self.assertEquals(len(followers), 10)
        followers = list(self.handler.get_followers('test', limit=2))
        self.assertEquals(len(followers), 2)
        self.assertEquals(followers[0].login, 'octocat')

    @patch.object(api.Github, '_request')
    def test_get_following(self, request):
        response = request.return_value
        response.headers = {'link': GET_LINK}
        response.content = self.gh._parser.dumps(GET_SHORT_USERS)  # 2 users
        following = list(self.handler.get_following('test'))
        request.assert_called_with('GET', 'users/test/following', page=5)
        self.assertIsInstance(following[0], User)
        self.assertEquals(len(following), 10)
        following = list(self.handler.get_following('test', limit=2))
        self.assertEquals(len(following), 2)

    @patch.object(api.Github, '_request')
    def test_get_repos(self, request):
        response = request.return_value
        response.headers = {'link': GET_LINK}
        response.content = self.gh._parser.dumps(GET_SHORT_REPOS)  # 1 repo
        repos = list(self.handler.get_repos('test'))
        request.assert_called_with('GET', 'users/test/repos', page=5)
        self.assertIsInstance(repos[0], Repo)
        self.assertEquals(len(repos), 5)
        repos = list(self.handler.get_repos('test', limit=2))
        self.assertEquals(len(repos), 2)
        self.assertIsInstance(repos[0].owner, User)

    @patch.object(api.Github, '_request')
    def test_get_watched(self, request):
        response = request.return_value
        response.headers = {'link': GET_LINK}
        response.content = self.gh._parser.dumps(GET_SHORT_REPOS)  # 1 repo
        watched = list(self.handler.get_watched('test'))
        request.assert_called_with('GET', 'users/test/watched', page=5)
        self.assertIsInstance(watched[0], Repo)
        self.assertEquals(len(watched), 5)
        watched = list(self.handler.get_watched('test', limit=2))
        self.assertEquals(len(watched), 2)

    @patch.object(api.Github, '_request')
    def test_get_orgs(self, request):
        response = request.return_value
        response.headers = {'link': GET_LINK}
        response.content = self.gh._parser.dumps(GET_SHORT_ORGS)  # 1 repo
        orgs = list(self.handler.get_orgs('test'))
        request.assert_called_with('GET', 'users/test/orgs', page=5)
        self.assertIsInstance(orgs[0], Org)
        self.assertEquals(len(orgs), 5)
        orgs = list(self.handler.get_orgs('test', limit=2))
        self.assertEquals(len(orgs), 2)
        self.assertEquals(orgs[0].login, 'github')

    @patch.object(api.Github, '_request')
    def test_get_gists(self, request):
        response = request.return_value
        response.headers = {'link': GET_LINK}
        response.content = self.gh._parser.dumps(GET_SHORT_GISTS)  # 1 repo
        gists = list(self.handler.get_gists('test'))
        request.assert_called_with('GET', 'users/test/gists', page=5)
        self.assertIsInstance(gists[0], Gist)
        self.assertEquals(len(gists), 5)
        gists = list(self.handler.get_gists('test', limit=2))
        self.assertEquals(len(gists), 2)
        self.assertIsInstance(gists[0].files, dict)
        from github3.models.gists import File
        self.assertIsInstance(gists[0].files['ring.erl'], File)
