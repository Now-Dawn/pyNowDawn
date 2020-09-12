#!/usr/bin/env python

from setuptools import setup, find_packages
from pynowdawn.__version__ import __author__, __author_email__, __description__, __license__, __title__,\
    __url__, __version__

setup(
    name=__title__,
    version=__version__,
    description=__description__,
    author=__author__,
    author_email=__author_email__,
    url=__url__,
    packages=find_packages(),
    long_description="""PyNowDawn is a client Python wrapper library for NowDawn web APIs. It allows quick and easy 
    consumption of NowDawn data from Python applications via a simple object model and in a human-friendly fashion.""",
    include_package_data=True,
    install_requires=[
        'requests>=2.20.0,<3',
        'geojson>=2.3.0,<3',
        'PySocks==1.7.1,<2',
        'requests[socks]'
    ],
    python_requires='>=3.7',
    classifiers=[
      "License :: OSI Approved :: MIT License",
      "Programming Language :: Python",
      "Programming Language :: Python :: 3.7",
      "Programming Language :: Python :: 3.8",
      "Natural Language :: English",
      "Operating System :: OS Independent",
      "Intended Audience :: Developers",
      "Topic :: Software Development :: Libraries"],
    package_data={
        '': ['*.bz2', '*.md', '*.txt', '*.json']
    },
    keywords='nowdawn web api client weather forecast uv alerting pollution airquality darksky',
    license=__license__
)