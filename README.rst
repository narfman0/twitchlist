twitchlist
==============

.. image:: https://badge.fury.io/py/twitchlist.png
    :target: https://badge.fury.io/py/twitchlist

.. image:: https://travis-ci.org/narfman0/twitchlist.png?branch=master
    :target: https://travis-ci.org/narfman0/twitchlist

Peep your followed twitch streams for activity

Installation
------------

Install via pip::

    pip install twitchlist

Usage
-----

Define the following in a run.sh or similar, and invoke::

    OAUTH_AUTHORIZATION="OAuth 1234567890asdfghjkqwertyuvdcsb" \
    CLIENT_ID="alksdoasind9n8feinfaksndakksad" \
    PERSISTED_QUERY_HASH="12312312312312312312312312312312312312babacbcbaccabcabacbcabbacb" \
        python main.py

Development
-----------

Run test suite to ensure everything works::

    make test

Release
-------

To publish your plugin to pypi, sdist and wheels are registered, created and uploaded with::

    make release-test

For test. After ensuring the package works, run the prod target and win::

    make release-prod

License
-------

Copyright (c) 2021 Jon Robison

See LICENSE for details
