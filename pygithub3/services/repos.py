#!/usr/bin/env python
# -*- encoding: utf-8 -*-

import requests

from .base import Service, MimeTypeMixin


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


class Collaborator(Service):

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

    def __init__(self, **config):
        self.collaborators = Collaborator(**config)
        self.commits = Commits(**config)
        self.downloads = Downloads(**config)
        super(Repo, self).__init__(**config)

    def list(self, user=None, type='all'):
        request = self.make_request('repos.list', user=user)
        return self._get_result(request, type=type)

    def list_by_org(self, org, type='all'):
        request = self.make_request('repos.list_by_org', org=org)
        return self._get_result(request, type=type)

    def create(self, data, in_org=None):
        request = self.make_request('repos.create', org=in_org, body=data)
        return self._post(request)

    def get(self, user=None, repo=None):
        request = self.make_request('repos.get', user=user, repo=repo)
        return self._get(request)

    def update(self, data, user=None, repo=None):
        request = self.make_request('repos.update', body=data,
            user=user, repo=repo)
        return self._patch(request)

    def __list_contributors(self, user=None, repo=None, **kwargs):
        request = self.make_request('repos.list_contributors',
            user=user, repo=repo)
        return self._get_result(request, **kwargs)

    def list_contributors(self, user=None, repo=None):
        return self.__list_contributors(user, repo)

    def list_contributors_with_anonymous(self, user=None, repo=None):
        return self.__list_contributors(user, repo, anom=True)

    def list_languages(self, user=None, repo=None):
        request = self.make_request('repos.list_languages',
            user=user, repo=repo)
        return self._get(request)

    def list_teams(self, user=None, repo=None):
        request = self.make_request('repos.list_teams', user=user, repo=repo)
        return self._get_result(request)

    def list_tags(self, user=None, repo=None):
        request = self.make_request('repos.list_tags', user=user, repo=repo)
        return self._get_result(request)

    def list_branches(self, user=None, repo=None):
        request = self.make_request('repos.list_branches',
            user=user, repo=repo)
        return self._get_result(request)
