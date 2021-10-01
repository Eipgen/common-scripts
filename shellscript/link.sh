#!/bin/bash
#
#***************************************
#Author:jxiao
#Email: ninggujxiao@gmail.com
#Date:202100929
#FileName: link.sh
#URL:
#Description: Show the Max use ratio 
#Copyright (C): 2021 All rights reserved
#****************************************

COLOR="\e[1;34m"
END="\e[0m"

RESULT=`netstat -tan|egrep 'ESTABLISHED' |tr -s ' ' : |cut -d: -f6|sort| uniq -c |sort -nr`
echo -e "$COLOR Active Internet connections's status:\n$RESULT$END"
