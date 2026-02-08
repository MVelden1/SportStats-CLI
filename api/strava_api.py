import requests
from dotenv import load_dotenv
from utils import STRAVA_ATHLETE_ENDPOINT, STRAVA_ACTIVITY_ENDPOINT

# TODO Weghalen als alles af is. Nu voor testen
load_dotenv()

def get_activities(acces_token):
    # url = STRAVA_ACTIVITY_ENDPOINT
    # token = "?access_token=" + os.getenv("ACCESS_TOKEN")
    #
    # response = requests.get(url + token)

    url = STRAVA_ACTIVITY_ENDPOINT
    header = {"authorization": f"Bearer {acces_token}"}
    param = {"per_page": 200, "page": 1}
    activities = requests.get(url, headers=header, params=param)

    print(activities)
    print(activities.json())
    return activities.json()


def get_athlete(acces_token):
    url = STRAVA_ATHLETE_ENDPOINT
    header = {"authorization": f"Bearer {acces_token}"}

    respons = requests.get(url, headers=header)

    print(respons)
    print(respons.json())
    return respons.json()

# TODO weghalen als klaar
# get_athlete()
# get_activities()
# get_refresh_token()
