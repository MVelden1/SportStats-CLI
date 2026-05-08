import datetime
from rich.console import Console
from rich.table import Table
from rich import box
from utils import format_timedelta, min_per_km

console = Console()

def activities_table(activities: list, title: str = "Activiteiten") -> None:
    table = Table(title=f"{title} ({len(activities)} resultaten)", box=box.ROUNDED)

    table.add_column("Naam", style="cyan")
    table.add_column("Datum", style="magenta", justify="right")
    table.add_column("Afstand", style="green", justify="right")
    table.add_column("Tijd", style="blue", justify="right")
    table.add_column("Tempo", style="blue", justify="right")

    for activity in activities:
        name = activity['name']
        date = datetime.datetime.strptime(activity['start_date_local'], "%Y-%m-%dT%H:%M:%SZ").strftime("%d-%m-%Y")
        distance_km = activity['distance'] / 1000
        moving_time = format_timedelta(datetime.timedelta(seconds=activity['moving_time']))
        pace = min_per_km(distance_km, activity['moving_time'])

        table.add_row(name, date, f"{distance_km:.2f}", moving_time, pace)

    console.print(table)