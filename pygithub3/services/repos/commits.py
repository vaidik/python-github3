#!/usr/bin/env python
# -*- encoding: utf-8 -*-

from . import Service, MimeTypeMixin


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
