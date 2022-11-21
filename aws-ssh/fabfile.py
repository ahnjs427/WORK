#! /usr/bin/env python

from fabric.api import env, local, roles, run, sudo, execute

env.user = 'centos'
env.key_filename = '~/.aws/vdi-pc.pem'
env.roledefs = {
    'MGMT' : [ '172.31.5.171',  '172.31.14.192', ],

    'TD'   : [ '172.31.9.147',  '172.31.12.251', '172.31.0.249' ],

    'FARM' : [ '172.31.4.220',  '172.31.3.46',  '172.31.9.132',  '172.31.15.134', '172.31.1.192', 
               '172.31.1.192',  '172.31.15.45', '172.31.0.255',  '172.31.1.86',   '172.31.0.172' 
             ],


    'VDI'  : [ '172.31.11.228', '172.31.3.20',  '172.31.10.171', '172.31.15.209', '172.31.14.249', '172.31.5.227',
               '172.31.10.29', '172.31.1.175',  '172.31.10.130',
             ],

    'AHN'  : [ '172.31.0.249' ],
}


@roles('VDI')
def install_NodeExporter():
    run('sudo useradd -M -s /bin/bash prometheus_node-exporter')
    run('sudo cp -rvf /netapp/data/Applications/prometheus/NodeExporter/node_exporter-1.4.0 /opt/')
    run('sudo cp -rvf /netapp/data/Applications/prometheus/NodeExporter/node_exporter.service /etc/systemd/system/')
    run('sudo systemctl daemon-reload')
    run('sudo systemctl start node_exporter')
    run('sudo systemctl enable node_exporter')
    




