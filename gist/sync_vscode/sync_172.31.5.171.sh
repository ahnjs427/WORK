#!/bin/bash


# copy to PRODUCTION FTP & TRACTOR-ENGINE
rsync -avhz --delete --progress -e "ssh -i ~/Downloads/vdi-pc.pem" /home/centos/.vscode-server/* centos@172.31.5.171:/home/centos/.vscode-server/
