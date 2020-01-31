import os
import boto3
from botocore.exceptions import ClientError
from ..services import util


ddb = boto3.resource('dynamodb', region_name=os.environ.get('AWS_REGION_NAME'), endpoint_url=os.environ.get('DDB_ENDPOINT_URL'))

ddb_users = ddb.Table('Users')

def ddb_users_find_create(user_hash, oauth_source, oauth_payload):
    util.logger.warning(user_hash)
    util.logger.warning(oauth_source)
    util.logger.warning(oauth_payload)

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
        print(e.response['Error']['Message'])
        return False
    
    return True