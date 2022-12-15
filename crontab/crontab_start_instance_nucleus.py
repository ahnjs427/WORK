#!/usr/bin/env python3

import boto3
import time

ec2 = boto3.client('ec2', region_name='ap-northeast-2')

nucleus = ['i-0a5d83de33c0462cf',]




# start FARM - c4 Family
while True:
    try: 
        ec2.start_instances(InstanceIds=nucleus)
    except Exception as e:
        pass
        print(e, '\033[31m' + 'retry....' + '\033[0m')
        time.sleep(60.0)
    else:
        print('\033[31m' + 'success!!' + '\033[0m')
        break
