import json
import os
from datetime import datetime

import requests
import urllib3

from utils import STRAVA_REFRESH_TOKEN_ENDPOINT, ACCESS_TOKEN, REFRESH_TOKEN

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
token_path = os.path.join(os.path.dirname(__file__), "tokens.json")

def load_tokens(token):
    with open(token_path, "r") as f:
        tokens = json.load(f)
        if token == REFRESH_TOKEN:
            return tokens["refresh_token"]
        elif token == ACCESS_TOKEN:
            return tokens["access_token"]
        return None


def get_valid_access_token():
    with open(token_path, "r") as f:
        data = json.load(f)
        expire_time = datetime.fromtimestamp(data["expires_at"])
    # Token is verlopen
    if datetime.now() > expire_time:
        return refresh_access_token()
    # Token is nog geldig
    else:
        return load_tokens(ACCESS_TOKEN)


def refresh_access_token():
    url = STRAVA_REFRESH_TOKEN_ENDPOINT
    payload = {
        "client_id": os.getenv("CLIENT_ID"),
        "client_secret": os.getenv("CLIENT_SECRET"),
        "refresh_token": load_tokens(REFRESH_TOKEN),
        "grant_type": "refresh_token",
        "f": "json"
    }

    response = requests.post(url, data=payload, verify=False)
    with open(token_path, "w") as f:
        json.dump(response.json(), f, indent=True)

    access_token = load_tokens(ACCESS_TOKEN)
    return access_token
