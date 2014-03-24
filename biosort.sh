#!/usr/bin/env bash
#Starts python program and cleans up after it
rm ./log/log* 2> /dev/null

python py_code/biosort.py

rm py_code/*.pyc
