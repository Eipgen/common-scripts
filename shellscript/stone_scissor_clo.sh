#!/bin/bash
#
#***************************************
#Author:jxiao
#Email: ninggujxiao@gmail.com
#Date:202100929
#FileName: rock_scissor_cloth.sh
#URL:
#Description: a game 
#Copyright (C): 2021 All rights reserved
#****************************************

game=("rock" "sicc" "clo")
num=$[$RANDOM%3]
computer=${game[$num]}
echo $computer


echo "please give your choice"

echo "1. rock"
echo "2. scissor"
echo "3. paper"

read -p "please chose 1-3:" person
case $person in 
1)
if [ $num -eq 0 ]; then
    echo "Tie"
elif [ $num -eq 1 ];then
    echo "you win"
else
    echo "you fail"
fi;;
2)
if [ $num -eq 0 ]; then
    echo "you fail"
elif [ $num -eq 1 ];then
    echo "Tie"
else
    echo "you win"
fi;;
3)
if [ $num -eq 0 ]; then
    echo "you win"
elif [ $num -eq 1 ];then
    echo "you fail"
else
    echo "Tie"
fi;;
*)
echo "must be in 1-3"
esac