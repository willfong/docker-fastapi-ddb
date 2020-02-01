import os
import boto3
from botocore.exceptions import ClientError
from ..services import util


ddb = boto3.resource('dynamodb', region_name=os.environ.get('AWS_REGION_NAME'), endpoint_url=os.environ.get('DDB_ENDPOINT_URL'))

ddb_users = ddb.Table('Users')
ddb_todos = ddb.Table('Todos')

def ddb_users_find_create(user_hash, oauth_source, oauth_payload):
    try:
        ddb_users.update_item(
            Key={
                'id': user_hash
            }, 
            UpdateExpression="SET oauth_source = :source, oauth_payload = :payload",
            ExpressionAttributeValues={
                ':source': oauth_source,
                ':payload': oauth_payload
            },
        )
    except ClientError as e:
        util.logger.error('[ddb_users_find_create] ' + e)
        return False
    return True


def ddb_todos_get_all():
    try:
        response = ddb_todos.scan()
    except ClientError as e:
        util.logger.error('[ddb_todos_get_all] ' + e)
        return False
    return response.get('Items')


def ddb_todos_add_todo(pid, dt, uid, todo):
    try:
        ddb_todos.put_item(
            Item={
                'id': pid,
                'datetime': dt,
                'users_id': uid,
                'todo': todo
            }
        )
    except ClientError as e:
        util.logger.error('[ddb_todos_add_todo] ' + e)
        return False
    return True
