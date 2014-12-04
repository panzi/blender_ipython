#!/usr/bin/python3

import sys

if sys.argv[1:2] == ['kernel']:
	from blender_ipython_wrapper import launch_kernel
	launch_kernel(sys.argv[1:])
else:
	from os.path import abspath, dirname, join as pathjoin

	try:
		from IPython.frontend.terminal.ipapp import launch_new_instance
	except ImportError:
		from IPython.terminal.ipapp import launch_new_instance

	# use wrapper script for starting python processes
	# the wrapper will defer execution to blender, if it was used to start a new kernel
	sys.executable = pathjoin(dirname(abspath(sys.argv[0])), 'blender_ipython_wrapper.py')

	launch_new_instance()
