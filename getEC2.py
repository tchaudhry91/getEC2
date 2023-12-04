import boto3

client = boto3.client('ec2')

import sys

region = sys.argv[1]

conn = boto3.resource('ec2', region=region)
instances = conn.instances.filter(region=region)
for instance in instances:
    if instance.state["Name"] == "running":
       print (instance.id, instance.instance_type, region, instance.tags)
