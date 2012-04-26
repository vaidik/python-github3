#!/usr/bin/env python
# -*- encoding: utf-8 -*-

import requests
from mock import patch, Mock

from pygithub3.tests.utils.core import TestCase
from pygithub3.resources.base import json
from pygithub3.services.issues import Issue, Comments, Events, Labels, Milestones
from pygithub3.tests.utils.base import (mock_response, mock_response_result,
                                        mock_json)
from pygithub3.tests.utils.services import _

json.dumps = Mock(side_effect=mock_json)
json.loads = Mock(side_effect=mock_json)


@patch.object(requests.sessions.Session, 'request')
class TestIssuesService(TestCase):

    def setUp(self):
        self.isu = Issue()

    def test_LIST_without_user(self, request_method):
        request_method.return_value = mock_response_result()
        self.isu.list().all()
        self.assertEqual(request_method.call_args[0], ('get', _('issues')))

    def test_LIST_by_repo(self, request_method):
        request_method.return_value = mock_response_result()
        self.isu.list_by_repo('octocat', 'Hello-World').all()
        self.assertEqual(request_method.call_args[0],
            ('get', _('repos/octocat/Hello-World/issues')))

    def test_GET(self, request_method):
        request_method.return_value = mock_response()
        self.isu.get('octocat', 'Hello-World', 1)
        self.assertEqual(request_method.call_args[0],
            ('get', _('repos/octocat/Hello-World/issues/1')))

    def test_CREATE(self, request_method):
        request_method.return_value = mock_response('post')
        self.isu.create('octocat', 'Hello-World', 
            dict(title='My issue', body='Fix this issue'))
        self.assertEqual(request_method.call_args[0],
            ('post', _('repos/octocat/Hello-World/issues')))

    def test_UPDATE(self, request_method):
        request_method.return_value = mock_response('patch')
        self.isu.update('octocat', 'Hello-World', 1, 
            {'body': 'edited'})
        self.assertEqual(request_method.call_args[0],
            ('patch', _('repos/octocat/Hello-World/issues/1')))


@patch.object(requests.sessions.Session, 'request')
class TestCommentService(TestCase):

    def setUp(self):
        self.cs = Comments()

    def test_LIST(self, request_method):
        request_method.return_value = mock_response_result()
        self.cs.list('octocat', 'Hello-World', 1).all()
        self.assertEqual(request_method.call_args[0],
            ('get', _('repos/octocat/Hello-World/issues/1/comments')))

    def test_GET(self, request_method):
        request_method.return_value = mock_response()
        self.cs.get('octocat', 'Hello-World', 1)
        self.assertEqual(request_method.call_args[0],
            ('get', _('repos/octocat/Hello-World/issues/comments/1')))

    def test_CREATE(self, request_method):
        request_method.return_value = mock_response('post')
        self.cs.create('octocat', 'Hello-World', 1, 'comment')
        self.assertEqual(request_method.call_args[0],
            ('post', _('repos/octocat/Hello-World/issues/1/comments')))

    def test_UPDATE(self, request_method):
        request_method.return_value = mock_response('patch')
        self.cs.update('octocat', 'Hello-World', 1, 'new comment')
        self.assertEqual(request_method.call_args[0],
            ('patch', _('repos/octocat/Hello-World/issues/comments/1')))

    def test_DELETE(self, request_method):
        request_method.return_value = mock_response('delete')
        self.cs.delete('octocat', 'Hello-World', 1)
        self.assertEqual(request_method.call_args[0],
            ('delete', _('repos/octocat/Hello-World/issues/comments/1')))


@patch.object(requests.sessions.Session, 'request')
class TestEventsService(TestCase):

    def setUp(self):
        self.ev = Events()

    def test_LIST_by_issue(self, request_method):
        request_method.return_value = mock_response_result()
        self.ev.list_by_issue('octocat', 'Hello-World', 1).all()
        self.assertEqual(request_method.call_args[0],
            ('get', _('repos/octocat/Hello-World/issues/1/events')))

    def test_LIST_by_repo(self, request_method):
        request_method.return_value = mock_response_result()
        self.ev.list_by_repo('octocat', 'Hello-World').all()
        self.assertEqual(request_method.call_args[0],
            ('get', _('repos/octocat/Hello-World/issues/events')))

    def test_GET(self, request_method):
        request_method.return_value = mock_response()
        self.ev.get('octocat', 'Hello-World', 1)
        self.assertEqual(request_method.call_args[0],
            ('get', _('repos/octocat/Hello-World/issues/events/1')))


