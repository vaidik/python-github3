#!/usr/bin/env python
# -*- encoding: utf-8 -*-

from mock import Mock

from pygithub3.resources.base import Resource
from pygithub3.requests import Request


class DummyResource(Resource):
    pass


def loads_mock(content):
    return content
DummyResource.loads = Mock(side_effect=loads_mock)


class DummyRequest(Request):
    uri = 'dummyrequest'
    resource = DummyResource


request = DummyRequest({})
# Working without json but name it json-related to not confuse
json_content = [dict(name='dummy')]


def mock_paginate_github_in_GET(request, page):
    def header(page):
        return {'link': '<https://d.com/d?page=%s>; rel="last"' % page}

    def content(page):
        if page >= 3:
            return json_content
        return json_content * 2

    response = Mock()
    response.headers = header(3)
    response.content = content(page)
    return response


def mock_no_paginate_github_in_GET(request, page):
    response = Mock()
    response.headers = {}
    response.content = [json_content * 3]
    return response
