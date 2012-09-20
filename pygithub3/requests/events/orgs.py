#!/usr/bin/env python
# -*- encoding: utf-8 -*-

from . import Request
from pygithub3.resources.events import OrgEvent


class List(Request):

    uri = 'orgs/{org}/events'
    resource = OrgEvent
