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
