#! /usr/bin/env python

from fabric.api import env, local, roles, run, sudo, execute

env.user = 'centos'
env.key_filename = '~/.aws/vdi-pc.pem'
env.roledefs = {
    'MGMT' : [ '172.31.5.171',  '172.31.14.192', ],

    'TD'   : [ '172.31.9.147',  '172.31.12.251', ],

    'FARM' : [ '172.31.4.220',  '172.31.3.46', '172.31.9.132',  '172.31.15.134', '172.31.1.192', ],

    'VDI'  : [ '172.31.11.228', '172.31.3.20',  '172.31.10.171', '172.31.15.209', '172.31.14.249',
               '172.31.5.227',  '172.31.10.29', '172.31.1.175',  '172.31.10.130', ]
}

@roles('FARM')
def mgmt_script():
    run('w')
    # run('/netapp/data/td/script/test-script.sh')
    
@roles('VDI')
def vdi_script():
    run('uptime')



    


