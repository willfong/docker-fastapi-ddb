import jwt
from datetime import datetime, timedelta
from fastapi import APIRouter
from pydantic import BaseModel
from ..services import user, util

router = APIRouter()

class LoginToken(BaseModel):
    value: str

def create_login_token(sub):
    token = jwt.encode({
        'sub': sub,
        'iat': datetime.utcnow(),
        'exp': datetime.utcnow() + timedelta(minutes=30)},
        util.get_secret_token())
    return token


@router.post("/facebook")
def login_facebook(token: LoginToken):
    facebook_data = user.facebook_verify_access_token(token.value)
    util.logger.warning(f"facebook data: {facebook_data}")
    user_id = user.find_or_create_user('facebook', facebook_data['user_id'], facebook_data)
    if user_id:
        return create_login_token(user_id)
    else:
        return {"error": "could not log in"}


@router.post("/google")
def login_google(token: LoginToken):
    google_data = user.google_verify_access_token(token.value)
    util.logger.warning(google_data)
    user_id = user.find_or_create_user('google', google_data['sub'], google_data)
    if user_id:
        return create_login_token(user_id)
    else:
        return {"error": "could not log in"}
