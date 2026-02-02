from flask import Blueprint, request
import jwt
from config import JWT_SECRET

auth_bp = Blueprint("auth", __name__)

@auth_bp.route("/login", methods=["POST"])
def login():
    user = request.json.get("user")
    token = jwt.encode({"user": user, "role": "user"}, JWT_SECRET, algorithm="HS256")
    return {"token": token}