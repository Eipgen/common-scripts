#!/usr/bin/env bash
# -*- coding: utf-8 -*-
#Filename:   trim.sh
#Author:     JinXiao
#Email:      ninggujxiao@gmail.com
#Date:       2021-09-30
#Desc:       trim


BEGIN {
    "tput cols" | getline width
    height = 10
}

NR <= height {
    if (length($0) > width) {
        print substr($0, 1, width - 1) "..."
        } else {
            print
        }
}

END {
    if (NR == height + 1) {
        print
    } else if (NR > height + 1) {
        print "...with " (NR - height) " more line"
        }
}
