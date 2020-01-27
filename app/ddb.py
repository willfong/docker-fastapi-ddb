import os
import boto3
import json
import decimal
from botocore.exceptions import ClientError

class DecimalEncoder(json.JSONEncoder):
    def default(self, o):
        if isinstance(o, decimal.Decimal):
            if o % 1 > 0:
                return float(o)
            else:
                return int(o)
        return super(DecimalEncoder, self).default(o)

dynamodb = boto3.resource('dynamodb', region_name=os.environ.get('AWS_REGION_NAME'), endpoint_url=os.environ.get('DDB_ENDPOINT_URL'))

GameScores = dynamodb.Table('GameScores')

'''
import boto3

dynamodb = boto3.resource('dynamodb', region_name='us-west-2', endpoint_url="http://localhost:8000")


table = dynamodb.create_table(
    TableName='GameScores',
    KeySchema=[
        {
            'AttributeName': 'UserID',
            'KeyType': 'HASH'  #Partition key
        },
        {
            'AttributeName': 'GameTitle',
            'KeyType': 'RANGE'  
        },
    ],
    AttributeDefinitions=[
        {
            'AttributeName': 'UserID',
            'AttributeType': 'S'
        },
        {
            'AttributeName': 'GameTitle',
            'AttributeType': 'S'
        },
    ],
    ProvisionedThroughput={
        'ReadCapacityUnits': 10,
        'WriteCapacityUnits': 10
    }
)

print("Table status:", table.table_status)
'''