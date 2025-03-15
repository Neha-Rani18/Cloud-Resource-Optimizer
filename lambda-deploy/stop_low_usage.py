import boto3
import sys

def stop_instances(instance_ids):
    ec2_client = boto3.client('ec2')
    try:
        ec2_client.stop_instances(InstanceIds=instance_ids)
        print(f"Successfully stopped instances: {instance_ids}")
    except Exception as e:
        print(f"Error stopping instances: {e}")

if __name__ == "__main__":
    if len(sys.argv) > 1:
        instance_ids = sys.argv[1:]
        stop_instances(instance_ids)
    else:
        print("No instance IDs provided.")