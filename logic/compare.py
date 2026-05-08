import datetime

from rich import box
from rich.console import Console
from rich.table import Table

from api import get_activities
from utils import min_per_km, format_timedelta

console = Console()

def compare_weeks(access_token: str, limit: int) -> None:
    activities = get_activities(access_token, limit)
    weeks = split_by_week(activities)
    comparison_table(weeks)
    input("Druk op enter om door te gaan...")


def split_by_week(activities: list) -> list[tuple]:
    today = datetime.datetime.now()
    start_of_this_week = (today - datetime.timedelta(days=today.weekday())).replace(hour=0, minute=0, second=0)

    weeks = []
    for i in range(4):
        week_start = start_of_this_week - datetime.timedelta(weeks=i)
        week_end = week_start + datetime.timedelta(weeks=1)
        week_activities = [
            a for a in activities
            if week_start <= datetime.datetime.strptime(a['start_date_local'], "%Y-%m-%dT%H:%M:%SZ") < week_end
        ]
        weeks.append((week_start, week_activities))

    return weeks


def calculate_stats(activities: list) -> dict:
    count = len(activities)
    total_distance = sum(a['distance'] for a in activities) / 1000
    total_time = sum(a['moving_time'] for a in activities)

    avg_pace = min_per_km(total_distance, total_time) if total_distance > 0 else "-"
    formatted_time = format_timedelta(datetime.timedelta(seconds=total_time)) if total_time > 0 else "-"

    return {
        "count": count,
        "distance": total_distance,
        "time": formatted_time,
        "pace": avg_pace,
    }


def comparison_table(weeks: list[tuple]) -> None:
    table = Table(title="Afgelopen 4 weken", box=box.ROUNDED)
    table.add_column("", style="bold")

    for week_start, _ in weeks:
        week_end = week_start + datetime.timedelta(days=6)
        label = f"{week_start.strftime('%d %b')} - {week_end.strftime('%d %b')}"
        table.add_column(label, justify="right")

    stats = [calculate_stats(activities) for _, activities in weeks]

    table.add_row("Activiteiten", *[str(s["count"]) for s in stats])
    table.add_row("Totale afstand", *[f"{s['distance']:.2f} km" for s in stats])
    table.add_row("Totale tijd", *[s["time"] for s in stats])
    table.add_row("Gem. tempo", *[s["pace"] for s in stats])

    console.print(table)
