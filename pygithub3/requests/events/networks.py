#!/usr/bin/env python
# -*- encoding: utf-8 -*-

from . import Request
from pygithub3.resources.events import NetworkEvent


class List(Request):

    uri = 'networks/{user}/{repo}/events'
    resource = NetworkEvent
