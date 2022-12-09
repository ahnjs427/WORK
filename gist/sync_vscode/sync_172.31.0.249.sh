#!/bin/bash


# copy to VDI12-TD-C

rsync -avhz --delete --progress -e "ssh -i ~/Downloads/vdi-pc.pem" /home/centos/.vscode-server/* centos@172.31.0.249:/home/centos/.vscode-server/
