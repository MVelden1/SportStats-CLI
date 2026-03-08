import requests
from dotenv import load_dotenv
from utils import STRAVA_ATHLETE_ENDPOINT, STRAVA_ACTIVITY_ENDPOINT

# TODO Weghalen als alles af is. Nu voor testen
load_dotenv()

def get_activities(access_token, limit) -> list:
    url = STRAVA_ACTIVITY_ENDPOINT
    header = _auth_header(access_token)
    param = {"per_page": limit, "page": 1}
    activities = requests.get(url, headers=header, params=param)

    return activities.json()


def get_athlete(access_token) -> dict:
    url = STRAVA_ATHLETE_ENDPOINT
    header = _auth_header(access_token)
    athlete = requests.get(url, headers=header)

    return athlete.json()

def _auth_header(acces_token: str) -> dict:
    return {"Authorization": f"Bearer {acces_token}"}
