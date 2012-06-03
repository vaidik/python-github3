#!/usr/bin/env python
# -*- encoding: utf-8 -*-

from pygithub3.services.base import Service

class Events(Service):
    """ Consume `Events API 
    <http://developer.github.com/v3/issues/events>`_ """

    def list_by_issue(self, user, repo, number):
        """ List events for an issue

        :param str user: Username
        :param str repo: Repo name
        :param int number: Issue number
        :returns: A :doc:`result`
        """
        request = self.request_builder('issues.events.list_by_issue', 
            user=user, repo=repo, number=number)
        return self._get_result(request)

    def list_by_repo(self, user, repo):
        """ List events for a repository

        :param str user: Username
        :param str repo: Repo name
        :returns: A :doc:`result`
        """
        request = self.request_builder('issues.events.list_by_repo', 
            user=user, repo=repo)
        return self._get_result(request)

    def get(self, user, repo, id):
        """ Get a single event

        :param str user: Username
        :param str repo: Repo name
        :param int id: Comment id
        """
        request = self.request_builder('issues.events.get', user=user, 
            repo=repo, id=id)
        return self._get(request)
