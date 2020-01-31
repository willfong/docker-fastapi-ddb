import jwt
from datetime import datetime
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
        current_app.config['SECRET_KEY'])
    return token

@router.post("/facebook")
def login_facebook(token: LoginToken):

    return {"msg": "Hello, World!"}


'''
@blueprint.route("/login/google", methods=['POST'])
def google_login():
    access_token = request.json.get("accessToken")
    google_id = google_verify_access_token(access_token)
    user_id = google_find_or_create_user(google_id)
    token = jwt.encode({
        'user_id': user_id,
        'google_id': google_id,
        'iat': datetime.utcnow(),
        'exp': datetime.utcnow() + timedelta(minutes=30)},
        current_app.config['SECRET_KEY'])
    return jsonify({ 'token': token.decode('UTF-8') })
'''

@router.post("/google")
def login_google(token: LoginToken):
    google_data = util.google_verify_access_token(token.value)
    util.logger.warning(google_data)
    user_id = user.find_or_create_user('google', google_data['sub'], google_data)
    return {"user_id": user_id}


'''
{
  "iss": "accounts.google.com",
  "azp": "483971-j6lj9es15ghndu.apps.googleusercontent.com",
  "aud": "483971-j6lj9es15ghndu.apps.googleusercontent.com",
  "sub": "3838388818282828",
  "hd": "exmaple.com",
  "email": "will@example.com",
  "email_verified": true,
  "at_hash": "EyTRmWCeU6Wjo1mtpY_6DQ",
  "name": "Will Fong",
  "picture": "https://lh6.googleusercontent.com/-QI76B4HJQjk/AAAAAAAAAAI/AAAAAAAAAAA/ACHi3reUHwiFlGawEi4NdgXUee/s96-c/photo.jpg",
  "given_name": "Will",
  "family_name": "Fong",
  "locale": "en-GB",
  "iat": 1580227102,
  "exp": 1580230702,
  "jti": "009e2cbf75162abadbd3c571c1"
}
'''