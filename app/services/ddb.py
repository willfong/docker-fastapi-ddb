import os
import boto3
from botocore.exceptions import ClientError
from ..services import util


dynamodb = boto3.resource('dynamodb', region_name=os.environ.get('AWS_REGION_NAME'), endpoint_url=os.environ.get('DDB_ENDPOINT_URL'))

USERS = dynamodb.Table('Users')
MESSAGES = dynamodb.Table('Messages')


def upsert(table, key, expression, values):
    try:
        table.update_item(
            Key=key, 
            UpdateExpression=expression,
            ExpressionAttributeValues=values,
        )
    except ClientError as e:
        util.logger.error(f"[UPSERT|{table}|{key}] {e}")
        return False
    return True

def put(table, item):
    try:
        table.put_item(Item=item)
    except ClientError as e:
        util.logger.error(f"[PUT|{table}|{item}] {e}")
        return False
    return True


def scan(table, sort=None):
    try:
        response = table.scan()
        data = response['Items']
        while 'LastEvaluatedKey' in response:
            response = table.scan(ExclusiveStartKey=response['LastEvaluatedKey'])
            data.extend(response['Items'])
    except ClientError as e:
        util.logger.error(f"[SCAN|{table}] {e}")
        return False
    if sort:
        data.sort(key=lambda x: x[sort], reverse=True)
    return data

def get(table, key):
    try: 
        response = table.get_item(Key=key)
    except ClientError as e:
        util.logger.error(f"[GET|{table}|{key}] {e}")
        return False
    return response['Item']
