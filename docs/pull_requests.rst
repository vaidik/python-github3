.. _Pull Requests service:

Pull Requests service
=====================

**Example**::

    from pygithub3 import Github

    gh = Github()

    pull_requests = gh.pull_requests.list().all()
    for pr in pull_requests:
        commits = gh.pull_requests.list_commits(pr.number).all()

Pull Requests
-------------

.. autoclass:: pygithub3.services.pull_requests.PullRequests
    :members:

    .. attribute:: comments

        :ref:`Pull Request Comments service`


.. _Pull Request Comments service:

Pull Request Comments
---------------------

.. autoclass:: pygithub3.services.pull_requests.Comments
    :members:
