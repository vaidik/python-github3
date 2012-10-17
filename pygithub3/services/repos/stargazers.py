#!/usr/bin/env python
# -*- encoding: utf-8 -*-

from . import Service


class Stargazers(Service):
    """ Consume `starring API
    <http://developer.github.com/v3/repos/starring>`_ """

    def list(self, user=None, repo=None):
        """ Get repository's stargazers

        :param str user: Username
        :param str repo: Repository
        :returns: A :doc:`result`

        .. note::
            Remember :ref:`config precedence`
        """
        request = self.make_request('repos.stargazers.list',
                                    user=user, repo=repo)
        return self._get_result(request)

    def list_repos(self, user=None):
        """ Get repositories being starred by a user

        :param str user: Username
        :returns: A :doc:`result`

        If you call it without user and you are authenticated, get the
        repositories being starred by the authenticated user.

        .. warning::
            If you aren't authenticated and call without user, it returns 403

        ::

            stargazers_service.list_repos('copitux')
            stargazers_service.list_repos()
        """
        request = self.request_builder('repos.stargazers.list_repos',
                                       user=user)
        return self._get_result(request)

    def is_starring(self, user=None, repo=None):
        """ Check if authenticated user is starring a repository

        :param str user: Username
        :param str repo: Repository

        .. note::
            Remember :ref:`config precedence`

        .. warning::
            You must be authenticated
        """
        request = self.make_request('repos.stargazers.is_starring',
                                    user=user, repo=repo)
        return self._bool(request)

    def star(self, user=None, repo=None):
        """ Star a repository

        :param str user: Username
        :param str repo: Repository

        .. note::
            Remember :ref:`config precedence`

        .. warning::
            You must be authenticated
        """
        request = self.make_request('repos.stargazers.star',
                                    user=user, repo=repo)
        self._put(request)

    def unstar(self, user=None, repo=None):
        """ Stop starring a repository

        :param str user: Username
        :param str repo: Repository

        .. note::
            Remember :ref:`config precedence`

        .. warning::
            You must be authenticated
        """
        request = self.make_request('repos.stargazers.unstar',
                                    user=user, repo=repo)
        self._delete(request)
