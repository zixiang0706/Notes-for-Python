#!/bin/bash
#

systemctl status httpd >> /dev/null
if [ $? -eq 0 ]
then
    echo "Http is running"
elif [ $? -ne 0 ]
then 
    echo "Http is stop! try to restart" >> /var/log/httperr.log
    read -p "restart?[y/n]" DO
    echo "  Your input is: $DO"
    if [ $DO == y ]
    then
        echo " restarting"
        systemctl restart httpd
    elif [ $DO == n ]
    then
        echo " script stop"
    else
        echo "wrong input"
    fi
fi
    

