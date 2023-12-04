import boto3

client = boto3.client('ec2')

conn = boto3.resource('ec2')
instances = conn.instances.filter()
for instance in instances:
    if instance.state["Name"] == "running":
       print (instance.id, instance.instance_type, region, instance.tags)
