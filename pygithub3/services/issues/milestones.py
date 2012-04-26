# -*- encoding: utf-8 -*-

from pygithub3.services.base import Service

class Milestones(Service):
    """ Consume `Milestones API 
    <http://developer.github.com/v3/issues/milestones>`_ """

    def list(self, user, repo):
        """ List milestones for a repo

        :param str user: Username
        :param str repo: Repo name
        :returns: A :doc:`result`
        """
        request = self.request_builder('issues.milestones.list', 
                                       user=user, 
                                       repo=repo)
        return self._get_result(request)

    def get(self, user, repo, number):
        """ Get a single milestone

        :param str user: Username
        :param str repo: Repo name
        :param int number: Milestone number
        """
        request = self.request_builder('issues.milestones.get', user=user, 
            repo=repo, number=number)
        return self._get(request)

    def create(self, 
               user, 
               repo, 
               title, 
               state=None, 
               description=None, 
               due_on=None):
        """ Create a milestone

        :param str user: Username
        :param str repo: Repo name
        :param str title: Milestone title
        :param str state: Milestone state
        :param str description: Milestone description
        :param date due_on: Milestone due date

        .. warning::
            You must be authenticated
        """
        request = self.request_builder('issues.milestones.create', 
                                       user=user, 
                                       repo=repo,  
                                       body={'title': title,
                                             'state': state,
                                             'due_on': due_on})
        return self._post(request)

    def update(self, 
               user, 
               repo, 
               number, 
               title, 
               state=None, 
               description=None,
               due_on=None):
        """ Update a milestone

        :param str user: Username
        :param str repo: Repo name
        :param int number: Milestone number
        :param str title: Milestone title
        :param str state: Milestone state
        :param str description: Milestone description
        :param date due_on: Milestone due date

        .. warning::
            You must be authenticated
        """
        request = self.request_builder('issues.milestones.update', 
                                        user=user, 
                                        repo=repo, 
                                        number=number, 
                                        body={'title': title,
                                              'state': state,
                                              'description': description,
                                              'due_on': due_on, })
        return self._patch(request)

    def delete(self, user, repo, number):
        """ Delete a milestone

        :param str user: Username
        :param str repo: Repo name
        :param int number: Milestone number

        ... warning::
            You must be authenticated
        """
        request = self.request_builder('issues.milestones.delete', 
                                       user=user,
                                       repo=repo, 
                                       number=number)
        self._delete(request)
