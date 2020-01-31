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

def google_verify_access_token(id_token):
    # We're doing it the lazy way here. What we get from the client side is JWT, we can just verify that instead of calling Google
    # Reason for that is to reduce the amount of dependencies for this, a demo app
    # For production, we should do it the right way by using google-auth

    response = requests.get(f'https://oauth2.googleapis.com/tokeninfo?id_token={id_token}').json()
    if response.get('error'):
        print(response.get('error_description'))
        return response.get('error_description')
    # Here, you should check that your domain name is in hd
    # if jwt['hd'] == 'example.com':
    #   return jwt
    # For now, we're just going to accept all
    return response

