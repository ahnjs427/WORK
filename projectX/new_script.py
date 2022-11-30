#!/usr/bin/env python

from __future__ import print_function

import os, sys
import time
from datetime import datetime, timedelta
import subprocess
import logging

logging.basicConfig(level=logging.DEBUG, format="'%(asctime)s - %(message)s'")


empty_list = []

def run_daemon_win_name() -> str:
    while True:
        key = datetime.now().strftime('%Y%m%d-%H%M')
        val = subprocess.check_output(['xdotool', 'getactivewindow', 'getwindowname']).decode().strip()
        dic = {key:val}
        # empty_list.append(dic)
        print (dic)

        time.sleep(3)

run_daemon_win_name()

win_pid = subprocess.check_output(['xdotool', 'getactivewindow', 'getwindowpid']).decode().strip()




































