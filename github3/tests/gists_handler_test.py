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

    @patch.object(Handler, '_get_resources')
    def test_all_gists(self, get):
        gists = self.handler.all_gists()
        get.assert_called_with('public', model=Gist, limit=None)

    @patch.object(Handler, '_get_resources')
    def test_my_gists(self, get):
        gists = self.handler.my_gists()
        get.assert_called_with('', model=Gist, limit=None)

    @patch.object(Handler, '_get_resources')
    def test_my_starred_gists(self, get):
        gists = self.handler.my_starred_gists()
        get.assert_called_with('starred', model=Gist, limit=None)

    @patch.object(Handler, '_post_resource')
    def test_create_gist(self, post):
        data = {
            'public': False,
            'files': {'file': {'contents': 'file_data'}},
            'desc': 'some'
        }
        gist = self.handler.create_gist(data['public'], data['files'],
                                        data['desc'])
        post.assert_called_with('', data=data, model=Gist)

    @patch.object(Handler, '_put')
    def test_star_gist(self, put):
        boolean = self.handler.star_gist(1)
        put.assert_called_with('1/star')

    @patch.object(Handler, '_delete')
    def test_unstar_gist(self, delete):
        boolean = self.handler.unstar_gist(1)
        delete.assert_callted_with('1/star')

    @patch.object(Handler, '_bool')
    def test_is_starred(self, bool):
        boolean = self.handler.is_starred(1)
        bool.assert_called_with('1/star')

    @patch.object(Handler, '_post_resource')
    def test_fork_gist(self, post):
        gist = self.handler.fork_gist(1)
        post.assert_called_with('1/fork', data=None, model=Gist)

    @patch.object(Handler, '_delete')
    def test_delete_gist(self, delete):
        boolean = self.handler.delete_gist(1)
        delete.assert_called_with('1')

    @patch.object(Handler, '_post_resource')
    def test_create_comment(self, post):
        gist_comment = self.handler.create_comment(1, 'comment')
        post.assert_called_with('1/comments', data={'body': 'comment'},
            model=GistComment)

    @patch.object(Handler, '_delete')
    def test_delete_comment(self, delete):
        boolean = self.handler.delete_comment(1)
        delete.assert_called_with('comments/1')
