#!/usr/bin/env python
# -*- encoding: utf-8 -*-

from .base import Handler
from .. import models


class Gist(Handler):
    """ Gist handler """

    prefix = 'gists'

    def __repr__(self):
        return '<Gist handler>'

    def get(self, gist_id):
        """ Return gist """

        return self._get_resource(gist_id, model=models.Gist)


class AuthGist(Gist):

    def create_gist(self, description, public=True, files={}):
        """ Create a gist """
        data = {'description': description,
                'public': public,
                'files': files}
        return self._post_resource('', data=data, model=models.Gist)
