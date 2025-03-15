import boto3

# Initialize S3 client
s3 = boto3.client('s3')

def list_s3_buckets():
    try:
        response = s3.list_buckets()
        buckets = [bucket['Name'] for bucket in response['Buckets']]

        if buckets:
            print("\n✅ S3 Buckets Found:")
            for bucket in buckets:
                print(f"- {bucket}")
        else:
            print("\n⚠️ No S3 buckets found.")

    except Exception as e:
        print("\n❌ Error retrieving S3 buckets:", str(e))

if __name__ == "__main__":
    list_s3_buckets()
