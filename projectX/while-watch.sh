#!/bin/bash

while true; do
	xdotool getactivewindow getwindowname >> output.txt
	sleep 3
done
