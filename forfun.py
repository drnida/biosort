#!/usr/bin/env python

import os
import subprocess

fail = 0
sort = 0

for x in range(0,100):
    output = subprocess.check_output("python py_code/biosort.py", shell=True)
    for line in output.split('\n'):
        if ',' in line:
            string = line.split(',')
            print str(string[0])
            if int(string[0]) >= 10000000:
                fail = 1 + fail
            else:
                sort = 1 + sort

print "fail: " + str(fail)
print "sort: " + str(sort)
