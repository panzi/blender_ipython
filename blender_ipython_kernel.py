#!/usr/bin/python3

import os
import sys
import distutils.spawn
import subprocess
import tempfile

blender = distutils.spawn.find_executable("blender")
tempscript = tempfile.mktemp()+"_blender_ipython.py"

with open(tempscript,"w") as f:
	f.write("""\
import sys
sys.argv[:] = [sys.executable]
from IPython.zmq.ipkernel import IPKernelApp

app = IPKernelApp.instance()
app.initialize(%r)
app.start()
""" % sys.argv[1:])

try:
	print("starting:", blender, '-b', '-P', tempscript)
	sys.exit(subprocess.call([blender, '-b', '-P', tempscript]))
finally:
	os.remove(tempscript)
