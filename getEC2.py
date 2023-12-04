import boto3
import sys

region = sys.argv[1]

print("Region:" + region)

client = boto3.client('ec2', region_name=region)

conn = boto3.resource('ec2', region_name=region)
instances = conn.instances.filter()
for instance in instances:
    if instance.state["Name"] == "running":
       print (instance.id, instance.instance_type, region, instance.tags)
