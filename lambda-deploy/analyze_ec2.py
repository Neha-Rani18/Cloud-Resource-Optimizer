import boto3
from datetime import datetime, timedelta
import subprocess
import json

def lambda_handler(event, context):
    ec2_client = boto3.client('ec2')
    cloudwatch_client = boto3.client('cloudwatch')
    
    # Fetch all instances
    instances = ec2_client.describe_instances()
    underutilized_instances = []
    
    for reservation in instances['Reservations']:
        for instance in reservation['Instances']:
            instance_id = instance['InstanceId']
            end_time = datetime.utcnow()
            start_time = end_time - timedelta(days=1)
            
            cpu_utilization = cloudwatch_client.get_metric_statistics(
                Period=86400,
                StartTime=start_time,
                EndTime=end_time,
                MetricName='CPUUtilization',
                Namespace='AWS/EC2',
                Statistics=['Average'],
                Dimensions=[
                    {'Name': 'InstanceId', 'Value': instance_id}
                ]
            )
            
            # Check if CPU utilization is consistently low
            avg_cpu = sum([point['Average'] for point in cpu_utilization['Datapoints']]) / max(len(cpu_utilization['Datapoints']), 1)
            
            if avg_cpu < 10:  # Assuming <10% CPU usage means underutilized
                underutilized_instances.append(instance_id)
                print(f"Instance {instance_id} is underutilized with avg CPU: {avg_cpu}%")
    
    # Trigger stop_low_usage_ec2.py with the list of underutilized instances
    if underutilized_instances:
        try:
            subprocess.run(['python', 'stop_low_usage_ec2.py'] + underutilized_instances, check=True)
        except subprocess.CalledProcessError as e:
            print(f"Error stopping instances: {e}")
    
    return {
        'statusCode': 200,
        'body': {'underutilized_instances': underutilized_instances}
    }

if __name__ == "__main__":
    # Mock event and context for local testing
    event = {}
    context = type('obj', (object,), {'timestamp': datetime.utcnow()})
    lambda_handler(event, context)