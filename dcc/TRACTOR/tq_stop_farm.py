#!/usr/bin/env python

import time
import tractor.api.query as tq
import boto3

ec2 = boto3.resource('ec2', region_name='ap-northeast-2')
filters = [{'Name': 'tag:Name', 'Values': ['Renderfarm-*']}]
instances = ec2.instances.filter(Filters=filters)
running_instance_list = []

active_jobs = tq.jobs("active", columns=["title"])
nuke_job = '[NUKE]'
katana_job = '(KAT)'
result_list = []

for dict_obj in active_jobs:
    string = (dict_obj['title'])
    result_list.append(string.split(' ')[0])

# 3D-Farm Start ShutDown Sequence
if not katana_job in result_list:
    time.sleep(300)
    if not katana_job in result_list:
        for instance in instances:
            if instance.state['Name'] == 'running':
                running_instance_list.append(instance.id)

        # ec2.stop_instances(InstanceIds=running_instance_list)
        # ec2.Instance(running_instance_list).stop()

        for i in running_instance_list:
            ec2.Instance(i).stop()





    


    



    

    


    

