# -*- encoding: utf-8 -*-

from pygithub3.services.base import Service


class Org(Service):
    """ Consume `Orgs API <http://developer.github.com/v3/orgs>`_ """

    def list(self, user=None):
        """ Get user's orgs

        :param str user: Username
        :returns: A :doc:`result`

        If you call it without user and you are authenticated, get the
        authenticated user's orgs, public and private.

        If you call it with a user, get the user's public orgs.

        ::

            org_service.list('copitux')
            org_service.list()
        """
        request = self.request_builder('orgs.list', user=user)
        return self._get_result(request)

    def get(self, name):
        """ Get a single org

        :param str name: Org name
        """
        request = self.request_builder('orgs.get', name=name)
        return self._get(request)

    def update(self, name, data):
        """ Update a single org

        :param str name: Org name
        :param dict data: Input. See `github orgs doc`_

        .. warning ::
            You must be authenticated

        ::

            org_service.update(dict(company='ACME Development',
                                    location='Timbuctoo'))
        """
        request = self.request_builder('orgs.update', name=name, body=data)
        return self._patch(request)
