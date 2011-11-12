#!/usr/bin/env python
# -*- encoding: utf-8 -*-

from unittest import TestCase
from github3 import api
from github3 import handlers


class TestGetHandlers(TestCase):

    def setUp(self):
        self.anom_gh = api.Github()
        self.auth_gh = api.Github('test', 'password')

    def test_get_user(self):
        anom_user = self.anom_gh.users
        auth_user = self.auth_gh.users

        self.assertEquals(isinstance(anom_user, handlers.users.User), True)
        self.assertEquals(isinstance(auth_user, handlers.users.AuthUser), True)

    def test_get_gists(self):
        anom_gists = self.anom_gh.gists
        auth_gists = self.auth_gh.gists

        self.assertEquals(isinstance(anom_gists, handlers.gists.Gist), True)
        self.assertEquals(
            isinstance(auth_gists, handlers.gists.AuthGist), True)
