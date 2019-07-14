#!/bin/bash
#login script

#user=root
read -p "Please enter your usename: " name
echo "Your usename is: $name"
if [ $name == root ]
then
    read -p "Please enter your password: " password
    if [ $password == 123456 ]
    then
        echo "Good!"
    else
        echo "failed"
    fi
fi
