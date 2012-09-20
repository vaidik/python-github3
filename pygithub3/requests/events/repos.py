#!/usr/bin/env python
# -*- encoding: utf-8 -*-

from . import Request
from pygithub3.resources.events import RepoEvent


class List(Request):

    uri = 'repos/{user}/{repo}/events'
    resource = RepoEvent
