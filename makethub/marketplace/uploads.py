from flask import Blueprint, request
from utils.fs import save_file
from workers.image_processor import process_image

uploads_bp = Blueprint("uploads", __name__)

@uploads_bp.route("/upload", methods=["POST"])
def upload():
    file = request.files["file"]
    path = save_file(file.filename, file.read())
    process_image(path)
    return "Uploaded"