#!/usr/bin/env python
# -*- encoding: utf-8 -*-

from mock import Mock

from pygithub3.resources.base import Resource
from pygithub3.requests import Request


def mock_json(content):
    return content


class DummyResource(Resource):
    pass


def loads_mock(content):
    return content
DummyResource.loads = Mock(side_effect=loads_mock)


class DummyRequest(Request):
    uri = 'dummyrequest'
    resource = DummyResource
