#!/usr/bin/env python
# -*- encoding: utf-8 -*-
#
# author: David Medina

class BadRequest(Exception):
    pass
class UnprocessableEntity(Exception):
    pass
class NotFound(Exception):
    pass
class AnomUser(Exception):
    """ Exception for AnomUser handler """
    pass
