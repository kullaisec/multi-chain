from flask import Blueprint, request
from workers.report_worker import submit_report

reviews_bp = Blueprint("reviews", __name__)

@reviews_bp.route("/review", methods=["POST"])
def review():
    text = request.json["text"]
    submit_report(text)
    return "OK"