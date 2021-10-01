#!/bin/bash
#
#***************************************
#Author:jxiao
#Email: ninggujxiao@gmail.com
#Date:202100929
#FileName: jindu.sh
#URL:
#Description: a game 
#Copyright (C): 2021 All rights reserved
#****************************************
jindu(){
    while :
    do 
    echo -n "#m" 
    sleep 0.2
    done
}
jingdu &
ls *
killall $!
echo " final"