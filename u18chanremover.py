#!/bin/python

import os
for root, dirs, files in os.walk('.'):
	for fname in files:
		fpath_old = os.path.join(root, fname)
		fsplit = os.path.splitext(fname)
		fbase = fsplit[0]
		fext = fsplit[1]
		if not fbase.endswith('_u18chan'):
			continue
		fpath_new = os.path.join(root, fbase[:-8]) + fext
		if os.path.isfile(fpath_new):
			print('SKIPPED: ' + fpath_new + ' (ALREADY EXISTS)')
			continue
		print(fpath_old + ' -> ' + fpath_new)
		os.rename(fpath_old, fpath_new)
