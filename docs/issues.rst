.. _Issues service:

Issues services
===============

**Fast sample**::

    from pygithub3 import Github

    auth = dict(login='octocat', password='pass')
    gh = Github(**auth)

    octocat_issues = gh.issues.list()
    octocat_repo_issues = gh.issues.list_by_repo('octocat', 'Hello-World')

Issues
-----

.. autoclass:: pygithub3.services.issues.Issue
    :members:

    .. attribute:: comments

        :ref:`Comments service`

    .. attribute:: events

        :ref:`Events service`

.. _Comments service:

Comments
----------

.. autoclass:: pygithub3.services.issues.Comments
    :members:

.. _ Events service:

Events
-------

.. autoclass:: pygithub3.services.issues.Comments
    :members:

.. _github issues doc: http://developer.github.com/v3/issues
.. _github comments doc: http://developer.github.com/v3/issues/comments