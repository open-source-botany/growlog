========
Overview
========

.. start-badges

.. list-table::
    :stub-columns: 1

    * - docs
      - |docs|
    * - tests
      - | |travis| |appveyor| |requires|
        | |codecov|
    * - package
      - | |version| |wheel| |supported-versions| |supported-implementations|
        | |commits-since|

.. |docs| image:: https://readthedocs.org/projects/growlog/badge/?style=flat
    :target: https://readthedocs.org/projects/growlog
    :alt: Documentation Status

.. |travis| image:: https://travis-ci.org/open-source-botany/growlog.svg?branch=master
    :alt: Travis-CI Build Status
    :target: https://travis-ci.org/open-source-botany/growlog

.. |appveyor| image:: https://ci.appveyor.com/api/projects/status/github/open-source-botany/growlog?branch=master&svg=true
    :alt: AppVeyor Build Status
    :target: https://ci.appveyor.com/project/open-source-botany/growlog

.. |requires| image:: https://requires.io/github/open-source-botany/growlog/requirements.svg?branch=master
    :alt: Requirements Status
    :target: https://requires.io/github/open-source-botany/growlog/requirements/?branch=master

.. |codecov| image:: https://codecov.io/github/open-source-botany/growlog/coverage.svg?branch=master
    :alt: Coverage Status
    :target: https://codecov.io/github/open-source-botany/growlog

.. |version| image:: https://img.shields.io/pypi/v/growlog.svg
    :alt: PyPI Package latest release
    :target: https://pypi.python.org/pypi/growlog

.. |commits-since| image:: https://img.shields.io/github/commits-since/open-source-botany/growlog/v0.4.0.svg
    :alt: Commits since latest release
    :target: https://github.com/open-source-botany/growlog/compare/v0.4.0...master

.. |wheel| image:: https://img.shields.io/pypi/wheel/growlog.svg
    :alt: PyPI Wheel
    :target: https://pypi.python.org/pypi/growlog

.. |supported-versions| image:: https://img.shields.io/pypi/pyversions/growlog.svg
    :alt: Supported versions
    :target: https://pypi.python.org/pypi/growlog

.. |supported-implementations| image:: https://img.shields.io/pypi/implementation/growlog.svg
    :alt: Supported implementations
    :target: https://pypi.python.org/pypi/growlog


.. end-badges

A simple CLI garden journal

* Free software: MIT license

Installation
============

::

    pip install growlog

Documentation
=============

https://growlog.readthedocs.io/

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
