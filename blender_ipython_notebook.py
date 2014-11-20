#!/usr/bin/python3

import sys
from os.path import abspath, dirname, join as pathjoin
from IPython.frontend.html.notebook.notebookapp import launch_new_instance

sys.executable = pathjoin(dirname(abspath(__file__)), 'blender_ipython_kernel.py')

launch_new_instance()
