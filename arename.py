#!/bin/python

import getopt
import os
import random
import sys
import math

rsindir = os.getcwd()
rslen = 8
rsprefix = ""
rspostfix = ""
rbupper = False
recurse = False

def rstr():
	rb = random.getrandbits(4 * rslen)
	rsn = rsprefix+'{0:0{1}x}'.format(rb, rslen)+rspostfix
	if rbupper:
		rsn = rsn.upper()
	return rsn

def main(argv):
	
	global rsindir
	global rslen
	global rsprefix
	global rspostfix
	global rbupper
	global recurse
	
	opts, args = getopt.getopt(argv,"i:n:ru",["prefix=", "postfix="])
	for opt, arg in opts:
		if opt == '-i':
			rsindir = arg
		if opt == '-n':
			if arg == 'auto':
				rslen = 'auto'
			else:
				rslen = int(arg)
		if opt == '-r':
			recurse = True
		if opt == '-u':
			rbupper = True
		if opt == '--prefix':
			rsprefix = arg
		if opt == '--postfix':
			rspostfix = arg
			
	files_orig = []
	if recurse:
		for root, dirs, files in os.walk(rsindir):
			for name in files:
				files_orig.append(os.path.join(root, name))
	else:
		files_orig = [f for f in os.listdir(rsindir) if os.path.isfile(f)]
	if rslen == 'auto':
		rslen = int(math.ceil((math.log(len(files_orig) + 1) / math.log(2)) / 4))
	files_temp = []
	files_new_strs = []
	files_new_exts = []
	
	fcur = 0
	
	for f in files_orig:
		fn, fext = os.path.splitext(f)
		files_temp.append(".arename__temp_"+str(fcur)+fext)
		fcur += 1
		while True:
			rs = rstr()
			if not rs in files_new_strs:
				files_new_strs.append(rs)
				files_new_exts.append(fext)
				break
	
	for fo, ft in zip(files_orig, files_temp):
		os.rename(fo, ft)
	
	for ft, fn, fne in zip(files_temp, files_new_strs, files_new_exts):
		os.rename(ft, fn+fne)

if __name__ == "__main__":
   main(sys.argv[1:])
