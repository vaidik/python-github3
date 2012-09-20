# -*- encoding: utf-8 -*-

from pygithub3.requests.base import Request, ValidationError
from pygithub3.resources.events import Event


class List(Request):

    uri = 'events'
    resource = Event
