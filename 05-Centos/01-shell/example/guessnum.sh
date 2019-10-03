#!/bin/bash
#

price=$(expr $RANDOM % 1000)
time=0

echo "guess price between 1000-0:"

while true
do
    read -p "please enter your price:" INT
    echo "your input is $INT"
    let time++
    if [ $INT -eq $price ]
    then
        echo "good you are right"
        echo "the times you used: $time"
        exit 0
    elif [ $INT -gt $price ]
    then
        echo "too big"
    else
        echo "too small"
    fi
done
