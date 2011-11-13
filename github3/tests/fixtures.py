#!/usr/bin/env python
# -*- encoding: utf-8 -*-

GET_USER = {
    "login": "octocat",
    "id": 1,
    "avatar_url": "https://github.com/images/error/octocat_happy.gif",
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

GET_LINK = '<https://api.github.com/gists/public?page=2>; rel="next", <https://api.github.com/gists/public?page=5>; rel="last"'
GET_RESOURCES = [
    {'login': 'octocat'},
    {'login': 'octocat'}
]
GET_FOLLOWERS = [
    {
        "login": "octocat",
        "id": 1,
        "avatar_url": "https://github.com/images/error/octocat_happy.gif",
        "url": "https://api.github.com/users/octocat"
    },
    {
        "login": "octocat",
        "id": 1,
        "avatar_url": "https://github.com/images/error/octocat_happy.gif",
        "url": "https://api.github.com/users/octocat"
    },
]
