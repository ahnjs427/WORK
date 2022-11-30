#!/usr/bin/env python

from __future__ import print_function

import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

import Xlib
import Xlib.display

display = Xlib.display.Display()
root = display.screen().root
windows = display.create_resource_object('window', 2243).get_wm_name()

# dsp = display.Display()

# dsp_name = dsp.get_display_name()
# dsp_ds = dsp.get_default_screen()

