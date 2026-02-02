from flask import Blueprint, request
from db import db_query

listings_bp = Blueprint("listings", __name__)

@listings_bp.route("/search")
def search():
    q = request.args.get("q")
    sql = f"SELECT * FROM listings WHERE title LIKE '%{q}%'"
    return {"results": db_query(sql)}