import os
import requests
from dotenv import load_dotenv
from utils.constants import STRAVA_ATHLETE_ENDPOINT, STRAVA_ACTIVITY_ENDPOINT

# TODO Weghalen als alles af is. Nu voor testen
load_dotenv()

def get_auth():
    pass

def get_activities():
    url = STRAVA_ACTIVITY_ENDPOINT
    token = os.getenv("ACCESS_TOKEN")
    headers = {"auhorization": f"Bearer {token}"}

    response = requests.get(url, headers=headers)
    print(response)
    print(response.json())
    print("API moet nog worden geïmplementeerd...")


def get_athlete():
    url = STRAVA_ATHLETE_ENDPOINT
    token = os.getenv("ACCESS_TOKEN")
    headers = {"authorization": f"Bearer {token}"}

    respons = requests.get(url, headers=headers)

    print(respons)
    print(respons.json())
    return respons.json()

get_athlete()
# get_activities()
