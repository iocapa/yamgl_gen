# -*- coding: utf-8 -*-
 
 
"""setup.py: setuptools control."""

import re
from setuptools import setup
from os import path

version = re.search(
    '^__version__\s*=\s*"(.*)"',
    open('yamgl_gen/yamgl_gen.py').read(),
    re.M
    ).group(1)
 

here = path.abspath(path.dirname(__file__))

with open(path.join(here, 'README.rst'), encoding='utf-8') as f:
    long_descr = f.read()
 
 
setup(
    name = "yamgl_gen",
    packages = ["yamgl_gen"],
    entry_points = {
        "console_scripts": ['yamgl_gen = yamgl_gen.yamgl_gen:main']
        },
    include_package_data = True,
    version = version,
    description = "Data structure generator for the yamgl library (Yet Another Monochrome Graphics Library).",
    long_description = long_descr,
    author = "Ionut-Catalin Pavel",
    author_email = "pavel.ionut.catalin.88@gmail.com",
    url = "https://github.com/iocapa/yamgl_gen",
    )