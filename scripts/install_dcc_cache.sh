#!/bin/bash

############################################################################
# make CACHE DISK
############################################################################
if [ ! -d /dcc_cache ]; then
    mkdir /dcc_cache
    chmod -R 777 /dcc_cache
fi

if [ ! -e /dcc_cache/lost+found ]; then
    (echo n; echo p; echo 1; echo ""; echo ""; echo w) | fdisk /dev/nvme1n1
    mkfs -t ext3 /dev/nvme1n1p1
    mount -t ext3 /dev/nvme1n1p1 /dcc_cache
    chmod -R 777 /dcc_cache
fi


###########################################################################
# make SWAP
###########################################################################
dd if=/dev/zero of=/dcc_cache/swapfile bs=128M count=128
chmod 600 /dcc_cache/swapfile
mkswap /dcc_cache/swapfile
swapon /dcc_cache/swapfile



    



