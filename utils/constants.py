# Strava API endpoints
import os
from dotenv import load_dotenv

# TODO: WEGHALEN ALS KLAAR VOOR TESTEN NU HIER
load_dotenv()

STRAVA_BASE_URL = "https://www.strava.com/api/v3"
STRAVA_ATHLETE_ENDPOINT = f"{STRAVA_BASE_URL}/athlete"
STRAVA_ACTIVITY_ENDPOINT = f"{STRAVA_ATHLETE_ENDPOINT}/activities"
STRAVA_REFRESH_TOKEN_ENDPOINT = f"{STRAVA_BASE_URL}/oauth/token"
REFRESH_TOKEN="f4c8d0013274089bfbb3abd7ef0621ada2c1e801"


STRAVA_PARAMS_REFRESH_TOKEN={
        "client_id": os.getenv("CLIENT_ID"),
        "client_secret": os.getenv("CLIENT_SECRET"),
        "refresh_token": REFRESH_TOKEN,
        "grant_type": "refresh_token",
        "f": "json"
    }
