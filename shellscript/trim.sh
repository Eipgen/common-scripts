#!/usr/bin/env bash
# -*- coding: utf-8 -*-
#Filename:   trim.sh
#Author:     JinXiao
#Email:      ninggujxiao@gmail.com
#Date:       2021-09-30
#Desc:       
set -euf -o pipefail

HEIGHT="${1:-10}"
WIDTH="${2:-$(tput cols)}"

expand |
awk -v height="${HEIGHT}" -v width="${WIDTH}" \
'height <= 0 || NR <= height {
    if (width > 0 && length($0) > width) {
        print substr($0, 1, width - 1) "..."
    } else {
        print
    }
}


END {
    if (height > 0) {
        if (NR == height + 1) {
            print
        } else if (NR > height + 1) {
            print "...with" (NR - height) "more line"
        }
    }
}'

