
Result
=======

Some requests returns multiple :doc:`resources`, for that reason the
``Github API`` paginate it and **pygithub3** too

.. autoclass:: pygithub3.core.result.Result

You have several ways to consume it

1. Iterating over the result::

    result = some_request()
    for page in result:
        for resource in page:
            print resource

2. With a generator::

    result = some_request()
    for resource in result.iterator():
        print resource

3. As a list::

    result = some_request()
    print result.all()

4. Also you can request some page manually

.. autoattribute:: pygithub3.core.result.Result.pages
.. automethod:: pygithub3.core.result.Result.get_page

Each ``Page`` is an iterator and contains resources


