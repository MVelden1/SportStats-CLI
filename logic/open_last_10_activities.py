from datetime import datetime, timedelta

import questionary
from rich import box
from rich.console import Console
from rich.table import Table

from api import get_activities
from utils import format_timedelta, min_per_km

console = Console()

def open_last_10_activities(access_token: str, limit: int) -> None:
    activities = get_activities(access_token, limit)
    statistics_table(activities)

    while True:
        sort_choice = questionary.select(
            "Sorteren op:",
            choices=[
                questionary.Choice("Datum (nieuwste eerst)", value=("start_date_local", True)),
                questionary.Choice("Datum (oudste eerst)", value=("start_date_local", False)),
                questionary.Choice("Afstand (hoog-laag)", value=("distance", True)),
                questionary.Choice("Afstand (laag-hoog)", value=("distance", False)),
                questionary.Choice("Tempo (snelst eerst)", value=("average_speed", True)),
                questionary.Choice("Terug naar menu", value="back"),
            ]
        ).ask()

        if sort_choice == "back":
            break

        key, reverse = sort_choice
        activities = sorted(activities, key=lambda a: a[key], reverse=reverse)
        statistics_table(activities)

    return


def statistics_table(activities: list) -> None:
    table = Table(title="activiteiten", box=box.ROUNDED) #box=box.SIMPLE_HEAVY)

    table.add_column("Naam", style="cyan")
    table.add_column("afstand", style="green", justify="right")
    table.add_column("tijd", style="blue", justify="right")
    table.add_column("tempo", style="blue", justify="right")
    table.add_column("Datum", style="magenta", justify="right")

    for activity in activities:
        name = activity['name']
        distance_km = (activity['distance'] / 1000)
        distance = f"{distance_km:.2f}"
        moving_time = format_timedelta(timedelta(seconds=activity['moving_time']))
        pace = min_per_km(distance_km, activity['moving_time'])
        date_str = activity['start_date_local']
        date = datetime.strptime(date_str, "%Y-%m-%dT%H:%M:%SZ").strftime("%d-%m-%Y")

        table.add_row(name, date, distance, moving_time, pace)

    console.print(table)
