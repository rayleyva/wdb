#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
wdb
"""
import os
import re
from setuptools import setup, find_packages

ROOT = os.path.dirname(__file__)
with open(os.path.join(ROOT, 'wdb', '__init__.py')) as fd:
    __version__ = re.search("__version__ = '([^']+)'", fd.read()).group(1)

options = dict(
    name="wdb",
    version=__version__,
    description="An improbable web debugger through WebSockets",
    long_description="See http://github.com/Kozea/wdb",
    author="Florian Mounier @ kozea",
    author_email="florian.mounier@kozea.fr",
    url="http://github.com/Kozea/wdb",
    license="GPLv3",
    platforms="Any",
    scripts=['wdb.server.py'],
    packages=find_packages(),
    install_requires=["tornado", "log_colorizer", "jedi", "filemagic"],
    package_data={
        'wdb_server': [
            'static/fonts/*',
            'static/stylesheets/*',
            'static/javascripts/*.js',
            'templates/*.html'
        ],
        'wdb': [
            'res/*'
        ]
    },
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 2",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: Implementation :: CPython",
        "Programming Language :: Python :: Implementation :: PyPy",
        "Topic :: Software Development :: Debuggers"])

setup(**options)
