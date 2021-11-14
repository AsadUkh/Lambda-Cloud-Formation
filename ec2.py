import boto3
instance_name_to_terminaite = 'testing-123'
region='eu-west-1'
ec2 = boto3.resource('ec2',region_name=region)
ec2_client = boto3.client('ec2')
instances = ec2.instances.filter(Filters=[{'Name': 'instance-state-name', 'Values': ['stopped']} , {'Name':'tag:Name', 'Values':[instance_name_to_terminaite]}])
instance_ids = []

for instance in instances:
   print(instance.id, instance.instance_type)

for instance in instances:
    instance_ids.append(instance.id)

#ec2_client .stop_instances(InstanceIds=instance_ids)

#for instance in instances:
#   print(instance.id, instance.instance_type)