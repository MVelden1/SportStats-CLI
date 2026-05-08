import datetime

import questionary
from rich.console import Console

from api import get_activities
from utils import activities_table

console = Console()

def open_filters(access_token: str, limit: int) -> None:
    activities = get_activities(access_token, limit)
    active_filters = {}

    while True:
        filtered = apply_filters(activities, active_filters)
        activities_table(filtered)

        choice = questionary.select(
            "Filter toevoegen:",
            choices=[
                questionary.Choice("Periode", value="periode"),
                questionary.Choice("Minimale afstand (km)", value="afstand"),
                questionary.Choice("Minimaal tempo (MM:SS)", value="tempo"),
                questionary.Choice("Filters resetten", value="reset"),
                questionary.Choice("Terug naar menu", value="back"),
            ]
        ).ask()

        if choice == "back":
            break
        elif choice == "reset":
            active_filters = {}
        elif choice == "periode":
            active_filters["periode"] = ask_period()
        elif choice == "afstand":
            active_filters["afstand"] = ask_distance()
        elif choice == "tempo":
            active_filters["tempo"] = ask_pace()


def apply_filters(activities: list, filters: dict) -> list:
    result = activities

    if "periode" in filters:
        since = filters["period"]
        result = [a for a in result if datetime.datetime.strptime(a['start_date_local'], "%Y-%m-%dT%H:%M:%SZ") >= since]

    if "afstand" in filters:
        distance = filters["distance"]
        result = [a for a in result if (a['distance'] / 1000) >= distance]

    if "tempo" in filters:
        pace = filters["pace"]
        result = [a for a in result if a['average_speed'] >= pace]

    return result

def ask_period() -> datetime.datetime:
    choice = questionary.select(
        "Periode:",
        choices=[
            questionary.Choice("Afgelopen 7 dagen", value=7),
            questionary.Choice("Afgelopen 30 dagen", value=30),
            questionary.Choice("Afgelopen 90 dagen", value=90),
            questionary.Choice("Dit jaar", value="jaar"),
        ]
    ).ask()

    if choice == "jaar":
        return datetime.datetime(datetime.datetime.now().year, 1, 1)
    return datetime.datetime.now() - datetime.timedelta(days=choice)


def ask_distance() -> float:
    while True:
        raw = console.input("[cyan]Minimale afstand in km (bijv. 10): [/cyan]")
        try:
            return float(raw.replace(",", "."))
        except ValueError:
            console.print("[red]Voer een geldig getal in (bijv. 10 of 10.5)[/red]")


def ask_pace() -> float:
    while True:
        raw = console.input("[cyan]Minimaal tempo in MM:SS (bijv. 5:00): [/cyan]")
        if ":" in raw:
            parts = raw.split(":")
            try:
                seconds_per_km = int(parts[0]) * 60 + int(parts[1])
                return 1000 / seconds_per_km  # omzetten naar m/s
            except (ValueError, ZeroDivisionError):
                pass
        console.print("[red]Ongeldig formaat. Gebruik MM:SS (bijv. 6:00)[/red]")

