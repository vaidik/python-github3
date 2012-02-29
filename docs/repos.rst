.. _Repos service:

Repos's services
===================

**Fast sample**::

    from pygithub3 import Github

    gh = Github()

    django_compressor = gh.repos.get(user='jezdez', repo='django_compressor')
    requests_collaborators = gh.repos.collaborators(user='kennethreitz',
        repo='requests')

.. _config precedence:

Config precedence
------------------

Some request always need ``user`` and ``repo`` parameters, both, to identify
a `repository`. Because there are a lot of requests which need that parameters,
you can :ref:`config each service` with ``user`` and ``repo`` globally.

So several requests follow a simple precedence ``user_in_arg > user_in_config``

You can see it better with an example: ::

    from pygithub3 import Github

    gh = Github(user='octocat', repo='oct_repo')
    oct_repo = gh.repos.get()
    another_repo_from_octocat = gh.repos.get(repo='another_repo')

    django_compressor = gh.repos.get(user='jezdez', repo='django_compressor')

.. note::

    Remember that each service is isolated from the rest ::

        # continue example...
        gh.repos.commits.set_user('copitux')
        oct_repo = gh.repos.get()
        oct_repo_collaborators = gh.repos.collaborators.list().all()

        # Fail because copitux/oct_repo doesn't exist
        gh.repos.commits.list_comments()

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

.. _github repo doc: http://developer.github.com/v3/repos
