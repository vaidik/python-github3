#!/usr/bin/env python
# -*- encoding: utf-8 -*-

from pygithub3.services.base import Service


class References(Service):
    """Consume `References API <http://developer.github.com/v3/git/refs/>`_"""

    def get(self, ref, user=None, repo=None):
        """Get a reference.

        .. note::
            Remember that branch references look like "heads/<branch_name>"

        """
        return self._get(
            self.make_request('git_data.references.get', ref=ref, user=user,
                              repo=repo)
        )

    def list(self, namespace='', user=None, repo=None):
        """List all the references

        :param str namespace: Limit the request to a particular type of
                              reference. For example, ``heads`` or ``tags``.

        """
        return self._get(
            self.make_request('git_data.references.list', user=user, repo=repo)
        )

    def create(self, body, user=None, repo=None):
        """Create a reference

        :param dict body: Data describing the reference to create
        :param str user: username
        :param str repo: repository name

        """
        return self._post(
            self.make_request('git_data.references.create', body=body,
                              user=user, repo=repo)
        )

    def update(self, ref, body, user=None, repo=None):
        """Update an existing reference

        :param str ref: The SHA of the reference to update
        :param dict body: data

        """
        return self._patch(
            self.make_request('git_data.references.update', ref=ref, body=body,
                              user=user, repo=repo)
        )

    def delete(self, ref, user=None, repo=None):
        """Delete a reference

        :param str ref: The SHA of the reference to delete

        """
        return self._delete(
            self.make_request('git_data.references.delete', ref=ref, user=user,
                              repo=repo)
        )
