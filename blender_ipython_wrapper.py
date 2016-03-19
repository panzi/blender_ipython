#!/usr/bin/python3

import os
import sys
import subprocess
import tempfile

__all__ = 'launch_kernel', 'main'

def launch_kernel(argv):
	tempscript = tempfile.mktemp()+"_blender_ipython_kernel.py"

	# generate kernel starter script
	with open(tempscript,"w") as f:
		f.write("""\
import sys
sys.argv[:] = [sys.executable]
try:
	from IPython.zmq.ipkernel import IPKernelApp
except ImportError as err:
	from ipykernel.kernelapp import IPKernelApp

app = IPKernelApp.instance()
app.initialize(%r)
app.start()
""" % argv)

	try:
		print('starting: blender -b -P', tempscript)
		sys.exit(subprocess.call(['blender', '-b', '-P', tempscript]))
	finally:
		os.remove(tempscript)

def main():
	if sys.argv[1:3] != ['-c', 'from IPython.zmq.ipkernel import main; main()']:
		# if it wasn't used to start a kernel really execute python
		os.execlp('python3','python3',*sys.argv[1:])
	else:
		launch_kernel(sys.argv[1:])

if __name__ == '__main__':
	main()
