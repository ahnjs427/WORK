#! /usr/bin/env python

import boto3

region = 'ap-northeast-2'
ec2 = boto3.client('ec2', region_name=region)
instances = [
             'i-02c293acaa8253742', #renderfarm-01
             'i-03f387e9c9503fc5d', #renderfarm-02
             'i-0ac71f3ffd78d2750', #renderfarm-03
             'i-0d0c316658c280adf', #renderfarm-04
             'i-0aedf0d4ccad67be9', #renderfarm-05

            #  'i-0be26d79a116550fa', #renderfarm-06
            #  'i-06397cdf3a487dfe8', #renderfarm-07
            #  'i-0d2039f72b6687486', #renderfarm-08
            #  'i-00e10328ca778ad28', #renderfarm-09
            #  'i-01ac193a3acd19b60', #renderfarm-10
            #  'i-08f17a25d6c4a9a2b', #renderfarm-11
            #  'i-037e94c8d9422c220', #renderfarm-12
            #  'i-06303d55f344e3177', #renderfarm-13
            #  'i-0fb21a760bf7ef5e2', #renderfarm-14
            #  'i-098f0b5361e635f2a', #renderfarm-15

             'i-0b2fbdf3602807d28', #VDI-PC-01
             'i-0f7375d22aa29ed32', #VDI-PC-02
             'i-09a97b01606de4b71', #VDI-PC-03
            #  'i-08f0191d84289ddff', #VDI-PC-04
             'i-0b2c8981b686fdb5f', #VDI-PC-05
            #  'i-0e3d56c121c36294a', #VDI-PC-06
             'i-0922dc46e95339f2b', #VDI-PC-07
             'i-069b14073a2e65356', #VDI-PC-08
             'i-0918baf2bacf3740c', #VDI-PC-09
             'i-06fa2924c38b72379', #VDI-PC-10:TD-a
             'i-04adda334f488ea0b', #VDI-PC-11:TD-b
             'i-071e56668382094e2', #VDI-Windows-PTgui
            ]
ec2.start_instances(InstanceIds=instances)


