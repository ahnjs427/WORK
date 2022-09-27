#!/usr/bin/env python

import boto3

ec2 = boto3.resource('ec2', region_name='ap-northeast-2')

filters = [{'Name': 'tag:Name', 'Values': ['Renderfarm-*']}]

running_instance_list = []

instances = ec2.instances.filter(Filters=filters)

for instance in instances:
    if instance.state['Name'] == 'running':
        running_instance_list.append(instance.id)

print(type(running_instance_list))
print(len(running_instance_list))


# 'Name': 'instance-state-name',
#         'Values': ['running'],