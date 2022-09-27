#!/usr/bin/env python

import os, time
from pprint import pprint

import tractor.api.query as tq
import boto3


jobs = tq.jobs("active or ready")
# pprint (jobs)

# One Cicle
if not jobs:
    print("list is empty")
    time.sleep(120)
    if not jobs: #shutdown
        print("list is empty")
        
        ec2 = boto3.resource('ec2', region_name = 'ap-northeast-2')
        filters = [{'Name': 'tag:Name', 'Values': ['Renderfarm-*']}]
        instances = ec2.instances.filter(Filters=filters)
        
        running_instance_list = []

        for instance in instances:
            if instance.state['Name'] == 'running':
                running_instance_list.append(instance.id)
                
        print(type(running_instance_list))
        print(len(running_instance_list))
                
        #  ec2.stop_instances(InstanceIds=running_instance_list)

if jobs: #pass
    print("list is not empty")
