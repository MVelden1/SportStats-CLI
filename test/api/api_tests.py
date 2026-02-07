import json
from api.strava_api import get_activities, get_athlete


def test():
    get_athlete_test()
    get_activities_test()


def get_athlete_test():
    with open("athlete.json", "w") as f:
        json.dump(get_athlete(), f, indent=True)

def get_activities_test():
    with open("activities.json", "w") as f:
        json.dump(get_activities(), f, indent=True)


if __name__ == "__test__":
    test()
