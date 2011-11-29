#!/usr/bin/env python
# -*- encoding: utf-8 -*-

from .base import Handler, MimeTypeMixin
from github3 import models


class Gist(Handler, MimeTypeMixin):
    """ Gist handler with public access """

    prefix = 'gists'

    def __repr__(self):
        return '<Gist handler>'

    def all_gists(self, limit=None):
        """ Return all public gists

        NOTE: It returns all gists in github environment. Maybe you
        want to use `limit` parameter
        """

        return self._get_resources('', model=models.Gist, limit=limit)

    def get(self, gist_id):
        """ Return gist

        param `gist_id`: Gist id
        """

        return self._get_resource(gist_id, model=models.Gist)

    def get_comments(self, gist_id, limit=None):
        """ Return gist's comments

        param `gist_id`: Gist id
        param `limit`: Number of comments
        """

        return self._get_resources('%s/comments' % gist_id,
            model=models.GistComment, limit=limit,
            headers=self.mime_header())

    def get_comment(self, comment_id):
        """ Return gist's comment

        param `comment_id`: Comment id
        """

        return self._get_resource('comments/%s' % comment_id,
            model=models.GistComment, headers=self.mime_header())


class AuthGist(Gist):

    def create_gist(self, description, public=True, files={}):
        """ Create a gist """
        data = {'description': description,
                'public': public,
                'files': files}
        return self._post_resource('', data=data, model=models.Gist)
