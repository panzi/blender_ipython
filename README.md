IPython for Blender
===================

These scripts contain hacks in order to run [IPython][1] in the context of [Blender's][2]
embedded Python interpreter.

[1]: http://ipython.org/
[2]: http://www.blender.org/

Usage
-----

Start an IPython Notebook:

	./blender_ipython.py notebook


Start a Qt Console:

	./blender_ipython.py qtconsole

Dependencies
------------

 * [Python][3] 3.3 (not tested with Python 3.4)
 * [IPython][1] 0.13 for Python 3 (not tested with IPython 1.x)
 * [Blender][2]

I only have Python 3.3 and IPython 0.13 and thus this was not tested with any newer versions. Because this scripts use big hacks to get the IPython kernel running in Blender it is very likely that it won't work with any other versions. In fact I got bug reports where people with Python 3.4 and IPython 1.x could not get it to work.

[3]: https://www.python.org/

The MIT License (MIT)
---------------------

Copyright (c) 2014 Mathias Panzenböck

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in
all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
THE SOFTWARE.
