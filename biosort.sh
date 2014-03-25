#!/usr/bin/env bash
#Starts python program and cleans up after it

if [ -e ./logs/log* ]
then
    read -p "Do you wish do delete pre-existing log files? " response
    case $response in
            [Yy]* ) rm ./log/log* 2> /dev/null;;
            [Nn]* ) echo "Exiting..."; exit;;
            * ) echo "Please respond yes or no";;
        esac
fi

python py_code/biosort.py

rm py_code/*.pyc
