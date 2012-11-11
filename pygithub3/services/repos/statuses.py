#!/usr/bin/env python
# -*- encoding: utf-8 -*-

from . import Service


class Statuses(Service):
    """ Consume `Repo Statuses API
    <http://developer.github.com/v3/repos/statuses>`_ """

    def list(self, sha=None, user=None, repo=None):
        """ Get repository's collaborators

        :param str sha: Commit's sha
        :param str user: Username
        :param str repo: Repository
        :returns: A :doc:`result`

        .. note::
            Remember :ref:`config precedence`
        """

        request = self.make_request('repos.statuses.list',
                                    sha=sha, user=user, repo=repo)
        return self._get_result(request)

    def create(self, data, sha, user=None, repo=None):
        """ Create a status

        :param dict data: Input. See `github statuses doc`_
        :param str sha: Commit's sha
        :param str user: Username
        :param str repo: Repository

        .. note::
            Remember :ref:`config precedence`

        .. warning::
            You must be authenticated

        ::

            data = {
              "state": "success",
              "target_url": "https://example.com/build/status",
              "description": "The build succeeded!"
            }
            statuses_service.create(data, '6dcb09', user='octocat',
                repo='oct_repo')
        """

        request = self.make_request('repos.statuses.create',
                                    sha=sha, user=user, repo=repo, body=data)
        return self._post(request)
