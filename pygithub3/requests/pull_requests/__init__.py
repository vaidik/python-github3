from pygithub3.requests.base import Request, ValidationError
from pygithub3.resources.base import Raw
from pygithub3.resources.pull_requests import PullRequest, File
from pygithub3.resources.repos import Commit


class List(Request):
    uri = 'repos/{user}/{repo}/pulls'
    resource = PullRequest


class Get(Request):
    uri = 'repos/{user}/{repo}/pulls/{number}'
    resource = PullRequest


class Create(Request):
    uri = 'repos/{user}/{repo}/pulls'
    resource = PullRequest
    body_schema = {
        'schema': ('title', 'body', 'base', 'head', 'issue'),
        'required': ('base', 'head'),
    }

    def validate_body(self, parsed):
        if (not ('title' in parsed and 'body' in parsed) and
            not 'issue' in parsed):
            raise ValidationError('pull request creation requires either an '
                                  'issue number or a title and body')

class Update(Request):
    uri = 'repos/{user}/{repo}/pulls/{number}'
    resource = PullRequest
    body_schema = {
        'schema': ('title', 'body', 'state'),
        'required': (),
    }

    def validate_body(self, body):
        if 'state' in body and body['state'] not in ['open', 'closed']:
            raise ValidationError('If a state is specified, it must be one '
                                  'of "open" or "closed"')


class List_commits(Request):
    uri = 'repos/{user}/{repo}/pulls/{number}/commits'
    resource = Commit


class List_files(Request):
    uri = 'repos/{user}/{repo}/pulls/{number}/files'
    resource = File


class Merge_status(Request):
    uri = 'repos/{user}/{repo}/pulls/{number}/merge'
    resource = Raw


class Merge(Request):
    uri = 'repos/{user}/{repo}/pulls/{number}/merge'
    resource = Raw
