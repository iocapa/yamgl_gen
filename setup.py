# -*- coding: utf-8 -*-
 
 
"""setup.py: setuptools control."""

import re
from setuptools import setup

version = re.search(
    '^__version__\s*=\s*"(.*)"',
    open('yamgl_gen/yamgl_gen.py').read(),
    re.M
    ).group(1)
 
 
with open("README.rst", "rb") as f:
    long_descr = f.read().decode("utf-8")
 
 
setup(
    name = "yamgl_gen",
    packages = ["yamgl_gen"],
    entry_points = {
        "console_scripts": ['yamgl_gen = yamgl_gen.yamgl_gen:main']
        },
    version = version,
    description = "Python command line application bare bones template.",
    long_description = long_descr,
    author = "Ionut-Catalin Pavel",
    author_email = "pavel.ionut.catalin.88@gmail.com",
    url = "http://gehrckdsdae.de/2014/02/distributing-a-python-command-line-application",
    )