from pygithub3.requests.base import Request
from pygithub3.resources.git_data import Tree


class Get(Request):
    uri = 'repos/{user}/{repo}/git/trees/{sha}'
    resource = Tree

    def clean_uri(self):
        if self.recursive:
            return self.uri + '?recursive=1'


class Create(Request):
    uri = 'repos/{user}/{repo}/git/trees'
    resource = Tree
    body_schema = {
        'schema': ('tree',),
        'required': ('tree',),
    }
