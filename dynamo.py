import boto3
from datetime import datetime, timedelta

# Initialize DynamoDB resource
session = boto3.Session(profile_name='bookie-bot')
dynamodb = session.resource('dynamodb', region_name="us-east-1")

# DynamoDB table name
table_name = 'NFL_odds'

# Reference the table
table = dynamodb.Table(table_name)


def insert_into_dynamodb(gameID, timestamp, c_time, bookmaker, home_team, away_team, home_ML, away_ML, home_spread, away_spread, h_spreadPrice, a_spreadPrice):
    try:
        response = table.put_item(
            Item={
                'GameID': gameID,
                'SortKey': f"{bookmaker}#{timestamp}",
                'Game Time': c_time,
                'HomeTeam': home_team,
                'AwayTeam': away_team,
                'HomeML': home_ML,
                'AwayML': away_ML,
                'HomeSpread': home_spread,
                'AwaySpread': away_spread,
                'HomeSprOdds': h_spreadPrice,
                'AwaySprOdds': a_spreadPrice
            }
        )
        print("PutItem succeeded:", response)
    except Exception as e:
        print("Error inserting into DynamoDB:", e)


def cleanup():
    six_days_ago = datetime.now() - timedelta(days=6)

    # Scan the table
    response = table.scan()
    for item in response['Items']:
        # Extract timestamp from the composite sort key
        sort_key = item['SortKey']
        bookmaker, timestamp_str = sort_key.split("#")
        item_timestamp = datetime.strptime(timestamp_str, '%Y-%m-%d %H:%M:%S')  # Adjust the format

        if item_timestamp < six_days_ago:
            table.delete_item(
                Key={
                    'YourPrimaryKey': item['YourPrimaryKey'],
                    'SortKey': sort_key
                }
            )
