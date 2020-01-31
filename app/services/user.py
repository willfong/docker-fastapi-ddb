import hashlib
from ..db import aws
from ..services import util


def find_or_create_user(oauth_source, user_id, oauth_payload):
    user_plaintext = f"{oauth_source}|{user_id}"
    user_hash = hashlib.sha224(user_plaintext.encode('ascii')).hexdigest()
    if aws.ddb_users_find_create(user_hash, oauth_source, oauth_payload):
        return user_hash
    else:
        util.logger.error("Error with creating user in DDB")
        return False
