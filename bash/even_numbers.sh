#!/bin/bash

num=1
while [ "$num" -lt 11 ]
do 
	if [ $(expr "$num" % 2) -eq 0 ]
	then
		echo "$num $(fortune)"
	fi
	num=$(expr "$num" + 1)
done
