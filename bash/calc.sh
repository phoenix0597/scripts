#!/bin/bash
read -p "Enter first value: " x
read -p "Enter second value: " y
read -p "Enter action symbol: " operator


# check for division by zero
if [ "$operator" = "/" ] && [ "$y" -eq 0 ]
then
	echo "Cannot be divided by zero!"
	exit 1
fi

# calculations
case $operator in
	"+") echo " $x + $y =" $(expr "$x" + "$y");;
	"*") echo " $x * $y =" $(expr "$x" \* "$y");;
	"-") echo " $x - $y =" $(expr "$x" - "$y");;
	"/") echo " $x / $y =" $(expr "$x" / "$y");;
	"**") echo " $x ** $y =" $(("$x"**"$y"));;
	*) echo "unknown operation!"
esac

