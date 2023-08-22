#!/bin/bash

# if program "fortune" doesn't installed then quit
if ! which fortune >/dev/null; 
then
  echo "The package "fortune" doesn't installed on this system"
	exit 1
fi

# show only even strings with cookies quotes
num=1
while [ "$num" -lt 11 ]
do 
	if [ $(expr "$num" % 2) -eq 0 ]
	then
		echo "$num $(fortune)"
	fi
	num=$(expr "$num" + 1)
done
