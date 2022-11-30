#! /usr/bin/python3

import time
import boto3

region = 'ap-northeast-2'
ec2 = boto3.client('ec2', region_name=region)
instances = [
             'i-0adc529bbe14bd1d7',         #renderfarm-01
            #  'i-0bd160a64359c65b1',         #renderfarm-02
            #  'i-0222307a6c89a2665',         #renderfarm-03
            #  'i-0fb59d0ee3b63ace7',         #renderfarm-04
             'i-0aedf0d4ccad67be9',         #renderfarm-05

             'i-0b2fbdf3602807d28',         #VDI-PC-01
             'i-0f7375d22aa29ed32',         #VDI-PC-02
             'i-09a97b01606de4b71',         #VDI-PC-03
            #  'i-08f0191d84289ddff',         #VDI-PC-04
             'i-0b2c8981b686fdb5f',         #VDI-PC-05
             'i-0e3d56c121c36294a',         #VDI-PC-06
             'i-0922dc46e95339f2b',         #VDI-PC-07
             'i-069b14073a2e65356',         #VDI-PC-08
             'i-0918baf2bacf3740c',         #VDI-PC-09

            #  'i-06fa2924c38b72379',     #VDI-PC-10 : TD-a
            #  'i-04adda334f488ea0b',     #VDI-PC-11 : TD-b
            #  'i-04532fbb62e9a474d',     #VDI-PC-12 : TD-c
            #  'i-0ff37626bf86d68df',     #VDI-PC-13 : for NUKE & HIERO
            #  'i-06da6ceca7113d60d',     #VDI-PC-14 : Omniverse-windows

            #  'i-0a5d83de33c0462cf',     #Omniverse-Nucleus
            ]

ec2.start_instances(InstanceIds=instances)