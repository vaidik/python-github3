#!/usr/bin/env python
# -*- encoding: utf-8 -*-

from unittest import TestCase

import requests
from mock import patch, Mock

from pygithub3.services.users import User
from pygithub3.resources.base import json
from pygithub3.tests.utils.base import mock_response
from pygithub3.tests.utils.services import _, mock_json

json.dumps = Mock(side_effect=mock_json)
json.loads = Mock(side_effect=mock_json)

@patch.object(requests.sessions.Session, 'request')
class TestUserService(TestCase):

    def setUp(self):
        self.us = User()

    def test_GET_without_user(self, request_method):
        request_method.return_value = mock_response()
        self.us.get()
        request_method.assert_called_with('get', _('user'), params={})
