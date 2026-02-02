import os
from config import UPLOAD_DIR

def save_file(name, content):
    path = f"{UPLOAD_DIR}/{name}"
    with open(path, "wb") as f:
        f.write(content)
    return path