from api.strava_api import get_athlete
from typing import Callable, Dict, Any


# TODO nog niet wat het moet zijn
def welcome():
    athlete = get_athlete()
    name = f"{athlete['firstname']} {athlete['lastname']}"
    return f"Welkom terug {name}!\n"

# TODO weghalen
# welcome()
