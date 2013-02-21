#!/usr/bin/env python
import sys

def average(proc,jobs,time):
    value = ((proc-1)*time)/jobs
    return value

try:
    input_file = sys.argv[1]
except:
    print "Please specify an input file"
    sys.exit(1)

infile = open(input_file,'r')

for line in infile:
    tmp = line.split()
    print tmp

infile.seek(0)
while True:
    line = infile.readline()
    if not line:
        break
    print line.split()    

infile.close()
