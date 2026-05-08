import requests
from utils import STRAVA_ATHLETE_ENDPOINT, STRAVA_ACTIVITY_ENDPOINT


def get_activities(access_token: str, limit: int) -> list:
    url = STRAVA_ACTIVITY_ENDPOINT
    header = _auth_header(access_token)
    param = {"per_page": limit, "page": 1}
    activities = requests.get(url, headers=header, params=param)

    return activities.json()


def get_athlete(access_token: str) -> dict:
    url = STRAVA_ATHLETE_ENDPOINT
    header = _auth_header(access_token)
    athlete = requests.get(url, headers=header)

    return athlete.json()

def _auth_header(acces_token: str) -> dict:
    return {"Authorization": f"Bearer {acces_token}"}
