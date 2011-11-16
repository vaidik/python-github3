#!/usr/bin/env python
# -*- encoding: utf-8 -*-

from unittest import TestCase
from mock import Mock, patch
from github3 import api
from fixtures import *
from github3.models import User, AuthUser, Repo, Gist, Org, Key
from github3.exceptions import *


class TestAuthUserHandler(TestCase):
    """ Test private api about user logged """

    def setUp(self):
        self.gh = api.Github('test', 'pass')
        self.handler = self.gh.users
        self.user_mock = Mock()
        self.user_mock.login = 'user_model'

    @patch.object(api.Github, 'get')
    def test_get(self, get):
        get.return_value = GET_FULL_USER
        user = self.handler.get()
        self.assertIsInstance(user, AuthUser)
        get.assert_called_with('user')
        self.assertEquals(len(user), len(GET_FULL_USER))

    @patch.object(api.Github, 'get')
    def test_get_emails(self, get):
        get.return_value = GET_USER_EMAILS
        emails = self.handler.get_emails()
        get.assert_called_with('user/emails')
        self.assertEquals(emails, GET_USER_EMAILS)

    @patch.object(api.Github, 'post')
    def test_create_emails(self, post):
        post.return_value = GET_USER_EMAILS
        emails = self.handler.create_emails(*GET_USER_EMAILS)
        post.assert_called_with('user/emails', data=GET_USER_EMAILS)
        self.assertEquals(emails, GET_USER_EMAILS)

    @patch.object(api.Github, 'delete')
    def test_delete_emails(self, delete):
        response = delete.return_value
        response.return_value = ''
        response.status_code = 204
        emails = self.handler.delete_emails(*GET_USER_EMAILS)
        delete.assert_called_with('user/emails', data=GET_USER_EMAILS,
                                  method='delete')
        self.assertTrue(emails)

    @patch.object(api.Github, 'head')
    def test_is_following(self, head):
        response = head.return_value
        response.status_code = 204
        self.assertTrue(self.handler.is_following('test'))
        head.assert_called_with('user/following/test')
        self.handler.is_following(self.user_mock)
        head.assert_called_with('user/following/user_model')

    @patch.object(api.Github, 'put')
    def test_follow(self, put):
        response = put.return_value
        response.status_code = 204
        self.assertTrue(self.handler.follow('test'))
        put.assert_called_with('user/following/test', method='put')

    @patch.object(api.Github, 'delete')
    def test_unfollow(self, delete):
        response = delete.return_value
        response.status_code = 204
        self.assertTrue(self.handler.unfollow('test'))
        delete.assert_called_with('user/following/test', method='delete')

    @patch.object(api.Github, '_request')
    def test_get_keys(self, request):
        response = request.return_value
        response.status_code = 200
        response.content = self.gh._parser.dumps(GET_USER_KEYS)
        response.headers = {'link': GET_LINK}  # 1 per page
        keys = list(self.handler.get_keys())
        self.assertEquals(len(keys), 5)
        self.assertIsInstance(keys[0], Key)
        request.assert_called_with('GET', 'user/keys', page=5)
        keys = list(self.handler.get_keys(limit=2))
        self.assertEquals(len(keys), 2)

    @patch.object(api.Github, 'get')
    def test_get_key(self, get):
        get.return_value = GET_USER_KEYS[0]
        key = self.handler.get_key(1)
        self.assertIsInstance(key, Key)
        get.assert_called_with('user/keys/1')
        model_key = Mock()
        model_key.id = 1
        key = self.handler.get_key(model_key)
        get.assert_called_with('user/keys/1')

    @patch.object(api.Github, 'post')
    def test_create_key(self, post):
        post.return_value = GET_USER_KEYS[0]
        key_data = {'title': 'some', 'key': 'ssh-rsa AAA'}
        created_key = self.handler.create_key(**key_data)
        self.assertIsInstance(created_key, Key)
        post.assert_called_with('user/keys', data=key_data)

    @patch.object(api.Github, 'delete')
    def test_delete_key(self, delete):
        response = delete.return_value
        response.status_code = 204
        self.assertTrue(self.handler.delete_key(1))
        delete.assert_called_with('user/keys/1', method='delete')
        model_key = Mock()
        model_key.id = 1
        key = self.handler.delete_key(model_key)
        delete.assert_called_with('user/keys/1', method='delete')

    @patch.object(api.Github, '_request')
    def test_get_repos(self, request):
        response = request.return_value
        response.status_code = 200
        response.content = self.gh._parser.dumps(GET_SHORT_REPOS)
        response.headers = {'link': GET_LINK}  # 1 per page
        repos = list(self.handler.get_repos(filter='public'))
        self.assertEquals(len(repos), 5)
        self.assertIsInstance(repos[0], Repo)
        request.assert_called_with('GET', 'user/repos',
                                   page=5, type='public')
        repos = list(self.handler.get_repos(limit=2))
        self.assertEquals(len(repos), 2)

    @patch.object(api.Github, 'head')
    def test_is_watching_repo(self, head):
        response = head.return_value
        response.status_code = 204
        self.assertTrue(self.handler.is_watching_repo('user', 'repo'))
        head.assert_called_with('user/watched/user/repo')
        model_user, model_repo = Mock(), Mock()
        model_user.login = 'user'
        model_repo.name = 'repo'
        self.assertTrue(self.handler.is_watching_repo('user', 'repo'))
        head.assert_called_with('user/watched/user/repo')

    @patch.object(api.Github, 'put')
    def test_watch_repo(self, put):
        response = put.return_value
        response.status_code = 204
        self.assertTrue(self.handler.watch_repo('user', 'repo'))
        put.assert_called_with('user/watched/user/repo', method='put')
        model_user, model_repo = Mock(), Mock()
        model_user.login = 'user'
        model_repo.name = 'repo'
        self.assertTrue(self.handler.watch_repo('user', 'repo'))
        put.assert_called_with('user/watched/user/repo', method='put')

    @patch.object(api.Github, 'delete')
    def test_unwatch_repo(self, delete):
        response = delete.return_value
        response.status_code = 204
        self.assertTrue(self.handler.unwatch_repo('user', 'repo'))
        delete.assert_called_with('user/watched/user/repo', method='delete')
        model_user, model_repo = Mock(), Mock()
        model_user.login = 'user'
        model_repo.name = 'repo'
        self.assertTrue(self.handler.unwatch_repo('user', 'repo'))
        delete.assert_called_with('user/watched/user/repo', method='delete')


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
