#!/usr/bin/env python
# -*- encoding: utf-8 -*-

from pygithub3.services.base import Service

class Comments(Service):
    """ Consume `Comments API 
    <http://developer.github.com/v3/issues/comments>`_ """

    def list(self, user, repo, number):
        """ List comments for an issue

        :param str user: Username
        :param str repo: Repo name
        :param int number: Issue number
        :returns: A :doc:`result`
        """
        request = self.request_builder('issues.comments.list', user=user, 
            repo=repo, number=number)
        return self._get_result(request)

    def get(self, user, repo, id):
        """ Get a single comment

        :param str user: Username
        :param str repo: Repo name
        :param int id: Comment id
        """
        request = self.request_builder('issues.comments.get', user=user, 
            repo=repo, id=id)
        return self._get(request)

    def create(self, user, repo, number, message):
        """ Create a comment on an issue

        :param str user: Username
        :param str repo: Repo name
        :param int number: Issue number
        :param str message: Comment message

        .. warning::
            You must be authenticated
        """
        request = self.request_builder('issues.comments.create', user=user, 
            repo=repo, number=number, body={'body': message})
        return self._post(request)

    def update(self, user, repo, id, message):
        """ Update a comment on an issue

        :param str user: Username
        :param str repo: Repo name
        :param int id: Issue id
        :param str message: Comment message

        .. warning::
            You must be authenticated
        """
        request = self.request_builder('issues.comments.edit', user=user, 
            repo=repo, id=id, body={'body': message})
        return self._patch(request)

    def delete(self, user, repo, id):
        """ Delete a single comment

        :param str user: Username
        :param str repo: Repo name
        :param int id: Comment id

        ... warning::
            You must be authenticated
        """
        request = self.request_builder('issues.comments.delete', user=user,
            repo=repo, id=id)
        self._delete(request)