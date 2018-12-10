#!/bin/python

import sys
import os
import signal

if len(sys.argv) > 1:
	d = sys.argv[1]
else:
	raise Exception("NEED ARGUMENT")

tsort = [t for t in open(d, 'r').read().splitlines() if len(t) > 0]
fsort = []
psort = []

def save_file():
	f = open(d, 'w')
	for i in range(len(tsort)):
		f.write("{0}\n".format(tsort[i]))
	for i in range(len(fsort)):
		f.write("{0}\n".format(fsort[i]))

def signal_handler(signal, frame):
	print("Interrupt received, saving progress...")
	save_file()
	sys.exit(0)
signal.signal(signal.SIGINT, signal_handler)

while len(tsort) > 1:
	for i in range(len(tsort) - 1):
		if [tsort[i], tsort[i+1]] in psort:
			continue
		val = 2
		while val not in [0, 1]:
			print("(0)[{0}] or (1)[{1}]".format(tsort[i], tsort[i+1]))
			try:
				val = int(sys.stdin.readline())
			except ValueError:
				pass
		if val == 1:
			tsort[i], tsort[i+1] = tsort[i+1], tsort[i]
		psort.append([tsort[i], tsort[i+1]])
	fsort.insert(0, tsort[-1])
	tsort.pop()
fsort.insert(0, tsort[-1])
tsort.pop()

save_file()
print("\n\n\nRESULTS:")
for i in range(len(fsort)):
	print("{0}. {1}".format(i+1, fsort[i]))
