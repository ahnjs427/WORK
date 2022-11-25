#! /usr/bin/env python

from fabric.api import env, local, roles, run, sudo, execute

env.user = 'centos'
env.key_filename = '~/.aws/vdi-pc.pem'
env.roledefs = {
    'MGMT' : [ '172.31.5.171',  '172.31.14.192', ],

    'TD'   : [ '172.31.9.147',  '172.31.12.251', '172.31.0.249' ],

    'FARM' : [ '172.31.0.146', '172.31.6.112', '172.31.5.61', '172.31.2.186', '172.31.1.192'
             ],


    'VDI'  : [ '172.31.11.228', '172.31.3.20', '172.31.10.171', '172.31.15.209', '172.31.14.249', 
               '172.31.5.227',
               '172.31.10.29', '172.31.1.175', '172.31.10.130',
             ],

    'AHN'  : [ '172.31.0.249' ],
}


@roles('VDI')
def stopNodeexpoter():
    run('sudo systemctl stop node_exporter')
    run('sudo systemctl disable node_exporter')

    




