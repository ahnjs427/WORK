#!/usr/bin/env python3

import boto3
import time

ec2 = boto3.client('ec2', region_name='ap-northeast-2')

one_off = ['i-02fb5214cc7987e7c', 'i-055cb465edf16a9f3', 'i-0a00b4e240c5d8a24', 'i-0291ec33eeac9052b', 'i-06be0e7d5e462dc96']




# start FARM - c4 Family
while True:
    try: 
        ec2.start_instances(InstanceIds=one_off)
    except Exception as e:
        pass
        print(e, '\033[31m' + 'retry....' + '\033[0m')
        time.sleep(60.0)
    else:
        print('\033[31m' + 'success!!' + '\033[0m')
        break
