#!/bin/bash
#
#***************************************
#Author:jxiao
#Email: ninggujxiao@gmail.com
#Date:202100929
#FileName: systeminfo.sh
#URL:
#Description: Show system information
#Copyright (C): 2021 All rights reserved
#****************************************
COLOR="\033[1;31m"
END="\033[0m"
echo -e "\033[1;32m-----------------Host systeminfo---------------$END" 
echo -e "HOSTNAME:     $COLOR`hostname`$END" 
echo -e "IPADDR:       $COLOR` ifconfig eth0|grep -Eo '([0-9]{1,3}\.){3}[0-9] 
{1,3}' |head -n1`$END" 
echo -e "OSVERSION:    $COLOR`cat /etc/redhat-release`$END" 
echo -e "KERNEL:       $COLOR`uname -r`$END" 
echo -e "CPU:         $COLOR`lscpu|grep 'Model name'|tr -s ' '|cut -d : -f2`$END" 
echo -e "MEMORY:       $COLOR`free -h|grep Mem|tr -s ' ' : |cut -d : -f2`$END"
echo -e "DISK:         $COLOR`lsblk |grep '^sd' |tr -s ' ' |cut -d " " -f4`$END"
