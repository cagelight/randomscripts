#!/bin/python

import os
from PIL import Image

for root, dirs, files in os.walk('.'):
	for fname in files:
		fpath_old = os.path.join(root, fname)
		fsplit = os.path.splitext(fname)
		fbase = fsplit[0]
		fext = fsplit[1]
		fextc = fext[1:]
		fpath_new = fpath_old
		
		try:
			img = Image.open(fpath_old)
		except:
			continue
		fmt = img.format
		
		if (fmt == 'JPEG'):
			if (fextc.upper() not in ['JPG', 'JPEG']):
				print('INCORRECT EXTENSION: (\'' + fpath_old + '\') IS ACTUALLY ' + fmt)
				fpath_new = os.path.join(root, fbase) + '.jpg'
		else:
			if (fextc.upper() != fmt):
				print('INCORRECT EXTENSION: (\'' + fpath_old + '\') IS ACTUALLY ' + fmt)
				fpath_new = os.path.join(root, fbase) + '.' + fmt.lower()
				
		if (fpath_new == fpath_old):
			continue
			
		if os.path.isfile(fpath_new):
			print('SKIPPED: ' + fpath_new + ' (ALREADY EXISTS)')
			continue
			
		print('RENAMED: ' + fpath_old + ' -> ' + fpath_new)
		os.rename(fpath_old, fpath_new)
