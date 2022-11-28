#!/usr/bin/env python

from __future__ import print_function

import subprocess
import influxdb_client, os, time
from influxdb_client import InfluxDBClient, Point, WritePrecision
from influxdb_client.client.write_api import SYNCHRONOUS

token = os.environ.get("INFLUXDB_TOKEN")
org = "oasys-org"
bucket="oasys-bucket"
url = "http://172.31.14.192:8086"

client = influxdb_client.InfluxDBClient(url=url, token=token, org=org)
write_api = client.write_api(write_options=SYNCHRONOUS)



for value in range(5):
  point = (Point("measurement1").tag("tagname1", "tagvalue1").field("field1", value))
  write_api.write(bucket=bucket, org="oasys-org", record=point)
  
  time.sleep(1)



