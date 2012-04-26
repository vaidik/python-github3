# -*- encoding: utf-8 -*-

from pygithub3.services.base import Service


class Labels(Service):
    """ Consume `Labels API 
    <http://developer.github.com/v3/issues/labels>`_ """

    def get(self, user, repo, name):
        """ Get a single label

        :param str user: Username
        :param str repo: Repo name
        :param str name: Label name
        """
        request = self.request_builder('issues.labels.get', user=user, 
            repo=repo, name=name)
        return self._get(request)

    def create(self, user, repo, name, color):
        """ Create a label on an repo

        :param str user: Username
        :param str repo: Repo name
        :param str name: Label name
        :param str color: Label color

        .. warning::
            You must be authenticated
        """
        request = self.request_builder('issues.labels.create', 
                                       user=user, 
                                       repo=repo, 
                                       body={'name': name,
                                             'color': color,})
        return self._post(request)

    def update(self, user, repo, name, new_name, color):
        """ Update a label on an repo

        :param str user: Username
        :param str repo: Repo name
        :param str name: Label name
        :param str name: Label new name
        :param str color: Label color

        .. warning::
            You must be authenticated
        """
        request = self.request_builder('issues.labels.update', 
                                       user=user, 
                                       repo=repo, 
                                       name=name,
                                       body={'name': new_name,
                                             'color': color,})
        return self._patch(request)

    def delete(self, user, repo, name):
        """ Delete a label on an repo

        :param str user: Username
        :param str repo: Repo name
        :param str name: Label name

        .. warning::
            You must be authenticated
        """
        request = self.request_builder('issues.labels.delete', 
                                       user=user, 
                                       repo=repo, 
                                       name=name)
        return self._delete(request)

    def list_by_repo(self, user, repo):
        """ List all labels for a repo

        :param str user: Username
        :param str repo: Repo name
        :returns: A :doc:`result`
        """
        request = self.request_builder('issues.labels.list_by_repo', 
                                       user=user, 
                                       repo=repo,)
        return self._get(request)

    def list_by_issue(self, user, repo, number):
        """ List labels for an issue

        :param str user: Username
        :param str repo: Repo name
        :param int number: Issue number
        :returns: A :doc:`result`
        """
        request = self.request_builder('issues.labels.list_by_issue', user=user, 
            repo=repo, number=number)
        return self._get(request)

    def add_to_issue(self, user, repo, number, labels):
        """ Add labels to issue

        :param str user: Username
        :param str repo: Repo name
        :param int number: Issue number
        :param list labels: List of label names
        :returns: A :doc:`result`
        """
        request = self.request_builder('issues.labels.add_to_issue', 
                                       user=user, 
                                       repo=repo, 
                                       number=number,
                                       body=labels)
        return self._post(request)

    def remove_from_issue(self, user, repo, number, label):
        """ Remove a label from an issue

        :param str user: Username
        :param str repo: Repo name
        :param int number: Issue number
        :param str label: Label name
        :returns: A :doc:`result`
        """
        request = self.request_builder('issues.labels.remove_from_issue', 
                                       user=user, 
                                       repo=repo, 
                                       number=number,
                                       name=label)
        return self._delete(request)

    def replace_all(self, user, repo, number, labels):
        """ Replace all labels of a issue

        :param str user: Username
        :param str repo: Repo name
        :param int number: Issue number
        :param list labels: New labels 
        :returns: A :doc:`result`
        """
        request = self.request_builder('issues.labels.replace_all', 
                                       user=user, 
                                       repo=repo, 
                                       number=number,
                                       body=labels,)
        return self._put(request)

    def remove_all(self, user, repo, number):
        """ Remove all labels from a issue

        :param str user: Username
        :param str repo: Repo name
        :param int number: Issue number
        :returns: A :doc:`result`
        """
        request = self.request_builder('issues.labels.remove_all', 
                                       user=user, 
                                       repo=repo, 
                                       number=number,)
        return self._delete(request)
