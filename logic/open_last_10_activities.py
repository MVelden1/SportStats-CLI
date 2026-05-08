import questionary
from rich.console import Console

from api import get_activities
from utils import activities_table

console = Console()

def open_last_10_activities(access_token: str, limit: int) -> None:
    activities = get_activities(access_token, limit)
    activities_table(activities)

    while True:
        sort_choice = questionary.select(
            "Sorteren op:",
            choices=[
                questionary.Choice("Datum (nieuwste eerst)", value=("start_date_local", True)),
                questionary.Choice("Datum (oudste eerst)", value=("start_date_local", False)),
                questionary.Choice("Afstand (hoog-laag)", value=("distance", True)),
                questionary.Choice("Afstand (laag-hoog)", value=("distance", False)),
                questionary.Choice("Tempo (snelst eerst)", value=("average_speed", True)),
                questionary.Choice("Tempo (langzaamst eerst)", value=("average_speed", False)),
                questionary.Choice("Terug naar menu", value="back"),
            ]
        ).ask()

        if sort_choice == "back":
            break

        key, reverse = sort_choice
        activities = sorted(activities, key=lambda a: a[key], reverse=reverse)
        activities_table(activities)
