#!/usr/bin/env python
# -*- encoding: utf-8 -*-

from pygithub3.services.base import Service
from .comments import Comments
from .events import Events

class Issue(Service):
    """ Consume `Issues API <http://developer.github.com/v3/issues>`_ """

    def __init__(self, **config):
        self.comments = Comments(**config)
        self.events = Events(**config)
        super(Issue, self).__init__(**config)

    def list(self, data={}):
        """ List your issues

        :param dict data: Input. See `github issues doc`_
        :returns: A :doc:`result`

        .. warning::
            You must be authenticated
        """
        request = self.request_builder('issues.list', body=data)
        return self._get_result(request)

    def list_by_repo(self, user, repo, data={}):
        """ List issues for a repo

        :param dict data: Input. See `github issues doc`_
        :returns: A :doc:`result`
        """
        request = self.request_builder('issues.list_by_repo', user=user, 
            repo=repo, body=data)
        return self._get_result(request)

    def get(self, user, repo, number):
        """ Get a single issue

        :param str user: Username
        :param str repo: Repo name
        :param int number: Issue number
        """
        request = self.request_builder('issues.get', user=user, repo=repo,
            number=number)
        return self._get(request)

    def create(self, user, repo, data):
        """ Create an issue

        :param str user: Username
        :param str repo: Repo name
        :param dict data: Input. See `github issues doc`_

        .. warning::
            You must be authenticated

        ::

            issues_service.create(dict(title='My test issue', 
                body='This needs to be fixed ASAP.',
                assignee='copitux'))
        """
        request = self.request_builder('issues.create', user=user, repo=repo,
            body=data)
        return self._post(request)

    def update(self, user, repo, number, data):
        """ Edit an issue

        :param str user: Username
        :param str repo: Repo name
        :param int number: Issue number
        :param dict data: Input. See `github issues doc`_

        .. warning::
            You must be authenticated
        """
        request = self.request_builder('issues.edit', user=user, repo=repo,
            number=number, body=data)
        return self._patch(request)