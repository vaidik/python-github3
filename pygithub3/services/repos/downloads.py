#!/usr/bin/env python
# -*- encoding: utf-8 -*-

import requests

from . import Service


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
