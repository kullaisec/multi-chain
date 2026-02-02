import jwt
from config import JWT_SECRET

def decode_token(token):
    return jwt.decode(token, JWT_SECRET, options={"verify_signature": False})