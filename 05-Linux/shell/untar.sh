#!/bin/bash
case $1 in 
	*.tar.gz)
		tar zxf $1
	;;
	*.tar.bz2)
		tar jxf $1
	;;
esac
