#! /usr/bin/env python

from fabric.api import env, local, roles, run, sudo, execute

env.user = 'centos'
env.key_filename = '~/.aws/vdi-pc.pem'
env.roledefs = {
    'MGMT' : [ '172.31.5.171',  '172.31.14.192', ],

    'TD'   : [ '172.31.9.147',  '172.31.12.251', ],

    'FARM' : [ '172.31.4.220',  '172.31.3.46',  '172.31.9.132',  '172.31.15.134', '172.31.1.192', 
               '172.31.1.192',  '172.31.15.45', '172.31.0.255',  '172.31.1.86',   '172.31.0.172' 
             ],


    'VDI'  : [ '172.31.11.228', '172.31.3.20',  '172.31.10.171', '172.31.15.209', '172.31.14.249', 
               '172.31.5.227',  '172.31.10.29', '172.31.1.175',  '172.31.10.130', '172.31.9.147',
             ],
}


@roles('FARM')
def script_farm():
    run('sudo tar -xzf /tmp/genarts.tar.gz -C /usr/')
   
 
@roles('VDI')
def script_vdi():
    run('nvidia-smi')



