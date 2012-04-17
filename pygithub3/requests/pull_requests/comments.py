from pygithub3.requests.base import Request
from pygithub3.resources.pull_requests import Comment


class List(Request):
    uri = 'repos/{user}/{repo}/pulls/{number}/comments'
    resource = Comment


class Get(Request):
    uri = 'repos/{user}/{repo}/pulls/comments/{number}'
    resource = Comment


class Create(Request):
    uri = 'repos/{user}/{repo}/pulls/{number}/comments'
    resource = Comment
    body_schema = {
        'schema': ('body', 'commit_id', 'path', 'position', 'in_reply_to'),
        'required': ('body',),
    }

    def validate_body(self, body):
        if (not ('commit_id' in body and
                 'path' in body and
                 'position' in body) and
            not 'in_reply_to' in body):
            raise ValidationError('supply either in_reply_to or commit_id, '
                                  'path, and position')


class Edit(Request):
    uri = 'repos/{user}/{repo}/pulls/comments/{number}'
    resource = Comment
    body_schema = {
        'schema': ('body',),
        'required': ('body',),
    }


class Delete(Request):
    uri = 'repos/{user}/{repo}/pulls/comments/{number}'
    resource = Comment
