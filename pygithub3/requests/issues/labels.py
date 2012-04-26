# -*- encoding: utf-8 -*-

from pygithub3.requests.base import Request, ValidationError
from pygithub3.resources.issues import Label



class Get(Request):
    uri = 'repos/{user}/{repo}/labels/{name}'
    resource = Label


class Create(Request):
    uri = 'repos/{user}/{repo}/labels'
    resource = Label
    body_schema = {
        'schema': ('name', 'color'),
        'required': ('name', 'color' )
    }

    def validate_color(color):
        color = color.get('color', '')
        if not Label.is_valid_color(color):
            raise ValidationError('colors must have 6 hexadecimal characters, '
                                  'without # in the beggining')


class Update(Request):

    uri = 'repos/{user}/{repo}/labels/{name}'
    resource = Label
    body_schema = {
        'schema': ('name', 'color'),
        'required': ('name', 'color' )
    }

    def validate_color(color):
        color = color.get('color', '')
        if not Label.is_valid_color(color):
            raise ValidationError('colors must have 6 hexadecimal characters, '
                                  'without # in the beggining')


class Delete(Request):
    uri = 'repos/{user}/{repo}/labels/{name}'
    resource = Label


class List_by_repo(Request):
    uri = 'repos/{user}/{repo}/labels'
    resource = Label



class List_by_issue(Request):
    uri = 'repos/{user}/{repo}/issues/{number}/labels'
    resource = Label


class Add_to_issue(Request):
    uri = 'repos/{user}/{repo}/issues/{number}/labels'
    resource = Label

class Remove_from_issue(Request):
    uri = 'repos/{user}/{repo}/issues/{number}/labels/{name}'
    resource = Label


class Replace_all(Request):
    uri = 'repos/{user}/{repo}/issues/{number}/labels'
    resource = Label


class Remove_all(Request):
    uri = 'repos/{user}/{repo}/issues/{number}/labels'
    resource = Label


class List_by_milestone(Request):
    uri = 'repos/{user}/{repo}/milestones/{number}/labels'
    resource = Label
