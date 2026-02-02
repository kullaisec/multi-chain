from flask import request, g
from auth.jwt_utils import decode_token

def require_auth():
    token = request.headers.get("Authorization", "").replace("Bearer ", "")
    g.user = decode_token(token)