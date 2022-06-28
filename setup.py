#!/usr/bin/env python
# -*- encoding: utf-8 -*-
from __future__ import absolute_import
from __future__ import print_function

import io
import re
from glob import glob
from os.path import basename
from os.path import dirname
from os.path import join
from os.path import splitext

from setuptools import find_packages
from setuptools import setup


def read(*names, **kwargs):
    with io.open(
        join(dirname(__file__), *names),
        encoding=kwargs.get('encoding', 'utf8')
    ) as fh:
        return fh.read()


setup(
    name='todoist-github',
    version='0.1.0',
    license='MIT license',
    description='Integrate Github events with todoist tasks and projects',
    long_description='%s\n%s' % (
        re.compile('^.. start-badges.*^.. end-badges', re.M | re.S).sub('', read('README.rst')),
        re.sub(':[a-z]+:`~?(.*?)`', r'``\1``', read('CHANGELOG.rst'))
    ),
    author='Steven Murray',
    author_email='steven.g.murray@asu.edu',
    url='https://github.com/steven-murray/todoist-github',
    packages=find_packages('src'),
    package_dir={'': 'src'},
    py_modules=[splitext(basename(path))[0] for path in glob('src/*.py')],
    include_package_data=True,
    zip_safe=False,
    classifiers=[
        # complete classifier list: http://pypi.python.org/pypi?%3Aaction=list_classifiers
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: Unix',
        'Operating System :: POSIX',
        'Operating System :: Microsoft :: Windows',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: Implementation :: CPython',
        'Programming Language :: Python :: Implementation :: PyPy',
        # uncomment if you test on these interpreters:
        # 'Programming Language :: Python :: Implementation :: IronPython',
        # 'Programming Language :: Python :: Implementation :: Jython',
        # 'Programming Language :: Python :: Implementation :: Stackless',
        'Topic :: Utilities',
    ],
    project_urls={
        'Documentation': 'https://todoist-github.readthedocs.io/',
        'Changelog': 'https://todoist-github.readthedocs.io/en/latest/changelog.html',
        'Issue Tracker': 'https://github.com/steven-murray/todoist-github/issues',
    },
    keywords=[
        # eg: 'keyword1', 'keyword2', 'keyword3',
    ],
    python_requires='>=3.5',
    install_requires=[
        'click',
        'cached_property',
        'pygithub',
        'todoist-python',
        'toml'
        # eg: 'aspectlib==1.1.1', 'six>=1.7',
    ],
    extras_require={
        'dev': ['bump2version', 'sphinx'],
        #   ':python_version=="2.6"': ['argparse'],
    },
    setup_requires=[
    ],
    entry_points={
        'console_scripts': [
            'tdg = todoist_github.cli:main',
        ]
    },
)
