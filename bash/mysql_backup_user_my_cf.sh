#!/bin/bash
 
destination="/home/stas/backup/mysql"
fileDate=`date +%Y-%m-%d_%H-%M`
dbname="database1"
cffile="/home/stas/.mysqldump.cf"


# check if mysql.service is running (we can't do backup if it is not)
systemctl status mysql.service >/dev/null
if [ "$?" -ne 0 ];
	then echo "The service 'mysql' is not running, creating a backup file is impossible!"
	exit 1
fi 

# find all backups that are older than 7 days and delete them
find $destination -type f -name "*.sql*" -mtime +7 -exec rm {} \; 2>/dev/null

if [ "$?" -eq 0 ]; 
	then echo "All expired backup files in the directory '$destination' have been successfully deleted" 
fi

# create a directory (if it does not exist) in which we will save backups
test -d $destination || mkdir -p $destination 2>/dev/null

# create a database backup, compress it and place it in the specified directory
mysqldump --defaults-extra-file="$cffile" "$dbname" | gzip > "$destination"/"$fileDate"-"$dbname".sql.gz

if [ "$?" -eq 0 ];
  then echo "Backup file '$destination/$fileDate-$dbname.sql.gz' has been successfully created"
	else echo "Failed to back up database $dbname! See log file."
fi
