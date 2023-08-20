#!/bin/bash

# Checking the Internet connection:
# 1. Try to resolve domain names ya.ru and google.com
host ya.ru > /dev/null; code_host1=$?
host google.com > /dev/null; code_host2=$?

if [ "$code_host1" -eq 0 ] && [ "$code_host2" -eq 0 ]
then
	echo "ya.ru, google.com are successfully mapped to their IP-addresses"
else

	echo "ya.ru or/and google.com cannot be mapped to IP-addresses now!"
fi

# 2. Try to ping ya.ru and google.com
res_ping1=$(ping -c4 ya.ru | tail -3); code_ping1=$?
res_ping2=$(ping -c4 google.com | tail -3); code_ping2=$?

if [ "$code_ping1" -eq 0 ] && [ "$code_ping2" -eq 0 ]
then
	echo "ya.ru, google.com are successfully pinged:"
	echo $res_ping1
	echo $res_ping2
else

	echo "attempt to ping ya.ru or/and google.com failed!"
fi


