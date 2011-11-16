#!/usr/bin/env python
# -*- encoding: utf-8 -*-

GET_USER = {
    "login": "octocat",
    "id": 1,
    "avatar_url": "https://github.com/images/error/octocat_happy.gif",
    "gravatar_id": "somehexcode",
    "url": "https://api.github.com/users/octocat",
    "name": "monalisa octocat",
    "company": "GitHub",
    "blog": "https://github.com/blog",
    "location": "San Francisco",
    "email": "octocat@github.com",
    "hireable": False,
    "bio": "There once was...",
    "public_repos": 2,
    "public_gists": 1,
    "followers": 20,
    "following": 0,
    "html_url": "https://github.com/octocat",
    "created_at": "2008-01-14T04:33:35Z",
    "type": "User"
}

GET_LINK = '<https://api.github.com/gists/public?page=2>; rel="next", \
<https://api.github.com/gists/public?page=5>; rel="last"'

GET_RESOURCES = [
    {'login': 'octocat'},
    {'login': 'octocat'}
]

GET_SHORT_USERS = [
    {
        "login": "octocat",
        "id": 1,
        "avatar_url": "https://github.com/images/error/octocat_happy.gif",
        "gravatar_id": "somehexcode",
        "url": "https://api.github.com/users/octocat"
    },
    {
        "login": "octocat",
        "id": 1,
        "avatar_url": "https://github.com/images/error/octocat_happy.gif",
        "gravatar_id": "somehexcode",
        "url": "https://api.github.com/users/octocat"
    },
]

GET_SHORT_ORGS = [
    {
        "login": "github",
        "id": 1,
        "url": "https://api.github.com/orgs/1",
        "avatar_url": "https://github.com/images/error/octocat_happy.gif"
    }
]

GET_SHORT_REPOS = [
    {
        "url": "https://api.github.com/repos/octocat/Hello-World",
        "html_url": "https://github.com/octocat/Hello-World",
        "clone_url": "https://github.com/octocat/Hello-World.git",
        "git_url": "git://github.com/octocat/Hello-World.git",
        "ssh_url": "git@github.com:octocat/Hello-World.git",
        "svn_url": "https://svn.github.com/octocat/Hello-World",
        "owner": {
            "login": "octocat",
            "id": 1,
            "avatar_url": "https://github.com/images/error/octocat_happy.gif",
            "gravatar_id": "somehexcode",
            "url": "https://api.github.com/users/octocat"
        },
        "name": "Hello-World",
        "description": "This your first repo!",
        "homepage": "https://github.com",
        "language": None,
        "private": False,
        "fork": False,
        "forks": 9,
        "watchers": 80,
        "size": 108,
        "master_branch": "master",
        "open_issues": 0,
        "pushed_at": "2011-01-26T19:06:43Z",
        "created_at": "2011-01-26T19:01:12Z"
    }
]

GET_SHORT_GISTS = [
    {
        "url": "https://api.github.com/gists/1",
        "id": "1",
        "description": "description of gist",
        "public": True,
        "user": {
            "login": "octocat",
            "id": 1,
            "avatar_url": "https://github.com/images/error/octocat_happy.gif",
            "gravatar_id": "somehexcode",
            "url": "https://api.github.com/users/octocat"
        },
        "files": {
            "ring.erl": {
                "size": 932,
                "filename": "ring.erl",
                "raw_url": "https://gist.github.com/raw/365370/8c4d2d43d178df\
                    44f4c03a7f2ac0ff512853564e/ring.erl",
                "content": "contents of gist"
            }
        },
        "comments": 0,
        "html_url": "https://gist.github.com/1",
        "git_pull_url": "git://gist.github.com/1.git",
        "git_push_url": "git@gist.github.com:1.git",
        "created_at": "2010-04-14T02:15:15Z"
    }
]
GET_FULL_USER = {
    "login": "octocat",
    "id": 1,
    "avatar_url": "https://github.com/images/error/octocat_happy.gif",
    "gravatar_id": "somehexcode",
    "url": "https://api.github.com/users/octocat",
    "name": "monalisa octocat",
    "company": "GitHub",
    "blog": "https://github.com/blog",
    "location": "San Francisco",
    "email": "octocat@github.com",
    "hireable": False,
    "bio": "There once was...",
    "public_repos": 2,
    "public_gists": 1,
    "followers": 20,
    "following": 0,
    "html_url": "https://github.com/octocat",
    "created_at": "2008-01-14T04:33:35Z",
    "type": "User",
    "total_private_repos": 100,
    "owned_private_repos": 100,
    "private_gists": 81,
    "disk_usage": 10000,
    "collaborators": 8,
    "plan": {
        "name": "Medium",
        "space": 400,
        "collaborators": 10,
        "private_repos": 20
    }
}
GET_USER_EMAILS = [
  "octocat@github.com",
  "support@github.com"
]
