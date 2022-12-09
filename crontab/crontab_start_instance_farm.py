#!/usr/bin/env python3

import boto3
import time

ec2 = boto3.client('ec2', region_name='ap-northeast-2')

groupFARM_01 = [ 'i-0adc529bbe14bd1d7', 'i-0bd160a64359c65b1', 'i-0222307a6c89a2665', 'i-0fb59d0ee3b63ace7', 'i-0aedf0d4ccad67be9' ]
groupFARM_02 = [ 'i-02fb5214cc7987e7c', 'i-055cb465edf16a9f3', 'i-0a00b4e240c5d8a24', 'i-0291ec33eeac9052b', 'i-06be0e7d5e462dc96' ]
groupFARM_03 = [ 'i-0291ec33eeac9052b', 'i-06be0e7d5e462dc96', 'i-0e5dae3bd6798946a', 'i-06e98657b134ddc02', 'i-0cd5a30b9582e8b88' ]


# start FARM - c4 Family
while True:
    try: 
        ec2.start_instances(InstanceIds=groupFARM_01)
    except Exception as e:
        pass
        print(e, '\033[31m' + 'retry....' + '\033[0m')
        time.sleep(60.0)
    else:
        print('\033[31m' + 'success!!' + '\033[0m')
        break