import boto3
import logging
from pythonjsonlogger import jsonlogger
import datetime

# Logger configuration
logger = logging.getLogger("K8S REPORTS")
logHandler = logging.StreamHandler()
formatter = jsonlogger.JsonFormatter()
logHandler.setFormatter(formatter)
logger.addHandler(logHandler)
logger.setLevel(logging.INFO)

# Boto3 EC2 client
ec2 = boto3.client('ec2')

# Getting information about instances
response = ec2.describe_instances(
    Filters=[
        {'Name': 'instance-state-code', 'Values': ['16']},
        {'Name': 'tag:k8s.io/role/master', 'Values': ['1']}
    ]
)

# Extract instance information
instances = []
for reservation in response['Reservations']:
    for instance in reservation['Instances']:
        instances.append(instance)

# Logging the instance information
for i, instance in enumerate(instances, start=1):
    instance_id = instance['InstanceId']
    instance_ip = instance.get('PublicIpAddress', 'No IP')
    instance_name = next((tag['Value'] for tag in instance['Tags'] if tag['Key'] == 'Name'), 'Unnamed')
    log_message = {
        "threadName": "MainThread",
        "name": "K8S REPORTS",
        "time": datetime.datetime.now().isoformat(),
        "Running clusters": len(instances),
        f"CLUSTER {i} IP": instance_ip,
        "CLUSTER NAME": instance_name,
        "msecs": logger.handlers[0].formatter.converter(time.time()) % 1000,
        "message": f"Instance ID: {instance_id}, Instance Name: {instance_name}",
        "levelname": "INFO",
    }
    logger.info(log_message)
