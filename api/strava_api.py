import requests
from dotenv import load_dotenv
from utils import STRAVA_ATHLETE_ENDPOINT, STRAVA_ACTIVITY_ENDPOINT

# TODO Weghalen als alles af is. Nu voor testen
load_dotenv()

def get_activities(access_token) -> list:
    # url = STRAVA_ACTIVITY_ENDPOINT
    # token = "?access_token=" + os.getenv("ACCESS_TOKEN")
    #
    # response = requests.get(url + token)

    url = STRAVA_ACTIVITY_ENDPOINT
    header = _auth_header(access_token)
    param = {"per_page": 200, "page": 1}
    activities = requests.get(url, headers=header, params=param)

    # print(activities)
    # print(activities.json())
    return activities.json()


def get_athlete(access_token) -> dict:
    url = STRAVA_ATHLETE_ENDPOINT
    header = _auth_header(access_token)

    respons = requests.get(url, headers=header)

    # TODO: print weghalen als api functionaliteit af is
    # print(respons)
    # print(respons.json())
    return respons.json()

def _auth_header(acces_token: str) -> dict:
    return {"Authorization": f"Bearer {acces_token}"}

# TODO weghalen als klaar
# get_athlete()
# get_activities()
# get_refresh_token()
