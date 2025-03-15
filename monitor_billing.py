import boto3
from datetime import datetime, timedelta

# Initialize Cost Explorer client
ce = boto3.client('ce')

def get_aws_cost(start_date, end_date):
    try:
        response = ce.get_cost_and_usage(
            TimePeriod={
                'Start': start_date,
                'End': end_date
            },
            Granularity='DAILY',
            Metrics=['UnblendedCost']
        )

        print("\n✅ AWS Cost Usage:")
        for result in response['ResultsByTime']:
            date = result['TimePeriod']['Start']
            cost = result['Total']['UnblendedCost']['Amount']
            print(f"📅 {date}: ${cost}")

    except Exception as e:
        print("\n❌ Error retrieving cost data:", str(e))

if __name__ == "__main__":
    end_date = datetime.today().strftime('%Y-%m-%d')
    start_date = (datetime.today() - timedelta(days=7)).strftime('%Y-%m-%d')
    get_aws_cost(start_date, end_date)
