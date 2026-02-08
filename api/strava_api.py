import os
import requests
import urllib3
from dotenv import load_dotenv
from utils.constants import STRAVA_ATHLETE_ENDPOINT, STRAVA_ACTIVITY_ENDPOINT, STRAVA_REFRESH_TOKEN_ENDPOINT, \
    STRAVA_PARAMS_REFRESH_TOKEN

# TODO Weghalen als alles af is. Nu voor testen
load_dotenv()
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

def get_refresh_token():
    url = STRAVA_REFRESH_TOKEN_ENDPOINT
    payload = STRAVA_PARAMS_REFRESH_TOKEN

    print("Requesting token...\n")
    response = requests.post(url, data=payload, verify=False)
    print(response.json())
    acces_token = response.json()['access_token']
    print("Access Token = {}\n".format(acces_token))
    # load_dotenv(override=True)

    return acces_token

def get_activities():
    # url = STRAVA_ACTIVITY_ENDPOINT
    # token = "?access_token=" + os.getenv("ACCESS_TOKEN")
    #
    # response = requests.get(url + token)

    url = STRAVA_ACTIVITY_ENDPOINT
    token = os.getenv("ACCESS_TOKEN")
    header = {"authorization": f"Bearer {token}"}
    param = {"per_page": 200, "page": 1}
    activities = requests.get(url, headers=header, params=param)

    print(activities)
    print(activities.json())
    return activities.json()


def get_athlete():
    url = STRAVA_ATHLETE_ENDPOINT
    token = os.getenv("ACCESS_TOKEN")
    header = {"authorization": f"Bearer {token}"}

    respons = requests.get(url, headers=header)

    print(respons)
    print(respons.json())
    return respons.json()

# TODO weghalen als klaar
# get_athlete()
# get_activities()
get_refresh_token()
