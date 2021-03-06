================
yamgl_gen v0.0.5
================

:Author: `Ionut-Catalin Pavel <pavel.ionut.catalin.88@gmail.com>`_

.. contents::
    :backlinks: none

.. sectnum::

Introduction
============

What is yamgl_gen?
------------------

**yamgl_gen** is a generator used for producing compile time object data 
for the yamgl library.

How is yamgl_gen licensed?
--------------------------

`CC-BY-SA <https://github.com/iocapa/yamgl_gen/blob/master/LICENSE>`_.

Contact details
---------------

For reporting problems with **yamgl_gen** or submitting feature requests, please
open an `issue <https://github.com/iocapa/yamgl_gen/issues>`_, or submit a
pull request.

Installing
==========

Prerequisites
-------------

* **yamgl_gen** was tested on Python 3.6, on Windows. 
  Compatibility with older version is not guaranteed.

* **yamgl_gen** has the following dependencies:

 * `lxml <https://github.com/lxml/lxml>`_

 * `freetype <https://github.com/rougier/freetype-py>`_ 

 * `Pillow <https://github.com/python-pillow/Pillow>`_ 

Installation process
--------------------

Installing **yamgl_gen** is very simple. Once you download and unzip the
package, you just have to execute the standard ``python setup.py install``. The
setup script will then place the ``yamgl_gen`` module into ``site-packages`` in
your Python's installation library.

Alternatively, since **yamgl_gen** is listed in the `Python Package Index
<http://pypi.python.org/pypi/yamgl_gen>`_ (PyPI), you can install it using your
favorite Python packaging/distribution tool, for example with::

    > pip install yamgl_gen

Using
=====

Usage rationale
---------------

yamgl_gen parses a given xlm file that must comply with the following `schema
<https://github.com/iocapa/yamgl_gen/blob/master/yamgl_gen/schema.xsd>`_ , the 
xml file contains all the objects that generate data.

Usage scenario
--------------

A sample `xml <https://github.com/iocapa/yamgl_gen/blob/master/examples/example.xml>`_ 
file is given inside the examples folder. The file contains generation instructions 
for some fonts and a image. The fonts and the image are not part of this release due 
to legal reasons.

The application will generate a pair of source files (a source and a header). The 
command line syntax is better detailed by running::
    
    > python yamgl_gen --help

Package contents
================

Once you unzip the ``yamgl_gen`` package, you'll see the following files and
directories:

README.rst:
  This README file.

LICENSE:
  The yamgl_gen license

setup.py:
  Installation script

examples/:
  A directory with some examples of using **yamgl_gen**

yamgl_gen/:
  The **yamgl_gen** module source code.

tests/:
  Unit tests.