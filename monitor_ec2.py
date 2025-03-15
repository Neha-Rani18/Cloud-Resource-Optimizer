import boto3

# Initialize EC2 client
ec2 = boto3.client('ec2', region_name='eu-north-1')

def list_ec2_instances():
    try:
        response = ec2.describe_instances()
        instances = []

        for reservation in response['Reservations']:
            for instance in reservation['Instances']:
                instances.append({
                    'Instance ID': instance['InstanceId'],
                    'State': instance['State']['Name'],
                    'Type': instance['InstanceType'],
                    'Launch Time': instance['LaunchTime'].strftime('%Y-%m-%d %H:%M:%S'),
                    'Public IP': instance.get('PublicIpAddress', 'N/A'),
                })

        if instances:
            print("\n✅ EC2 Instances Found:")
            for instance in instances:
                print(instance)
        else:
            print("\n⚠️ No running EC2 instances found.")

    except Exception as e:
        print("\n❌ Error retrieving EC2 instances:", str(e))

if __name__ == "__main__":
    list_ec2_instances()
