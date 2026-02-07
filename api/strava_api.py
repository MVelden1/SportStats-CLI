import os
import requests
from dotenv import load_dotenv

# TODO Weghalen als alles af is. Nu voor testen
load_dotenv()


def get_activities():
    print("API moet nog worden geïmplementeerd...")


def get_athlete():
    url = "https://www.strava.com/api/v3/athlete"
    token = os.getenv("ACCESS_TOKEN")
    headers = {"authorization": f"Bearer {token}"}

    respons = requests.get(url, headers=headers)

    # print(respons.status_code)
    # print(respons.json())

    return respons.json()

# get_athlete()
