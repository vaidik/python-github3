Fork
====
Refactor and complete api wrapper. Intensive work in progress

Use with auth user
------------------

    from github3.api import Github

    gh = Github('user', 'password')

    users_handler = gh.users
    for repo in users_handler.get_repos():
        print repo

    gists_handler = gh.gists
    gists_handler.create_gist(
        u'Description',
        files={'file1.txt': {'content': u'Content of first file'}})

Installation
------------

To install Github3, simply:

    $ pip -e git+https://copitux@github.com/copitux/python-github3#egg=python-github3

License
-------

ISC License.

    Copyright (c) 2011, Kenneth Reitz <me@kennethreitz.com>

    Permission to use, copy, modify, and/or distribute this software for any
    purpose with or without fee is hereby granted, provided that the above
    copyright notice and this permission notice appear in all copies.

    THE SOFTWARE IS PROVIDED "AS IS" AND THE AUTHOR DISCLAIMS ALL WARRANTIES
    WITH REGARD TO THIS SOFTWARE INCLUDING ALL IMPLIED WARRANTIES OF
    MERCHANTABILITY AND FITNESS. IN NO EVENT SHALL THE AUTHOR BE LIABLE FOR
    ANY SPECIAL, DIRECT, INDIRECT, OR CONSEQUENTIAL DAMAGES OR ANY DAMAGES
    WHATSOEVER RESULTING FROM LOSS OF USE, DATA OR PROFITS, WHETHER IN AN
    ACTION OF CONTRACT, NEGLIGENCE OR OTHER TORTIOUS ACTION, ARISING OUT OF
    OR IN CONNECTION WITH THE USE OR PERFORMANCE OF THIS SOFTWARE.


Contribute
----------

If you'd like to contribute, simply fork `the repository`, commit your changes
to the **develop** branch (or branch off of it), and send a pull request. Make
sure you add yourself to `AUTHORS`.


Roadmap
-------

- Unittests
- Handlers
- Sphinx Documentation
- Examples
- OAuth Last (how?)
