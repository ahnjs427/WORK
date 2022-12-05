#!/usr/bin/env python3.9

import boto3
import time

ec2 = boto3.client('ec2', region_name='ap-northeast-2')


groupDCV = ['i-0b2fbdf3602807d28',
             'i-0f7375d22aa29ed32',
             'i-09a97b01606de4b71',
            #  'i-08f0191d84289ddff',
             'i-0b2c8981b686fdb5f',
             'i-0e3d56c121c36294a',
             'i-0922dc46e95339f2b',
             'i-069b14073a2e65356',
             'i-0918baf2bacf3740c',
            ]

groupFARM_01 = ['i-0adc529bbe14bd1d7', 'i-0bd160a64359c65b1', 'i-0222307a6c89a2665', 'i-0fb59d0ee3b63ace7', 'i-0aedf0d4ccad67be9']
groupFARM_02 = ['i-02fb5214cc7987e7c', 'i-055cb465edf16a9f3',]
groupFARM_03 = ['i-0e5dae3bd6798946a', 'i-06e98657b134ddc02', 'i-0cd5a30b9582e8b88', 'i-0e7a7ba97c213da3b', 'i-07349bc418f4529b8']

# start VDI - g4dn Family
# ec2.start_instances(InstanceIds=groupDCV)


# start FARM - c4 Family
# ec2.start_instances(InstanceIds=groupFARM_02)
while True:
    try: 
        ec2.start_instances(InstanceIds=groupFARM_02)
    except:
        pass
        print('retry...')
        time.sleep(60.0)
    else:
        print('success!')
    


# 'i-0a00b4e240c5d8a24', 'i-0291ec33eeac9052b', 'i-06be0e7d5e462dc96'