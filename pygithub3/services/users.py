#!/usr/bin/env python
# -*- encoding: utf-8 -*-

from .base import Service


class Keys(Service):
    """ Consume `Keys API <http://developer.github.com/v3/users/keys/>`_

    .. warning::

        You must be authenticated for all requests
    """

    def list(self):
        """ Get public keys

        :returns: A :doc:`result`
        """
        request = self.make_request('users.keys.list')
        return self._get_result(request)

    def get(self, key_id):
        """ Get a public key

        :param int key_id: Key id
        """
        request = self.make_request('users.keys.get',
            key_id=key_id)
        return self._get(request)

    def add(self, data):
        """ Add a public key

        :param dict data: Key (title and key attributes required)

        ::

            key_service.add(dict(title='host', key='ssh-rsa AAA...'))
        """
        request = self.make_request('users.keys.add',
            body=data)
        return self._post(request)

    def update(self, key_id, data):
        """ Update a public key

        :param int key_id: Key id
        :param dict data: Key (title and key attributes required)

        ::

            key_service.update(42, dict(title='host', key='ssh-rsa AAA...'))
        """
        request = self.make_request('users.keys.update',
            key_id=key_id, body=data)
        return self._patch(request)

    def delete(self, key_id):
        """ Delete a public key

        :param int key_id: Key id
        """
        request = self.make_request('users.keys.delete',
            key_id=key_id)
        self._delete(request)


class Followers(Service):
    """ Consume `Followers API
    <http://developer.github.com/v3/users/followers/>`_
    """

    def list(self, user=None):
        """ Get user's followers

        :param str user: Username
        :returns: A :doc:`result`

        If you call it without user and you are authenticated, get the
        authenticated user's followers

        .. warning::

            If you aren't authenticated and call without user, it returns 403

        ::

            followers_service.list()
            followers_service.list('octocat')
        """
        request = self.make_request('users.followers.list', user=user)
        return self._get_result(request)

    def list_following(self, user=None):
        """ Get who a user is following

        :param str user: Username
        :returns: A :doc:`result`

        If you call it without user and you are authenticated, get the
        authenticated user's followings

        .. warning::

            If you aren't authenticated and call without user, it returns 403

        ::

            followers_service.list_following()
            followers_service.list_following('octocat')
        """
        request = self.make_request('users.followers.listfollowing', user=user)
        return self._get_result(request)

    def is_following(self, user):
        """ Check if you are following a user

        :param str user: Username
        """
        request = self.make_request('users.followers.isfollowing', user=user)
        return self._bool(request)

    def follow(self, user):
        """ Follow a user

        :param str user: Username

        .. warning::

            You must be authenticated
        """
        request = self.make_request('users.followers.follow', user=user)
        self._put(request)

    def unfollow(self, user):
        """ Unfollow a user

        :param str user: Username

        .. warning::

            You must be authenticated
        """
        request = self.make_request('users.followers.unfollow', user=user)
        self._delete(request)


class Emails(Service):
    """ Consume `Emails API <http://developer.github.com/v3/users/emails/>`_

    .. warning::

        You must be authenticated for all requests
    """

    def list(self):
        """ Get user's emails

        :returns: A :doc:`result`
        """
        request = self.make_request('users.emails.list')
        return self._get_result(request)

    def add(self, *emails):
        """ Add emails

        :param list emails: Emails to add

        .. note::

            It rejects non-valid emails

        ::

            email_service.add('test1@xample.com', 'test2@xample.com')
        """
        request = self.make_request('users.emails.add', body=emails)
        return self._post(request)

    def delete(self, *emails):
        """ Delete emails

        :param list emails: List of emails

        ::

            email_service.delete('test1@xample.com', 'test2@xample.com')
        """
        request = self.make_request('users.emails.delete', body=emails)
        self._delete(request)


class User(Service):
    """ Consume `Users API <http://developer.github.com/v3/users>`_ """

    def __init__(self, **config):
        self.keys = Keys(**config)
        self.emails = Emails(**config)
        self.followers = Followers(**config)
        super(User, self).__init__(**config)

    def get(self, user=None):
        """ Get a single user

        :param str user: Username

        If you call it without user and you are authenticated, get the
        authenticated user.

        .. warning::

            If you aren't authenticated and call without user, it returns 403

        ::

            user_service.get('copitux')
            user_service.get()
        """
        request = self.make_request('users.get', user=user)
        return self._get(request)

    def update(self, data):
        """ Update the authenticated user

        :param dict data: Input to update

        ::

            user_service.update(dict(name='new_name', bio='new_bio'))
        """
        request = self.make_request('users.update', body=data)
        return self._patch(request)
