#! /usr/bin/env python

from fabric.api import env, local, run, sudo, execute

import random
import os
import json

env.user = 'centos'
env.hosts = [ '172.31.5.171', '172.31.14.192']
env.key_filename = '~/.aws/vdi-pc.pem'

def remove_tmp():
    sudo('rm -rf /tmp/*')

# def uptime():
#     run('uptime')

# def deploy():
#     execute(hostname)
#     execute(uptime)



