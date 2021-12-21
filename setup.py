import os
import sys

from distutils.util import convert_path
from fnmatch import fnmatchcase
from setuptools import setup, find_packages




# Provided as an attribute, so you can append to these instead
# of replicating them:
standard_exclude = ["*.py", "*.pyc", "*$py.class", "*~", ".*", "*.bak"]
standard_exclude_directories = [
    ".*", "CVS", "_darcs", "./build", "./dist", "EGG-INFO", "*.egg-info"
]

# (c)

PACKAGE = "django-notes"
NAME = "notes"
DESCRIPTION = "A simple reusable app to add notes to various models"
AUTHOR = "Colin Powell"
AUTHOR_EMAIL = "colin@onecardinal.com"
URL = "http://github.com/powellc/django-notes/"
VERSION = "1.0.0"


setup(
    name=NAME,
    version=VERSION,
    description=DESCRIPTION,
    long_description="",
    author=AUTHOR,
    author_email=AUTHOR_EMAIL,
    license="BSD",
    url=URL,
    packages=find_packages(exclude=["tests.*", "tests"]),
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Environment :: Web Environment",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: BSD License",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Framework :: Django",
    ],
    zip_safe=False,
)

