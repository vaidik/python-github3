#!/usr/bin/env python
# -*- encoding: utf-8 -*-
#
# author: Antti Kaihola

from datetime import datetime
import json
from mock import MagicMock, Mock, patch
import unittest

import github3.api
import github3.handlers.gists
import github3.handlers.user
import github3.models


GIST_RESPONSE = '{"user":{"gravatar_id":"123","url":"https://api.github.com/users/testuser","avatar_url":"https://secure.gravatar.com/avatar/123?d=https://a248.e.akamai.net/assets.github.com%2Fimages%2Fgravatars%2Fgravatar-1.png","login":"testuser","id":12345},"url":"https://api.github.com/gists/791920","history":[{"version":"deadbeefdeadbeefdeadbeefdeadbeefdeadbeef","url":"https://api.github.com/gists/791920/deadbeefdeadbeefdeadbeefdeadbeefdeadbeef","user":{"gravatar_id":"123","url":"https://api.github.com/users/testuser","avatar_url":"https://secure.gravatar.com/avatar/123?d=https://a248.e.akamai.net/assets.github.com%2Fimages%2Fgravatars%2Fgravatar-1.png","login":"testuser","id":12345},"committed_at":"2011-11-09T08:50:53Z","change_status":{"deletions":0,"additions":1,"total":1}}],"description":"description","created_at":"2011-11-09T08:50:53Z","public":true,"comments":0,"updated_at":"2011-11-09T08:50:53Z","git_pull_url":"git://gist.github.com/791920.git","forks":[],"git_push_url":"git@gist.github.com:791920.git","html_url":"https://gist.github.com/791920","id":"791920","files":{"filename.ext":{"raw_url":"https://gist.github.com/raw/791920/badafadacadafadabadacadafadabadabadacada/filename.ext","type":"text/plain","content":"content","size":7,"language":null,"filename":"filename.ext"}}}'


class GistsTestCase(unittest.TestCase):
    def test_create_gist(self):
        """The HTTP request for creating a gist is correct"""
        g = github3.api.Github()
        g.session.auth = ('testuser', 'password')
        u = github3.handlers.user.AuthUser(g)
        gists = github3.handlers.gists.AuthGist(g)
        OpenerDirector = MagicMock(name='OpenerDirector')
        opener = OpenerDirector.return_value
        response = opener.open.return_value
        response.read.return_value = GIST_RESPONSE
        response.code = 201
        
        with patch('urllib2.OpenerDirector', OpenerDirector):

            gist = gists.create_gist(
                'description',
                files={'filename.ext': {'content': 'content'}})

        request = opener.open.call_args[0][0]
        self.assertEqual(request.method, 'POST')
        self.assertEqual(request.get_full_url(),
                         'https://api.github.com/gists?per_page=100')
        self.assertEqual(request.headers['Authorization'],
                         'Basic dGVzdHVzZXI6cGFzc3dvcmQ=')
        self.assertEqual(json.loads(request.data),
                         {u'description': u'description',
                          u'files': {u'filename.ext': {u'content': u'content'}},
                          u'public': True})


class GistHandlerTestCase(unittest.TestCase):
    def test_response_conversion(self):
        """A gist response is decoded correctly to a Gist object"""
        g = github3.api.Github()
        handler = github3.handlers.gists.Gist(g)
        converter = handler._get_converter()
        converter.inject(github3.models.Gist)

        gist = converter.loads(json.loads(GIST_RESPONSE))

        self.assertEqual(
            {filename: value.__dict__
             for filename, value in gist.files.iteritems()},
            {u'filename.ext': {
                'content': u'content',
                'filename': u'filename.ext',
                'raw_url': (u'https://gist.github.com/'
                            u'raw/791920/'
                            u'badafadacadafadabadacadafadabadabadacada/'
                            u'filename.ext'),
                'size': 7,
                'type': u'text/plain'}})
        self.assertEqual(gist.description, u'description')
        self.assertEqual(gist.url, u'https://api.github.com/gists/791920')
        self.assertEqual(gist.created_at, datetime(2011, 11, 9, 8, 50, 53))
        self.assertEqual(gist.html_url, u'https://gist.github.com/791920')
        self.assertEqual(gist.public, True)
        self.assertEqual(
            gist.user.__dict__,
            {'avatar_url': (u'https://secure.gravatar.com/avatar/123'
                            u'?d=https://a248.e.akamai.net/'
                            u'assets.github.com%2Fimages%2Fgravatars'
                            u'%2Fgravatar-1.png'),
             'id': 12345,
             'login': u'testuser',
             'url': u'https://api.github.com/users/testuser'})
        self.assertEqual(gist.git_pull_url, u'git://gist.github.com/791920.git')
        self.assertEqual(gist.git_push_url, u'git@gist.github.com:791920.git')
        self.assertEqual(gist.id, u'791920')
        self.assertEqual(len(gist.history), 1)
        h = gist.history[0]
        self.assertEqual(h.change_status.__dict__, {'additions': 1, 'total': 1})
        self.assertEqual(h.committed_at, datetime(2011, 11, 9, 8, 50, 53))
        self.assertEqual(h.url,
                         u'https://api.github.com/gists/791920/'
                         u'deadbeefdeadbeefdeadbeefdeadbeefdeadbeef')
        self.assertEqual(h.user.__dict__, gist.user.__dict__)
        self.assertEqual(h.version, u'deadbeefdeadbeefdeadbeefdeadbeefdeadbeef')
