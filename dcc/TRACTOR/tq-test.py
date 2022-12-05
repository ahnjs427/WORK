#!/usr/bin/env python

import time
import tractor.api.query as tq
import boto3

active_jobs = tq.jobs("active", columns=["title"])

nuke_job = '[NUKE]'
katana_job = '(KAT)'
result_list = []

for active_jobs_obj in active_jobs:
    string = (active_jobs_obj['title'])
    result_list.append(string.split(' ')[0])

# 2D-Farm ShutDown Sequence
if not nuke_job in result_list:
    time.sleep(180)
    if not nuke_job in result_list:
        ec2 = boto3.resource('ec2', region_name='ap-northeast-2')
        filters = [{'Name': 'tag:Name', 'Values': ['Renderfarm-*']}]
        instances = ec2.instances.filter(Filters=filters)

        running_instance_list = []

        for instance in instances:
            if instance.state['Name'] == 'running':
                running_instance_list.append(instance.id)
                # ec2.stop_instances(InstanceIds=running_instance_list)
        
if active_jobs:
    pass
