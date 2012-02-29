#!/usr/bin/env python
# -*- encoding: utf-8 -*-

import requests

from .base import Service, MimeTypeMixin


class Watchers(Service):

    def list(self, user=None, repo=None):
        request = self.make_request('repos.watchers.list',
            user=user, repo=repo)
        return self._get_result(request)

    def list_repos(self, user=None):
        request = self.make_request('repos.watchers.list_repos', user=user)
        return self._get_result(request)

    def is_watching(self, user=None, repo=None):
        request = self.make_request('repos.watchers.is_watching',
            user=user, repo=repo)
        return self._bool(request)

    def watch(self, user=None, repo=None):
        request = self.make_request('repos.watchers.watch',
            user=user, repo=repo)
        self._put(request)

    def unwatch(self, user=None, repo=None):
        request = self.make_request('repos.watchers.unwatch',
            user=user, repo=repo)
        self._delete(request)


class Keys(Service):

    def list(self, user=None, repo=None):
        request = self.make_request('repos.keys.list', user=user, repo=repo)
        return self._get_result(request)

    def get(self, id, user=None, repo=None):
        request = self.make_request('repos.keys.get',
            id=id, user=user, repo=repo)
        return self._get(request)

    def create(self, data, user=None, repo=None):
        request = self.make_request('repos.keys.create',
            body=data, user=user, repo=repo)
        return self._post(request)

    def update(self, id, data, user=None, repo=None):
        request = self.make_request('repos.keys.update',
            id=id, body=data, user=user, repo=repo)
        return self._patch(request)

    def delete(self, id, user=None, repo=None):
        request = self.make_request('repos.keys.delete',
            id=id, user=user, repo=repo)
        self._delete(request)


class Forks(Service):

    def list(self, user=None, repo=None, sort='newest'):
        request = self.make_request('repos.forks.list', user=user, repo=repo)
        return self._get_result(request, sort=sort)

    def create(self, user=None, repo=None, org=None):
        request = self.make_request('repos.forks.create', user=user, repo=repo)
        org = {'org': org} if org else {}
        return self._post(request, **org)


class Downloads(Service):

    def list(self, user=None, repo=None):
        request = self.make_request('repos.downloads.list',
            user=user, repo=repo)
        return self._get_result(request)

    def get(self, id, user=None, repo=None):
        request = self.make_request('repos.downloads.get',
            id=id, user=user, repo=repo)
        return self._get(request)

    def create(self, data, user=None, repo=None):
        request = self.make_request('repos.downloads.create',
            body=data, user=user, repo=repo)
        download = self._post(request)

        # TODO: improve it. e.g Manage all with file desc
        def upload(file_path):
            body = download.ball_to_upload()
            body['file'] = (file_path, open(file_path, 'rb'))
            return requests.post(download.s3_url, files=body)

        download.upload = upload
        return download

    def delete(self, id=id, user=None, repo=None):
        request = self.make_request('repos.downloads.delete',
            id=id, user=user, repo=repo)
        self._delete(request)


class Commits(Service, MimeTypeMixin):

    """ TODO: Pagination structure differs from usual
    def list(self, user=None, repo=None, sha='', path=''):
        request = self.make_request('repos.commits.list', user=user, repo=repo)
        return self._get_result(request, sha=sha, path=path)
    """

    def get(self, sha, user=None, repo=None):
        request = self.make_request('repos.commits.get',
            sha=sha, user=user, repo=repo)
        return self._get(request)

    def list_comments(self, sha=None, user=None, repo=None):
        request = self.make_request('repos.commits.list_comments',
            sha=sha, user=user, repo=repo)
        return self._get_result(request, **self._get_mimetype_as_header())

    def create_comment(self, data, sha, user=None, repo=None):
        request = self.make_request('repos.commits.create_comment',
            sha=sha, user=user, repo=repo, body=data)
        return self._post(request, **self._get_mimetype_as_header())

    def get_comment(self, cid, user=None, repo=None):
        request = self.make_request('repos.commits.get_comment',
            comment_id=cid, user=user, repo=repo)
        return self._get(request, **self._get_mimetype_as_header())

    def update_comment(self, data, cid, user=None, repo=None):
        request = self.make_request('repos.commits.update_comment',
            comment_id=cid, user=user, repo=repo, body=data)
        return self._patch(request, **self._get_mimetype_as_header())

    def compare(self, base, head, user=None, repo=None):
        request = self.make_request('repos.commits.compare',
            base=base, head=head, user=user, repo=repo)
        return self._get(request)

    def delete_comment(self, cid, user=None, repo=None):
        request = self.make_request('repos.commits.delete_comment',
            comment_id=cid, user=user, repo=repo)
        self._delete(request)


