from flask import Blueprint, g
from auth.middleware import require_auth
from utils.http import fetch_internal

admin_bp = Blueprint("admin", __name__)

@admin_bp.route("/admin")
def admin():
    require_auth()
    if g.user.get("role") == "admin":
        return fetch_internal("/stats")
    return "Forbidden", 403