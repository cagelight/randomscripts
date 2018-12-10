#!/bin/python

import getopt
import os
import random
import sys
import math

from natsort import natsorted

rsindir = os.getcwd()
rsnum = 0
rslen = 'auto'
rsprefix = ""
rspostfix = ""
rsnatural = True
rsdirs = False

def main(argv):
	
	global rsindir
	global rsnum
	global rslen
	global rsprefix
	global rspostfix
	global rsnatural
	global rsdirs
	
	opts, args = getopt.getopt(argv,"Ni:n:l:d",["prefix=", "postfix="])
	for opt, arg in opts:
		if opt == '-N':
			rsnatural = False
		if opt == '-i':
			rsindir = arg
		if opt == '-n':
			rsnum = int(arg)
		if opt == '-l':
			rslen = int(arg)
		if opt == '--prefix':
			rsprefix = arg
		if opt == '--postfix':
			rspostfix = arg
		if opt == '-d':
			rsdirs = True
			
	files_orig = None
	if (rsdirs):
		files_orig = [f for f in os.listdir(rsindir) if os.path.isdir(f)]
	else:
		files_orig = [f for f in os.listdir(rsindir) if os.path.isfile(f)]
		
	if rsnatural:
		files_orig = natsorted(files_orig)
	else:
		files_orig = sorted(files_orig)
	
	if rslen == 'auto':
		rslen = math.ceil(math.log(len(files_orig) + rsnum, 10))
	
	files_temp = []
	files_new_strs = []
	files_new_exts = []
	
	fcur = rsnum
	
	for f in files_orig:
		fn, fext = os.path.splitext(f)
		files_temp.append(".arename__temp_"+str(fcur)+fext)
		rs = str(fcur)
		rs = rs.zfill(rslen)
		rs = rsprefix + str(rs) + rspostfix
		files_new_strs.append(rs)
		files_new_exts.append(fext)
		fcur += 1
	
	for fo, ft in zip(files_orig, files_temp):
		os.rename(fo, ft)
	
	for ft, fn, fne in zip(files_temp, files_new_strs, files_new_exts):
		os.rename(ft, fn+fne)

if __name__ == "__main__":
   main(sys.argv[1:])
