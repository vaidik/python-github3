# -*- encoding: utf-8 -*-

from . import Service


class Teams(Service):
    """ Consume `Teams API <http://developer.github.com/v3/orgs/teams/>`_

    .. warning ::
        You must be authenticated as an owner of the org
    """

    def list(self, org):
        """ Get org's teams

        :param str org: Organisation name
        :returns: A :doc:`result`
        """
        request = self.request_builder('orgs.teams.list', org=org)
        return self._get_result(request)

    def get(self, id):
        """ Get a team

        :param int id: The team id
        :returns: A :doc:`result`
        """
        request = self.request_builder('orgs.teams.get', id=id)
        return self._get(request)

    def create(self, org, name, repo_names=None, permission=None):
        """ Create a new team

        :param str org: Organisation name
        :param str name: Team name
        :param list repo_names: List of repo names to belong to the team
        :param str permission: Permissions to be granted to members
        """
        data = {'name': name}
        if repo_names:
            data['repo_names'] = repo_names
        if permission:
            data['permission'] = permission
        request = self.request_builder('orgs.teams.create', org=org, body=data)
        return self._post(request)

    def update(self, id, name, permission=None):
        """ Update a team

        :param int id: The team id
        :param str name: Team name
        :param str permission: Permissions to be granted to members
        """
        data = {'name': name}
        if permission:
            data['permission'] = permission
        request = self.request_builder('orgs.teams.update', id=id, body=data)
        return self._patch(request)

    def delete(self, id):
        """ Delete a team

        :param int id: The team id
        """
        request = self.request_builder('orgs.teams.delete', id=id)
        return self._delete(request)

    def list_members(self, id):
        """ List the members of a team

        :param int id: The team id
        :returns: A :doc:`result`
        """
        request = self.request_builder('orgs.teams.list_members', id=id)
        return self._get_result(request)

    def is_member(self, id, user):
        """ Determine if user is a member of a team

        :param int id: The team id
        :param str user: User name
        """
        request = self.request_builder('orgs.teams.is_member',
                                       id=id, user=user)
        return self._bool(request)

    def add_member(self, id, user):
        """ Add a user to a team

        :param int id: The team id
        :param str user: User name
        """
        request = self.request_builder('orgs.teams.add_member',
                                       id=id, user=user)
        return self._put(request)

    def remove_member(self, id, user):
        """ Remove a member from a team

        :param int id: The team id
        :param str user: User name
        """
        request = self.request_builder('orgs.teams.remove_member',
                                       id=id, user=user)
        return self._delete(request)

    def list_repos(self, id):
        """ List the repos that a team's members get access to

        :param int id: The team id
        :returns: A :doc:`result`
        """
        request = self.request_builder('orgs.teams.list_repos', id=id)
        return self._get_result(request)

    def contains_repo(self, id, user, repo):
        """ Determine if user is a member of a team

        :param int id: The team id
        :param str user: User name
        :param str repo: Repo name
        """
        request = self.request_builder('orgs.teams.contains_repo',
                                       id=id, user=user, repo=repo)
        return self._bool(request)

    def add_repo(self, id, user, repo):
        """ Give team members access to a repo

        :param int id: The team id
        :param str user: User name
        :param str repo: Repo name
        """
        request = self.request_builder('orgs.teams.add_repo',
                                       id=id, user=user, repo=repo)
        return self._put(request)

    def remove_repo(self, id, user, repo):
        """ Remove a repo from the a team

        :param int id: The team id
        :param str user: User name
        :param str repo: Repo name
        """
        request = self.request_builder('orgs.teams.remove_repo',
                                       id=id, user=user, repo=repo)
        return self._delete(request)
