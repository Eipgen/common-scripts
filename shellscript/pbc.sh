#!/bin/bash
#
#***************************************
#Author:jxiao
#Email: ninggujxiao@gmail.com
#Date:202100929
#FileName: pbc.sh
#URL:
#Description: parakkel bc
#Copyright (C): 2021 All rights reserved
#****************************************

parallel -C, -k -j100% "echo '$1' | bc -l"
