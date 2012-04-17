#!/usr/bin/env python
# -*- encoding: utf-8 -*-

from pygithub3.services.base import Service


class Tags(Service):
    """Consume `Tags API <http://developer.github.com/v3/git/tags/>`_"""

    def get(self, sha, user=None, repo=None):
        """Get a tag

        :param str sha: The sha of the tag to get.
        :param str user: Username
        :param str repo: Repository

        """
        return self._get(
            self.make_request('git_data.tags.get', sha=sha, user=user,
                              repo=repo)
        )

    def create(self, body, user=None, repo=None):
        """Create a tag

        :param dict body: Data describing the tag to create
        :param str user: Username
        :param str repo: Repository

        """
        return self._post(
            self.make_request('git_data.tags.create', body=body, user=user,
                              repo=repo)
        )
