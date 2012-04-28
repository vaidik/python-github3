# -*- encoding: utf-8 -*-

from pygithub3.resources.orgs import Member
from . import Request


class List(Request):
    uri = 'orgs/{org}/members'
    resource = Member


class Get(Request):
    uri = 'orgs/{org}/members/{user}'


class Delete(Request):
    uri = 'orgs/{org}/members/{user}'


class Listpublic(Request):
    uri = 'orgs/{org}/public_members'
    resource = Member


class Getpublic(Request):
    uri = 'orgs/{org}/public_members/{user}'


class Publicize(Request):
    uri = 'orgs/{org}/public_members/{user}'


class Conceal(Request):
    uri = 'orgs/{org}/public_members/{user}'
