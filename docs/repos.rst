.. _Repos service:

Repos's services
===================

**Fast sample**::

    from pygithub3 import Github

    auth = dict(login='octocat', password='pass')
    gh = Github(**auth)

    # Get copitux user
    gh.users.get('copitux')

    # Get copitux's followers
    gh.users.followers.list('copitux')

    # Get octocat's emails
    gh.users.emails.list()

Repo
-------

.. autoclass:: pygithub3.services.repos.Repo
    :members:

    .. attribute:: collaborators

        :ref:`Collaborators service`

    .. attribute:: commits

        :ref:`Commits service`

    .. attribute:: downloads

        :ref:`Downloads service`

    .. attribute:: forks

        :ref:`Forks service`

    .. attribute:: keys

        :ref:`RepoKeys service`

    .. attribute:: watchers

        :ref:`Watchers service`

.. _Collaborators service:

Collaborators
--------------


.. _Commits service:

Commits
----------

.. _Downloads service:

Downloads
------------


.. _Forks service:

Forks
---------


.. _RepoKeys service:

Keys
----------


.. _Watchers service:

Watchers
---------
