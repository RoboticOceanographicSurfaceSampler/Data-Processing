#!/usr/bin/env python
'''
Process Folder handler for processROSSLogs
Written by Nick McComb
Version 1.0 [Aug 2016]

This script is a higher level handler designed for the processROSSLogs.sh script
that will parse all of the files in a current directory. It looks for all of the
files exported by the pixhawk and then sends them to the other script.

'''

import os
import glob

exeTarget = 'processROSSLogs.sh'

logs = glob.glob('***.BIN')
logs.sort()
print 'Processing: '
print logs

for target in logs:
	print '[[[PROCESSING ' + target + ']]]'
	os.system('./' + exeTarget + ' ' + target)
