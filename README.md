# Cloud Resource Optimizer

## Overview
Cloud Resource Optimizer is an AWS Lambda-based solution that monitors EC2 instances and automatically stops low-usage instances to optimize cloud costs.

## Features
- **Monitor EC2 Usage**: It gets the CPU usage from AWS CloudWatch
- **Stop Low-Usage Instances**: Automatically stops under-utilized instances that have low CPU usage.
- **Scheduled Execution**: Uses Amazon EventBridge Scheduler to run every 3 days.
- **Cost Optimization**: Reduces unnecessary cloud resource usage by stopping low CPU usage instances.

## Prerequisites
- AWS account with IAM permissions.
- Python 3.x installed.
- AWS CLI configured.

## Setup Instructions

### 1. Configure AWS Credentials
Run the following command to set up AWS credentials:
```sh
aws configure
```
Enter:
- **AWS Access Key ID**
- **AWS Secret Access Key**
- **Default Region** (e.g., `us-east-1`)
- **Output Format** (`json` or leave blank)

Alternatively, set environment variables:
```sh
export AWS_ACCESS_KEY_ID=your_access_key
export AWS_SECRET_ACCESS_KEY=your_secret_key
export AWS_DEFAULT_REGION=your_region
```

### 2. Install Dependencies
Navigate to the project folder and install required Python libraries:
```sh
pip install -r requirements.txt -t .
```

### 3. Package and Deploy to AWS Lambda
Zip your project files:
```sh
zip -r lambda_package.zip .
```
Upload the **lambda_package.zip** to AWS Lambda and set up the handler function accordingly.

### 4. Configure IAM Role
Create an IAM role with these policies:
- `AmazonEC2FullAccess`
- `CloudWatchReadOnlyAccess`
- `AmazonS3ReadOnlyAccess` (if needed)

Attach this role to your Lambda function.

### 5. Set Up EventBridge Scheduler
To run the function every 3 days:
- Go to **Amazon EventBridge** → **Scheduler**.
- Create a new schedule with **cron expression**: `rate(3 days)`.
- Set the target as your Lambda function.

## Testing
- Manually invoke the Lambda function from the AWS console.
- Check logs in **Amazon CloudWatch**.
- Verify stopped instances in **EC2 Dashboard**.

## Contributing
Feel free to submit issues or pull requests to improve this project!


