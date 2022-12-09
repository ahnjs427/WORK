#!/usr/bin/env python3

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

# start VDI - g4dn Family
ec2.start_instances(InstanceIds=groupDCV)