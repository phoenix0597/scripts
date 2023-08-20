#!/bin/bash

#echo "Choose the directory for searching executable file: "
#read dir

for file in $(find "/usr" -type f)
do
    # select only executable files from the list
    if [ -x "$file" ]
        then
            echo "$file"
    fi
done



