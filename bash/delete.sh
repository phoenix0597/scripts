#!/bin/bash
#set -x
trashdir="$HOME/TRASH"

# create TRASH directory if it doesn't exists
if [ ! -d "$trashdir" ]
    then
        mkdir "$trashdir"
        echo "TRASH directory has been created."
fi

# find and remove all the old files and directories in the TRASH folder every time when the sript starts
find "$trashdir" -type f -mtime +2 2>/dev/null | xargs rm -f 
find "$trashdir"/* -type d -mtime +2 2>/dev/null | xargs rm -rf

# if file is a symbolic link, simply delete such file ($1 - the file name)
if [ -h "$1" ]
	then
		echo "File $1 was a symbolic link that linked to the original file $(readlink $1)"
		rm -f "$1"
		echo "Only a symbolic link $1 has been deleted"

# if file is a hard link (i.e it has more then 2 names) just delete it and output 
# the list of another files which have the same inode
elif [ "$(stat -c %h "$1")" ]
	then
		inodenumber=$(stat -c %i "$1")
		rm -f "$1"
		echo "File $1 was a hard link and has been deleted. Another name/names of it is/are:"
		ls -lidR "$PWD"/* | grep "$inodenumber" | awk '{print $10}'
# if the file is usual, then compress and put it into the TRASH directory
else
	gzip -c $1 > "$trashdir"/"$1.gz"
	# delete the original file if compressed file was succsessfully saved
	if [ -f "$trashdir"/"$1.gz" ]
		then
			echo "File $1 was successfuly compessed and put into the TRASH folder."
			rm -f "$1"
	fi
fi

