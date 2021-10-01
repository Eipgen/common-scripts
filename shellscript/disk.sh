#!/bin/bash
#
#***************************************
#Author:jxiao
#Email: ninggujxiao@gmail.com
#Date:202100929
#FileName: disk.sh
#URL:
#Description: Show the Max use ratio 
#Copyright (C): 2021 All rights reserved
#****************************************
BEGIN="\e[1;35m"
END="\e[0m"

echo -e "Disk sda max use ratio is $BEGIN`df  | grep /dev/sda | grep -o '[0-9]\+%'`$END"
echo -e "Disk sdb max use ratio is $BEGIN`df  | grep /dev/sdb | grep -o '[0-9]\+%'`$END"
