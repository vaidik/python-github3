#!/usr/bin/env python
# -*- encoding: utf-8 -*-

from datetime import datetime

from pygithub3.services.base import Service
from pygithub3.resources.base import GITHUB_DATE_FORMAT

class Milestones(Service):
    """ Consume `Milestones API
    <http://developer.github.com/v3/issues/milestones>`_ """

    def list(self, user=None, repo=None, state='open', sort='due_date',
            direction='desc'):
        """ List milestones for a repo

        :param str user: Username
        :param str repo: Repo name
        :param str state: 'open' or 'closed'
        :param str sort: 'due_date' or 'completeness'
        :param str direction: 'asc' or 'desc'
        :returns: A :doc:`result`

        .. note::
            Remember :ref:`config precedence`
        """
        request = self.make_request('issues.milestones.list', user=user,
            repo=repo)
        return self._get_result(request, state=state, sort=sort,
            direction=direction)

    def get(self, number, user=None, repo=None):
        """ Get a single milestone

        :param int number: Milestone number
        :param str user: Username
        :param str repo: Repo name

        .. note::
            Remember :ref:`config precedence`
        """
        request = self.make_request('issues.milestones.get', user=user,
            repo=repo, number=number)
        return self._get(request)

    def _normalize_due_on(self, data):
        """ If ``due_on`` comes as ``datetime``, it'll normalize it """
        try:
            due_on = datetime.strptime(data.get('due_on'), GITHUB_DATE_FORMAT)
            data.update({'due_on': due_on})
        except:
            pass

    def create(self, data, user=None, repo=None):
        """ Create a milestone

        :param dict data: Input. See `github milestones doc`_
        :param str user: Username
        :param str repo: Repo name

        .. warning::
            You must be authenticated

        .. note::
            Remember :ref:`config precedence`
        """
        self._normalize_due_on(data)
        request = self.make_request('issues.milestones.create', user=user,
            repo=repo, body=data)
        return self._post(request)

    def update(self, number, data, user=None, repo=None):
        """ Update a milestone

        :param int number: Milestone number
        :param dict data: Input. See `github milestones doc`_
        :param str user: Username
        :param str repo: Repo name

        .. warning::
            You must be authenticated

        .. note::
            Remember :ref:`config precedence`
        """
        self._normalize_due_on(data)
        request = self.make_request('issues.milestones.update', user=user,
            repo=repo, number=number, body=data)
        return self._patch(request)

    def delete(self, number, user=None, repo=None):
        """ Delete a milestone

        :param int number: Milestone number
        :param str user: Username
        :param str repo: Repo name

        .. warning::
            You must be authenticated

        .. note::
            Remember :ref:`config precedence`
        """
        request = self.make_request('issues.milestones.delete', user=user,
            repo=repo, number=number)
        self._delete(request)
