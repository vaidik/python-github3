#!/usr/bin/env python
# -*- encoding: utf-8 -*-

import requests
from mock import patch, Mock

from pygithub3.tests.utils.core import TestCase
from pygithub3.resources.base import json
from pygithub3.services.orgs import Org
from pygithub3.tests.utils.base import (mock_response, mock_response_result,
                                        mock_json)
from pygithub3.tests.utils.services import _

json.dumps = Mock(side_effect=mock_json)
json.loads = Mock(side_effect=mock_json)


@patch.object(requests.sessions.Session, 'request')
class TestOrgService(TestCase):

    def setUp(self):
        self.org = Org()

    def test_LIST_without_user(self, request_method):
        request_method.return_value = mock_response_result()
        self.org.list().all()
        self.assertEqual(request_method.call_args[0], ('get', _('user/orgs')))

    def test_LIST_with_user(self, request_method):
        request_method.return_value = mock_response_result()
        self.org.list('octocat').all()
        self.assertEqual(request_method.call_args[0],
            ('get', _('users/octocat/orgs')))

    def test_GET(self, request_method):
        request_method.return_value = mock_response()
        self.org.get('acme')
        self.assertEqual(request_method.call_args[0], ('get', _('orgs/acme')))

    def test_UPDATE(self, request_method):
        request_method.return_value = mock_response('patch')
        self.org.update('acme', {'company': 'ACME Widgets'})
        self.assertEqual(request_method.call_args[0],
            ('patch', _('orgs/acme')))
