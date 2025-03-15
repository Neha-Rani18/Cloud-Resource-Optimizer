import boto3

# Test S3 access
s3 = boto3.client('s3')

try:
    response = s3.list_buckets()
    print("✅ AWS Credentials are working!")
    print("Available Buckets:", [bucket['Name'] for bucket in response['Buckets']])
except Exception as e:
    print("❌ AWS Credentials are not set up properly:", str(e))
