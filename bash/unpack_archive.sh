#!/bin/bash
#set -x
allowed_extensions="gz lzma xz bz2 zip"
unpack_dir="/home/stas/my-projects/unpacked"
# takes an app name as an argument ($1 - $app) and returns true  if this app is installed
check_if_app_installed() {
    if [ $(dpkg -s "$1" 2>/dev/null | grep "No packages found" | wc -l) -eq 0 ]
        then # echo "package exists"
            echo true 
        else # no such package installed
            echo "No such package installed, you need to install it to unpack the file!"
            false
            exit 1
    fi
}

# actually unpacking the file ($1 - the file name)
unpacking_file() {
    file_extension=$(get_file_extension $1)
    app_and_unpacking_command=$(get_app_name "$file_extension")
    app=$(echo "$app_and_unpacking_command" | cut -d " " -f 1)
    unpacking_command=$(echo "$app_and_unpacking_command" | cut -d " " -f 2)
    app_is_installed=$(check_if_app_installed "$app")
    filename_without_ext=$(echo "$1" | sed 's/\.[^.]*$//')
    # check if app is installed
    if "$app_is_installed"
        then
            if [ "$app" = "zip" ]
                then  # it is needed to define target file name for gzip app
                    echo $("$unpacking_command $1" > "$unpack_dir"/"$filename_without_ext")
                else
                    echo $("$unpacking_command" "-c" "$1" > "$unpack_dir"/"$filename_without_ext")
                if [ $? -eq 0 ]
                    then
                        echo "File $1 has successfully unpacked!"
                fi
            fi
    fi
}

# takes a file name as an argument ($1 - the file_name) and returns its extension
get_file_extension() {
    file_extension=$(echo "$1" | sed 's/^.*\.//')
    # check if file has a correct extension
    if  [ $(echo "$allowed_extensions" | grep "$file_extension" | wc -l) -eq 0 ]
    then
        echo "An error has occured, please select file with extensions: gz, lzma, xz, bz2 or zip!"
        exit 1
    else
        echo "$file_extension"
    fi  
    # return $file_extension
}
 
# takes a file extension as an argument ($1 - $file_extension) and returns list ($app; $unpacking_command) parameters to unpack a file
get_app_name() {
app=""
if [ "$1" = "gz" ]
    then 
        app="gzip"; unpacking_command="gunzip"
elif [ "$1" = "lzma" ] || [ "$1" = "xz" ]
    then 
        app="lzma"; unpacking_command="unlzma"
elif [ "$1" = "bz2" ]
    then
        app="bzip2"; unpacking_command="bunzip2"
elif [ "$1" = "zip" ]
    then 
        app="unzip"; unpacking_command="unzip"
fi
echo "$app" "$unpacking_command"
}

check_if_file_exists() {
if [ ! -f "$1" ]
    then
        echo "An error has occured! No such file!"
        exit 1
fi
}

# main part
# 1) Check if file exists ($1 - the file name)
check_if_file_exists "$1"

# 2) unpacking file with its corresponding app ($1 - the file name)
unpacking_file "$1"


