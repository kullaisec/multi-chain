import requests
from config import INTERNAL_ADMIN_URL

def fetch_internal(path):
    return requests.get(INTERNAL_ADMIN_URL + path).text