#!/bin/bash

check=`ps -ef | grep -v "grep" | grep "2d-tq.py" | wc -l`

if [ $check == 0 ]; then
    /home/centos/WORK/tq_stop_farm.py
fi




