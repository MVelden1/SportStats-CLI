import datetime
import os

from rich import box
from rich.console import Console
from rich.table import Table

from api import get_activities
from utils import format_timedelta, min_per_km

console = Console()

def open_last_10_activities(access_token: str, limit: int) -> None:
    activities = get_activities(access_token, limit)
    statistics_table(activities)
    return


def statistics_table(activities: list) -> None:
    table = Table(title="activiteiten", box=box.ROUNDED) #box=box.SIMPLE_HEAVY)

    table.add_column("Naam", style="cyan")
    table.add_column("afstand", style="green", justify="right")
    table.add_column("tijd", style="blue", justify="right")
    table.add_column("tempo", style="blue", justify="right")

    for activity in activities:
        name = activity['name']
        distance_km = (activity['distance'] / 1000)
        distance = f"{distance_km:.2f}"
        moving_time = format_timedelta(datetime.timedelta(seconds=activity['moving_time']))
        pace = min_per_km(distance_km, activity['moving_time'])

        table.add_row(name, distance, moving_time, pace)

    console.print(table)
    input("Druk op enter om door te gaan...")
    os.system('cls' if os.name == 'nt' else 'clear')

# open_statistics("969e90f9cf856d2de0f89d5205a1ea334d645847")
