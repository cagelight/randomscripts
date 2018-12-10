#!/bin/python

import os
import subprocess

for item in os.listdir('.'):
	try:
		path = os.path.join('.', item)
		if not os.path.isfile(path):
			continue
		i1 = item.index('_')
		i2 = item.index('.')
		if i1 < i2:
			continue
		artist = item[i2+1:i1]
		
		newdir = os.path.join('.', 'fa', artist)
		newpath = os.path.join(newdir, item)
		
		if not os.path.exists(newdir):
			os.makedirs(newdir)
		
		subprocess.call(['mv', '-vn', path, newpath])
	except:
		continue
