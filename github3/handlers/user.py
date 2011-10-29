#!/usr/bin/env python
# -*- encoding: utf-8 -*-
#
# author: David Medina

from .base import Handler

class User(Handler):
    """ Handler to query public user api """

    def __init__(self, gh, username):
        if not username:
            raise exceptions.AnomUser("%s need a username" % self.__class__)

        self._url = ('users', username)
        self._model = models.AnomUser
        self.username = username
        super(User, self).__init__(gh)

    def __repr__(self):
        return '<Handler.AnomUser> %s' % self.username

    def get(self):
        return self._get_resource()

    def get_followers(self, limit=None):
        return self._get_resources('followers')

    def get_following(self, limit=None):
        return self._get_resources('following')

class AuthUser(AnomUser):
    """ Handler to query public/private api for authenticated user """

    def __init__(self, gh):
        self._url = ('user',)
        self._model = models.User
        super(AnomUser, self).__init__(gh)

    def __repr__(self):
        return '<Handler.User>'