@patch.object(requests.sessions.Session, 'request')
class TestLabelsService(TestCase):

    def setUp(self):
        self.lb = Labels()

    def test_GET(self, request_method):
        request_method.return_value = mock_response()
        self.lb.get('octocat', 'Hello-World', 'bug')
        self.assertEqual(request_method.call_args[0],
            ('get', _('repos/octocat/Hello-World/labels/bug')))

    def test_CREATE(self, request_method):
        request_method.return_value = mock_response('post')
        self.lb.create('octocat', 'Hello-World', 'bug', 'FF0000')
        self.assertEqual(request_method.call_args[0],
            ('post', _('repos/octocat/Hello-World/labels')))

    def test_UPDATE(self, request_method):
        request_method.return_value = mock_response('patch')
        self.lb.update('octocat', 'Hello-World', 'bug', 'critical', 'FF0000')
        self.assertEqual(request_method.call_args[0],
            ('patch', _('repos/octocat/Hello-World/labels/bug')))

    def test_DELETE(self, request_method):
        request_method.return_value = mock_response('delete')
        self.lb.delete('octocat', 'Hello-World', 'bug')
        self.assertEqual(request_method.call_args[0],
            ('delete', _('repos/octocat/Hello-World/labels/bug')))

    def test_LIST_by_repo(self, request_method):
        request_method.return_value = mock_response()
        self.lb.list_by_repo('octocat', 'Hello-World')
        self.assertEqual(request_method.call_args[0],
            ('get', _('repos/octocat/Hello-World/labels')))

    def test_LIST_by_issue(self, request_method):
        request_method.return_value = mock_response()
        self.lb.list_by_issue('octocat', 'Hello-World', 1)
        self.assertEqual(request_method.call_args[0],
            ('get', _('repos/octocat/Hello-World/issues/1/labels')))

    def test_ADD_to_issue(self, request_method):
        request_method.return_value = mock_response('post')
        self.lb.add_to_issue('octocat', 'Hello-World', 1, ['bug', 'critical'])
        self.assertEqual(request_method.call_args[0],
            ('post', _('repos/octocat/Hello-World/issues/1/labels')))

    def test_REMOVE_from_issue(self, request_method):
        request_method.return_value = mock_response('delete')
        self.lb.remove_from_issue('octocat', 'Hello-World', 1, 'bug')
        self.assertEqual(request_method.call_args[0],
            ('delete', _('repos/octocat/Hello-World/issues/1/labels/bug')))

    def test_REPLACE_all(self, request_method):
        self.lb.replace_all('octocat', 'Hello-World', 1, ['bug', 'critical'])
        self.assertEqual(request_method.call_args[0],
            ('put', _('repos/octocat/Hello-World/issues/1/labels')))

    def test_REMOVE_all(self, request_method):
        request_method.return_value = mock_response('delete')
        self.lb.remove_all('octocat', 'Hello-World', 1)
        self.assertEqual(request_method.call_args[0],
            ('delete', _('repos/octocat/Hello-World/issues/1/labels')))
        

@patch.object(requests.sessions.Session, 'request')
class TestMilestonesService(TestCase):

    def setUp(self):
        self.mi = Milestones()

    def test_LIST_by_repo(self, request_method):
        request_method.return_value = mock_response_result()
        self.mi.list('octocat', 'Hello-World').all()
        self.assertEqual(request_method.call_args[0],
            ('get', _('repos/octocat/Hello-World/milestones')))

    def test_GET(self, request_method):
        request_method.return_value = mock_response()
        self.mi.get('octocat', 'Hello-World', 1)
        self.assertEqual(request_method.call_args[0],
            ('get', _('repos/octocat/Hello-World/milestones/1')))

    def test_CREATE(self, request_method):
        request_method.return_value = mock_response('post')
        self.mi.create('octocat', 'Hello-World', 'title')
        self.assertEqual(request_method.call_args[0],
            ('post', _('repos/octocat/Hello-World/milestones')))

    def test_UPDATE(self, request_method):
        request_method.return_value = mock_response('patch')
        self.mi.update('octocat', 'Hello-World', 1, 'critical')
        self.assertEqual(request_method.call_args[0],
            ('patch', _('repos/octocat/Hello-World/milestones/1')))

    def test_DELETE(self, request_method):
        request_method.return_value = mock_response('delete')
        self.mi.delete('octocat', 'Hello-World', 1)
        self.assertEqual(request_method.call_args[0],
            ('delete', _('repos/octocat/Hello-World/milestones/1')))
