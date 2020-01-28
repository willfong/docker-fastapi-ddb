from fastapi import APIRouter
from ..ddb import DecimalEncoder, GameScores
from ..log import logger

# Put these imports into ddb
import json
from botocore.exceptions import ClientError

router = APIRouter()

@router.get("/")
async def read_items():
    try:
        response = GameScores.get_item(
            Key={
                'UserID': 'will',
                'GameTitle': 'Overwatch'
            }
        )
    except ClientError as e:
        logger.error(e.response['Error']['Message'])
    else:
        item = response.get('Item')
        logger.debug("GetItem success")
        logger.debug(json.dumps(item, indent=4, cls=DecimalEncoder))
        return item

@router.get("/put")
async def put_items():
    try:
        GameScores.put_item(
            Item={
                'UserID': 'will',
                'GameTitle': 'Overwatch',
            }
        )
    except ClientError as e:
        logger.error(e.response['Error']['Message'])
    else:
        return {"msg": "Insert successful"}