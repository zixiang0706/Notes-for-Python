!/bin/bash
#this is if script

SYS=`uname`
KERNEL=`uname -r`

if [ $SYS != Linux ]
then
    echo "you sys is $SYS"
    echo "you kernel is $KERNEL"
fi


