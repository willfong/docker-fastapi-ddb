import os
import requests
import logging

logger = logging.getLogger(__name__)
myFormatter = logging.Formatter('[%(asctime)s] [%(levelname)s] %(message)s')
handler = logging.StreamHandler()
handler.setFormatter(myFormatter)
logger.addHandler(handler)


def get_secret_token():
    # TODO: Obviously, this should be updated to AWS KMS
    return 'SECRET_TOKEN_HERE'

def verify_token(token):  
    try: 
        jwt.decode(token, get_secret_token())
    except:
        print('bad token')
        return False
    return True
