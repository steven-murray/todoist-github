========
Overview
========

.. start-badges

.. list-table::
    :stub-columns: 1

    * - docs
      - |docs|
    * - tests
      - | |travis| |requires|
        | |coveralls| |codecov|
    * - package
      - | |version| |wheel| |supported-versions| |supported-implementations|
        | |commits-since|
.. |docs| image:: https://readthedocs.org/projects/todoist-github/badge/?style=flat
    :target: https://readthedocs.org/projects/todoist-github
    :alt: Documentation Status

.. |travis| image:: https://travis-ci.org/steven-murray/todoist-github.svg?branch=master
    :alt: Travis-CI Build Status
    :target: https://travis-ci.org/steven-murray/todoist-github

.. |requires| image:: https://requires.io/github/steven-murray/todoist-github/requirements.svg?branch=master
    :alt: Requirements Status
    :target: https://requires.io/github/steven-murray/todoist-github/requirements/?branch=master

.. |coveralls| image:: https://coveralls.io/repos/steven-murray/todoist-github/badge.svg?branch=master&service=github
    :alt: Coverage Status
    :target: https://coveralls.io/r/steven-murray/todoist-github

.. |codecov| image:: https://codecov.io/github/steven-murray/todoist-github/coverage.svg?branch=master
    :alt: Coverage Status
    :target: https://codecov.io/github/steven-murray/todoist-github

.. |version| image:: https://img.shields.io/pypi/v/todoist-github.svg
    :alt: PyPI Package latest release
    :target: https://pypi.org/project/todoist-github

.. |commits-since| image:: https://img.shields.io/github/commits-since/steven-murray/todoist-github/v0.0.0.svg
    :alt: Commits since latest release
    :target: https://github.com/steven-murray/todoist-github/compare/v0.0.0...master

.. |wheel| image:: https://img.shields.io/pypi/wheel/todoist-github.svg
    :alt: PyPI Wheel
    :target: https://pypi.org/project/todoist-github

.. |supported-versions| image:: https://img.shields.io/pypi/pyversions/todoist-github.svg
    :alt: Supported versions
    :target: https://pypi.org/project/todoist-github

.. |supported-implementations| image:: https://img.shields.io/pypi/implementation/todoist-github.svg
    :alt: Supported implementations
    :target: https://pypi.org/project/todoist-github


.. end-badges

Integrate Github events with todoist tasks and projects


Installation
============

::

    pip install git+git://github.com/steven-murray/todoist-github


Features
========

* Run via command-line
* TOML config file for easy setup
* Creates a new project for every repo that you own or are a member of
* Creates a new task for every issue/PR that you are assigned to, or if you own the repo,
  will make a new task for _every_ issue.
* Removes tasks that are no longer open issues/PRs.
* Allows you to set due dates, organize by priority etc yourself on todoist.
* All tasks are named [issue.name]: [isssue.url] for ease of finding the original issue.

Future features:

* Customize how (and which) tasks are created via the TOML file.

Documentation
=============


Future documentation will be hosted at https://todoist-github.readthedocs.io/

Development
===========

To run the all tests run::

    tox

Note, to combine the coverage data from all the tox environments run:

.. list-table::
    :widths: 10 90
    :stub-columns: 1

    - - Windows
      - ::

            set PYTEST_ADDOPTS=--cov-append
            tox

    - - Other
      - ::

            PYTEST_ADDOPTS=--cov-append tox
