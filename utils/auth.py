import os
from datetime import datetime

import requests
import urllib3

from utils import STRAVA_REFRESH_TOKEN_ENDPOINT, ACCESS_TOKEN, REFRESH_TOKEN
from utils.io_handler import read_json, write_json

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
# TODO: onderstaande nog optimaliseren?
file_path = os.path.join(os.path.dirname(__file__), "tokens.json")

def load_tokens(token) -> str | None:
    tokens = read_json(file_path)
    if token == REFRESH_TOKEN:
        return tokens["refresh_token"]
    elif token == ACCESS_TOKEN:
        return tokens["access_token"]
    return None


def get_valid_access_token() -> str:
    data = read_json(file_path)
    expire_time = datetime.fromtimestamp(data["expires_at"])

    if datetime.now() > expire_time:
        return refresh_access_token()
    return load_tokens(ACCESS_TOKEN)


def refresh_access_token() -> str:
    url = STRAVA_REFRESH_TOKEN_ENDPOINT
    payload = {
        "client_id": os.getenv("CLIENT_ID"),
        "client_secret": os.getenv("CLIENT_SECRET"),
        "refresh_token": load_tokens(REFRESH_TOKEN),
        "grant_type": "refresh_token",
        "f": "json"
    }

    response = requests.post(url, data=payload, verify=False)
    write_json(file_path, response.json(), 4)

    access_token = load_tokens(ACCESS_TOKEN)
    return access_token
