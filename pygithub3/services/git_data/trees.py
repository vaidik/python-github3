#!/usr/bin/env python
# -*- encoding: utf-8 -*-

from pygithub3.services.base import Service


class Trees(Service):
    """Consume `Trees API <http://developer.github.com/v3/git/trees/>`_"""

    def get(self, sha, recursive=False, user=None, repo=None):
        """Get a tree object

        :param str sha: The SHA of the tree you want.
        :param bool recursive: Whether to resolve each sub-tree belonging to
                               this tree
        :param str user: Username
        :param str repo: Repository

        """
        return self._get(
            self.make_request('git_data.trees.get', sha=sha,
                              recursive=recursive, user=user, repo=repo)
        )

    def create(self, body, user=None, repo=None):
        """Create a tree object

        :param dict body: Data describing the tree to create

        """
        return self._post(
            self.make_request('git_data.trees.create', body=body, user=user,
                              repo=repo)
        )
