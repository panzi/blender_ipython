#!/usr/bin/python3

import sys

if sys.argv[1:2] == ['kernel']:
	from blender_ipython_wrapper import launch_kernel
	launch_kernel(sys.argv[1:])
else:
	from os.path       import abspath, dirname, join as pathjoin
	from pkg_resources import load_entry_point

	# use wrapper script for starting python processes
	# the wrapper will defer execution to blender, if it was used to start a new kernel
	sys.executable = pathjoin(dirname(abspath(__file__)), 'blender_ipython_wrapper.py')

	sys.exit(load_entry_point('ipython', 'console_scripts', 'ipython3')())
