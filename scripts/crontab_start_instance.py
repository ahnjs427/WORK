#! /usr/local/bin/python3.9

import time
import boto3

region = 'ap-northeast-2'
ec2 = boto3.client('ec2', region_name=region)

instances_vdi = [
             'i-0b2fbdf3602807d28',         #VDI-PC-01
             'i-0f7375d22aa29ed32',         #VDI-PC-02
             'i-09a97b01606de4b71',         #VDI-PC-03
            #  'i-08f0191d84289ddff',         #VDI-PC-04
             'i-0b2c8981b686fdb5f',         #VDI-PC-05
             'i-0e3d56c121c36294a',         #VDI-PC-06
             'i-0922dc46e95339f2b',         #VDI-PC-07
             'i-069b14073a2e65356',         #VDI-PC-08
             'i-0918baf2bacf3740c',         #VDI-PC-09
]

instances_farm = [ 
             'i-0adc529bbe14bd1d7',         #renderfarm-01
             'i-0bd160a64359c65b1',         #renderfarm-02
             'i-0222307a6c89a2665',         #renderfarm-03
             'i-0fb59d0ee3b63ace7',         #renderfarm-04
             'i-0aedf0d4ccad67be9',         #renderfarm-05
             'i-02fb5214cc7987e7c',
             'i-055cb465edf16a9f3',
             'i-0a00b4e240c5d8a24',
             'i-0291ec33eeac9052b',
             'i-06be0e7d5e462dc96',
             'i-0e5dae3bd6798946a',
             'i-06e98657b134ddc02',
             'i-0cd5a30b9582e8b88',
             'i-0e7a7ba97c213da3b',
             'i-07349bc418f4529b8',
]
# start VDI - g4dn Family
ec2.start_instances(InstanceIds=instances_vdi)

# start FARM - c4 Family

while True:
    time.sleep(60)
    try:
        print('try...')
        ec2.start_instances(InstanceIds=instances_farm)
    except Exception as e:
        print(e)
    else:
        print('Success!')
    finally:
        ec2.start_instances(InstanceIds=instances_farm)
        print('Retry...')
    