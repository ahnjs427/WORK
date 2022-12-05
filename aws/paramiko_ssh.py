#! /usr/bin/env python

import paramiko

client = paramiko.SSHClient()
client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

list_td   = [ '172.31.9.147',  '172.31.12.251', ]
list_mgmt = [ '172.31.5.171',  '172.31.14.192', ]
list_farm = [ '172.31.4.220',  '172.31.3.46', '172.31.9.132',  '172.31.15.134', '172.31.1.192']
list_vdi  = [ '172.31.11.228', '172.31.3.20',  '172.31.10.171', '172.31.15.209', '172.31.14.249',
              '172.31.5.227',  '172.31.10.29', '172.31.1.175', '172.31.10.130',]


for ip in list_mgmt:
    client.connect(ip, username='centos', password=None, key_filename='~/.aws/vdi-pc.pem')

    stdin, stdout, stderr = client.exec_command('/bin/rm -rf /var/tmp/*')

    lines = stdout.readlines()
    print (''.join(lines))
    print ('-' * 80)

    client.close()
