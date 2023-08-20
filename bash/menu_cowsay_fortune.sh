#!/bin/bash

while true
do
	echo "Who do you want advice from?"
	cat << options
bunny
tux
daemon
kitty
vader-koala
quit
options
read -p "Make your choice: " option
if [ "$option" = "quit" ]
	then
		echo
		echo "Goodbuy!"
		break
	else
		fortune | cowsay -f $option
fi
done

