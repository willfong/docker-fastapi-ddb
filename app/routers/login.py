import requests
import hashlib
from fastapi import APIRouter
from pydantic import BaseModel
from ..log import logger

router = APIRouter()

class LoginToken(BaseModel):
    value: str

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
    google_token = google_verify_access_token(token.value)
    user_id = google_find_or_create_user(token)
    return {"yourtoken": token.value}


def google_verify_access_token(id_token):
    # We're doing it the lazy way here. What we get from the client side is JWT, we can just verify that instead of calling Google
    # Reason for that is to reduce the amount of dependencies for this, a demo app
    # For production, we should do it the right way by using google-auth

    jwt = requests.get(f'https://oauth2.googleapis.com/tokeninfo?id_token={id_token}').json()
    if jwt.get('error'):
        print(jwt.get('error_description'))
        return jwt.get('error_description')
    # Here, you should check that your domain name is in hd
    # if jwt['hd'] == 'example.com':
    #   return jwt
    # For now, we're just going to accept all
    return jwt

def google_find_or_create_user(token):
    user_plaintext = f"{token['aud']}|{token['sub']}"
    user_id = hashlib.sha224(user_plaintext.encode('ascii')).hexdigest()
    
    return user_id


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