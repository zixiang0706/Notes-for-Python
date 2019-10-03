#!/bin/bash
#

USER=$(cat file)
echo $USER
for i in $USER
do
    echo "find: $i"
done
