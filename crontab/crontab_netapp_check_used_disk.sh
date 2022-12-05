#/bin/bash

TARGET='/office_share/aws/Billing/daily_used_disk_size.txt'


echo '' >> $TARGET
echo '' >> $TARGET
echo '' >> $TARGET
echo '========================================================' >> $TARGET
date '+%Y-%m-%d' >> $TARGET
echo '========================================================' >> $TARGET

sshpass -p Zmffkdnem1! ssh fsxadmin@172.31.69.184 \
volume show -vserver fsx-svm01 -volume fsx_svm01_netapp | grep -A 3 'Filesystem Size:' >> $TARGET