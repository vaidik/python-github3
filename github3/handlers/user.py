#!/usr/bin/env python
# -*- encoding: utf-8 -*-
#
# author: David Medina

from .base import Handler
import github3.models as models
import github3.exceptions as exceptions

class User(Handler):
    """ Handler to query public user api """

    def __init__(self, gh, username):
        if not username:
            raise exceptions.AnomUser("%s need a username" % self.__class__)

        self._url = ('users', username)
        self._model = models.User
        self.username = username
        super(User, self).__init__(gh)

    def __repr__(self):
        return '<handler.User> %s' % self.username

    def get(self):
        return self._get_resource()

    def get_followers(self, limit=None):
        return self._get_resources('followers')

    def get_following(self, limit=None):
        return self._get_resources('following')

    def get_repos(self, limit=None):
        return self._get_resources('repos', model=models.Repo)

    def get_watched(self, limit=None):
        return self._get_resources('watched', model=models.Repo)

    def get_orgs(self, limit=None):
        return self._get_resources('orgs', model=models.Org)

    def get_gists(self, limit=None):
        return self._get_resources('gists', model=models.Gist)

class AuthUser(User):
    """ Handler to query public/private api for authenticated user """

    def __init__(self, gh):
        self._url = ('user',)
        self._model = models.User
        super(User, self).__init__(gh)

    def __repr__(self):
        return '<handler.AuthUser>'

    def get(self):
        return self._get_resource(model=models.AuthUser)

    def get_emails(self):
        return self._get_raw('emails')

