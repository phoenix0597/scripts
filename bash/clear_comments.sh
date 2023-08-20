#!/bin/bash

if [ -x "$1" ]
then
    grep "^#!" "$1" > "$1".cleared
    grep -v "^#" "$1" >> "$1".cleared
    echo "The code of the script $1 has cleared from comments. See $1.cleared file"
else
    echo "The file $1 is not executable!"
fi


