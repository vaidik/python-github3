"""
github3.models
~~~~~~~~~~~~~~

This module provides the Github3 object model.
"""

import json
import inspect

from github3.helpers import to_python, to_api, key_diff

class BaseResource(object):
    """A BaseResource object."""

    _strs = []
    _ints = []
    _dates = []
    _bools = []
    _map = {}
    _list_map = {}
    _writeable = []
    _cache = {}

    def post_map(self):
        try:
            handler = self.handler()
            methods = filter(
                lambda x: x[0].startswith('get') and callable(x[1]),
                inspect.getmembers(handler, inspect.ismethod))
            for name, callback in methods:
                setattr(self, name, callback)
        except:
            pass

    def __init__(self):
        self._bootstrap()
        super(BaseResource, self).__init__()

    def __dir__(self):
        return self.keys()

    def _bootstrap(self):
        """Bootstraps the model object based on configured values."""

        for attr in self.keys():
            setattr(self, attr, None)

    def keys(self):
        return self._strs + self._ints + self._dates + self._bools + self._map.keys()

    def dict(self):
        d = dict()
        for k in self.keys():
            d[k] = self.__dict__.get(k)

        return d

    @classmethod
    def new_from_dict(cls, d, gh=None):

        return to_python(
            obj=cls(), in_dict=d,
            str_keys = cls._strs,
            int_keys = cls._ints,
            date_keys = cls._dates,
            bool_keys = cls._bools,
            object_map = cls._map,
            list_map = cls._list_map,
            _gh = gh
        )


    def update(self):
        deploy = key_diff(self._cache, self.dict(), pack=True)

        deploy = to_api(deploy, int_keys=self._ints, date_keys=self._dates, bool_keys=self._bools)
        deploy = json.dumps(deploy)

        r = self._gh._patch_resource(self.ri, deploy)
        return r



#class Org(BaseResource):
#    """Github Organization object model."""
#
#    _strs = [
#        'login', 'url', 'avatar_url', 'name', 'company', 'blog', 'location', 'email'
#        'html_url', 'type', 'billing_email']
#    _ints = [
#        'id', 'public_repos', 'public_gists', 'followers', 'following',
#        'total_private_repos', 'owned_private_repos', 'private_gists', 'disk_usage',
#        'collaborators']
#    _dates = ['created_at']
#    _map = {'plan': Plan}
#    _writable = ['billing_email', 'blog', 'company', 'email', 'location', 'name']
#
#    @property
#    def ri(self):
#        return ('orgs', self.login)
#
#    def __repr__(self):
#        return '<org {0}>'.format(self.login)
#
#    def repos(self, limit=None):
#         return self._gh._get_resources(('orgs', self.login, 'repos'), Repo, limit=limit)
#
#    def members(self, limit=None):
#        return self._gh._get_resources(('orgs', self.login, 'members'), User, limit=limit)
#
#    def is_member(self, username):
#        if isinstance(username, User):
#            username = username.login
#
#        r = self._gh._http_resource('GET', ('orgs', self.login, 'members', username), check_status=False)
#        return (r.status_code == 204)
#
#    def publicize_member(self, username):
#        if isinstance(username, User):
#            username = username.login
#
#        r = self._gh._http_resource('PUT', ('orgs', self.login, 'public_members', username), check_status=False, data='')
#        return (r.status_code == 204)
#
#    def conceal_member(self, username):
#        if isinstance(username, User):
#            username = username.login
#
#        r = self._gh._http_resource('DELETE', ('orgs', self.login, 'public_members', username), check_status=False)
#        return (r.status_code == 204)
#
#    def remove_member(self, username):
#        if isinstance(username, User):
#            username = username.login
#
#        r = self._gh._http_resource('DELETE', ('orgs', self.login, 'members', username), check_status=False)
#        return (r.status_code == 204)
#
#    def public_members(self, limit=None):
#        return self._gh._get_resources(('orgs', self.login, 'public_members'), User, limit=limit)
#
#    def is_public_member(self, username):
#        if isinstance(username, User):
#            username = username.login
#
#        r = self._gh._http_resource('GET', ('orgs', self.login, 'public_members', username), check_status=False)
#        return (r.status_code == 204)
#
#
