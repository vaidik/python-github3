#!/usr/bin/env python
# -*- encoding: utf-8 -*-

try:
    from unittest2 import TestCase  # Python 2.6
except ImportError:
    from unittest import TestCase  # Python >2.7

from .base import Mock, DummyRequest

request = DummyRequest()
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
