import boto3

rds = boto3.client('rds')
response        = rds.describe_db_instances()
instances       = response.get('DBInstances')

print 'Server Name | Server Address | Server Configuration | Server Engine | Server Status'

for i in instances:
   dbidentifier = i.get('DBInstanceIdentifier')
   dbinstanceclass = i.get('DBInstanceClass')
   dbendpoint = i.get('Endpoint')
   dbaddress = dbendpoint.get('Address')
   status = i.get('DBInstanceStatus')
   dbengine = i.get('Engine')
   dbversion = i.get ('EngineVersion')
   
   print   dbidentifier,'|',  dbaddress,'|',  dbinstanceclass,'|',  dbengine , dbversion,'|',  status
