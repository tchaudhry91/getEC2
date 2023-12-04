import boto3
import sys

region = sys.argv[1]
print("Region:" + region)

session=boto3.Session(region_name=region) #boto3 session, aws profile 

ec2_resource=session.resource(service_name="ec2") # resource object method

'''
client object method, commented because this script using resource object method
ec2_client=session.client(service_name="ec2")
'''

#using Resource Object
'''
for each_instances in ec2_resource.instances.all():
    print(each_instances.id, each_instances.state['Name'])
'''

for instance in ec2_resource.instances.all():
     print(
            "Id: {0}\nPlatform: {1}\nType: {2}\nPublic IPv4: {3}\nAMI: {4}\nState: {5}\n".format(
         instance.id, instance.platform, instance.instance_type, instance.public_ip_address, instance.image.id, instance.state
         )
     )
