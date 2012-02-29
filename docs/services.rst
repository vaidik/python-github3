Services
==========

:doc:`github` class is a glue to all of them and the recommended option to
start

Overview
..........

You can access to the API requests through the different services.

If you take a look at
`github API v3 documentation <http://developer.github.com/>`_, you'll see a
few sections in the sidebar.

**pygithub3** has one service per each section of request-related

For example: ::

    repos => services.repos.repo
        collaborators => services.repos.collaborators
        commits => services.repos.commits
        ....

Each service has the functions to throw the API requests and is isolated
from the rest.

Config each service
.....................................

Each service can be configurated with some variables (behind the scenes, each
service has her client which is configurated with this variables).

.. note::

    Also you can configure :doc:`github` as a service

.. autoclass:: pygithub3.services.base.Service
    :members:

List of services
..................

.. toctree::
    :maxdepth: 2

    users
    repos