class Collaborators(Service):

    def list(self, user=None, repo=None):
        request = self.make_request('repos.collaborators.list',
            user=user, repo=repo)
        return self._get_result(request)

    def add(self, collaborator, user=None, repo=None):
        request = self.make_request('repos.collaborators.add',
            collaborator=collaborator, user=user, repo=repo)
        return self._put(request)

    def is_collaborator(self, collaborator, user=None, repo=None):
        request = self.make_request('repos.collaborators.is_collaborator',
            collaborator=collaborator, user=user, repo=repo)
        return self._bool(request)

    def delete(self, collaborator, user=None, repo=None):
        request = self.make_request('repos.collaborators.delete',
            collaborator=collaborator, user=user, repo=repo)
        self._delete(request)


class Repo(Service):
    """ Consume `Repos API <http://developer.github.com/v3/repos>`_ """

    def __init__(self, **config):
        self.collaborators = Collaborators(**config)
        self.commits = Commits(**config)
        self.downloads = Downloads(**config)
        self.forks = Forks(**config)
        self.keys = Keys(**config)
        self.watchers = Watchers(**config)
        super(Repo, self).__init__(**config)

    def list(self, user=None, type='all'):
        """ Get user's repositories

        :param str user: Username
        :param str type: Filter by type (optional). See `github repo doc`_
        :returns: A :doc:`result`

        If you call it without user and you are authenticated, get the
        authenticated user's repositories

        .. warning::

            If you aren't authenticated and call without user, it returns 403

        ::

            repo_service.list('copitux', type='owner')
            repo_service.list(type='private')
        """
        request = self.make_request('repos.list', user=user)
        return self._get_result(request, type=type)

    def list_by_org(self, org, type='all'):
        """ Get organization's repositories

        :param str org: Organization name
        :param str type: Filter by type (optional). See `github repo doc`_
        :returns: A :doc:`result`

        ::

            repo_service.list_by_org('myorganization', type='member')
        """
        request = self.make_request('repos.list_by_org', org=org)
        return self._get_result(request, type=type)

    def create(self, data, in_org=None):
        """ Create a new repository

        :param dict data: Input. See `github repo doc`_
        :param str in_org: Organization where create the repository (optional)

        .. warning::

            You must be authenticated

            If you use ``in_org`` arg, the authenticated user must be a member
            of <in_org>

        ::

            repo_service.create(dict(name='new_repo', description='desc'))
            repo_service.create(dict(name='new_repo_in_org', team_id=2300),
                in_org='myorganization')
        """
        request = self.make_request('repos.create', org=in_org, body=data)
        return self._post(request)

    def get(self, user=None, repo=None):
        """ Get a single repo

        :param str user: Username
        :param str repo: Repository

        .. note::

            Remember :ref:`config precedence`
        """
        request = self.make_request('repos.get', user=user, repo=repo)
        return self._get(request)

    def update(self, data, user=None, repo=None):
        """ Update a single repository

        :param dict data: Input. See `github repo doc`_
        :param str user: Username
        :param str repo: Repository

        .. note::

            Remember :ref:`config precedence`

        .. warning::

            You must be authenticated

        ::

            repo_service.update(dict(has_issues=True), user='octocat',
                repo='oct_repo')
        """
        request = self.make_request('repos.update', body=data,
            user=user, repo=repo)
        return self._patch(request)

    def __list_contributors(self, user=None, repo=None, **kwargs):
        request = self.make_request('repos.list_contributors',
            user=user, repo=repo)
        return self._get_result(request, **kwargs)

    def list_contributors(self, user=None, repo=None):
        """ Get repository's contributors

        :param str user: Username
        :param str repo: Repository
        :returns: A :doc:`result`

        .. note::

            Remember :ref:`config precedence`
        """
        return self.__list_contributors(user, repo)

    def list_contributors_with_anonymous(self, user=None, repo=None):
        """ Like :attr:`~pygithub3.services.repos.Repo.list_contributors` plus
        anonymous """
        return self.__list_contributors(user, repo, anom=True)

    def list_languages(self, user=None, repo=None):
        """ Get repository's languages

        :param str user: Username
        :param str repo: Repository
        :returns: A :doc:`result`

        .. note::

            Remember :ref:`config precedence`
        """
        request = self.make_request('repos.list_languages',
            user=user, repo=repo)
        return self._get(request)

    def list_teams(self, user=None, repo=None):
        """ Get repository's teams

        :param str user: Username
        :param str repo: Repository
        :returns: A :doc:`result`

        .. note::

            Remember :ref:`config precedence`
        """
        request = self.make_request('repos.list_teams', user=user, repo=repo)
        return self._get_result(request)

    def list_tags(self, user=None, repo=None):
        """ Get repository's tags

        :param str user: Username
        :param str repo: Repository
        :returns: A :doc:`result`

        .. note::

            Remember :ref:`config precedence`
        """
        request = self.make_request('repos.list_tags', user=user, repo=repo)
        return self._get_result(request)

    def list_branches(self, user=None, repo=None):
        """ Get repository's branches

        :param str user: Username
        :param str repo: Repository
        :returns: A :doc:`result`

        .. note::

            Remember :ref:`config precedence`
        """
        request = self.make_request('repos.list_branches',
            user=user, repo=repo)
        return self._get_result(request)
