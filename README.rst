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

* Free software: MIT license

Installation
============

::

    pip install todoist-github

Documentation
=============


https://todoist-github.readthedocs.io/


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
