#!/bin/bash
#test if and else 

ping -c 3 -i 0.2 -t 3  $1 >/dev/null

if [ $? -eq 0 ]
then
    echo "target is up"
else
    echo "target is down"
fi

