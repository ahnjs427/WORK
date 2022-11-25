#!/usr/bin/env python

import boto3

ec2 = boto3.resource('ec2', region_name='ap-northeast-2')
filters = [{'Name': 'tag:Name', 'Values': ['Renderfarm-01', 'Renderfarm-02', 'Renderfarm-03', 'Renderfarm-04']}]
instances = ec2.instances.filter(Filters=filters)
running_instance_list = []

for instance in instances:
    if instance.state['Name'] == 'running':
        running_instance_list.append(instance.id)

for i in running_instance_list:
    print(i)



# 'Name': 'instance-state-name',
#         'Values': ['running'],