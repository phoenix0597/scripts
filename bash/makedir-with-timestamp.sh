#!/bin/bash
count=0
while true
do
	dirname="/tmp/directory-$(date +%Y%m%d_%H%M)"
	mkdir "$dirname"
	if [ $? -eq 0 ]
	then
		echo "Directory $dirname has created"
		count=$(expr $count + 1)
	else
		echo "Creating directory $dirname failed!"
	fi

	if [ "$count" -ge 7 ]
	then
		break
	fi
	sleep 60
done
