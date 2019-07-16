#!/bin/bash
#

read -p "Please enter a num: " NUM
echo "you entered is: $NUM"

if [ $NUM -gt 85 ] && [ $NUM -le 100 ]
then
    echo "bigger than 85"
elif [ $NUM -gt 65 ] && [ $NUM -le 85 ]
then
    echo "bigger than 65"
else
    echo "less than 65"
fi

