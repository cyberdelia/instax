Instax
======

Making celery monitoring easier, using statsd.

Usage
-----

You first need to configure the ``statsd`` client like explained in the docs :
http://statsd.readthedocs.org/en/latest/configure.html#from-the-environment

Launch your celery worker with the ``--events`` argument ::

    celery worker --events

Then run ``instax`` with the following arguments ::

    celery events -c instax.Instax --frequency=10.0

