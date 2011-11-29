#!/usr/bin/env python
# -*- encoding: utf-8 -*-

from unittest import TestCase
from mock import Mock, patch
from github3 import api
from github3.models import Gist, GistComment
from github3.handlers.base import Handler


class TestGistHandler(TestCase):

    def setUp(self):
        self.gh = api.Github()
        self.handler = self.gh.gists

    @patch.object(Handler, '_get_resources')
    def test_get_gists(self, get):
        gists = self.handler.all_gists()
        get.assert_called_with('', model=Gist, limit=None)

    @patch.object(Handler, '_get_resource')
    def test_get(self, get):
        gist = self.handler.get(1)
        get.assert_called_with(1, model=Gist)

    @patch.object(Handler, '_get_resources')
    def test_get_comments(self, get):
        comments = self.handler.get_comments(1)
        get.assert_called_with('1/comments', model=GistComment, limit=None,
            headers=None)

    @patch.object(Handler, '_get_resource')
    def test_get_comment(self, get):
        comment = self.handler.get_comment(1)
        get.assert_called_with('comments/1', model=GistComment, headers=None)

class TestAuthGistHandler(TestCase):

    def setUp(self):
        self.gh = api.Github('test', 'pass')
        self.handler = self.gh.gists

    def test_inherit(self):
        self.assertTrue(hasattr(self.handler, 'get'))
        self.assertTrue(hasattr(self.handler, 'get_comments'))
        self.assertTrue(hasattr(self.handler, 'get_comment'))

