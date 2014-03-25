#!/usr/bin/env bash
#Starts python program and cleans up after it

if [ -e ./logs/log* ]
then
    while true; do
		  read -p "Do you wish do delete pre-existing log files? " response
        case $response in
            [Yy]* ) rm ./logs/log* 2> /dev/null; break;;
            [Nn]* ) echo "Exiting..."; exit;;
            * ) echo "Please respond yes or no";;
        esac
    done
fi

python py_code/biosort.py

rm py_code/*.pyc
