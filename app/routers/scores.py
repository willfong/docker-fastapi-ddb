from fastapi import APIRouter
from ..ddb import DecimalEncoder, GameScores

# Put these imports into ddb
import json
from botocore.exceptions import ClientError

router = APIRouter()

@router.get("/")
async def read_items():
    try:
        response = GameScores.get_item(
            Key={
                'UserID': 'will'
            }
        )
    except ClientError as e:
        print(e.response['Error']['Message'])
    else:
        item = response['Item']
        print("GetItem succeeded:")
        print(json.dumps(item, indent=4, cls=DecimalEncoder))
        return item

@router.get("/put")
async def put_items():
    try:
        response = GameScores.put_item(
            Item={
                'UserID': 'will',
                'GameTitle': 'Overwatch',
            }
        )
    except ClientError as e:
        print(e.response['Error']['Message'])
    else:
        return {"Hello": "World"}