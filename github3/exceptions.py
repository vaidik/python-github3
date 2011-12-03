#!/usr/bin/env python
# -*- encoding: utf-8 -*-

class BadRequest(Exception):
    pass
class UnprocessableEntity(Exception):
    pass
class NotFound(Exception):
    pass
class Unauthorized(Exception):
    pass
class UserIsAnonymous(Exception):
    pass
