#!/usr/bin/env python
# -*- encoding: utf-8 -*-

from . import Request

from pygithub3.resources.repos import Status


class List(Request):

    uri = 'repos/{user}/{repo}/statuses/{sha}'
    resource = Status


class Create(Request):

    uri = '/repos/{user}/{repo}/statuses/{sha}'
    resource = Status
    body_schema = {
        'schema': ('state', 'target_url', 'description'),
        'required': ('state',)}
