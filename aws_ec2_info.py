import boto3

ec2 = boto3.resource('ec2')
rds = boto3.client('rds')
classic_address = ec2.ClassicAddress('public_ip')
for r in ec2.instances.all():
  for tag in r.tags:
    print tag['Value'],'','|','',r.network_interfaces_attribute
