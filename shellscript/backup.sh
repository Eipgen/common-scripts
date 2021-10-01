#!/bin/bash
#
#***************************************
#Author:jxiao
#Email: ninggujxiao@gmail.com
#Date:202100929
#FileName: backup.sh
#URL:
#Description: back etc dir into backup
#Copyright (C): 2021 All rights reserved
#****************************************

echo -e "\033[1;32mStaring backup... \033[0m"
sleep 2
cp -av /etc/GeoIP.conf ./data/`date +%F` 
echo -e "\033[1;32mBackup is finished\033[0m"

