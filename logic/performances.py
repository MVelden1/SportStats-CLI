import datetime
import os

from rich.console import Console
from rich.table import Table

from utils import to_seconds, format_timedelta

console = Console()

def calculate_performances() -> None:
    # print("vergelijkbare prestaties berekenen is nog niet geimplementeerd...\n")
    print("Hier kun je vergelijkbare prestaties berekenen bijv. op basis van een recent gelopen pr.\n"
          "De afstanden die worden berekend zijn 5km, 10km, halve marathon en de marathon.\n")

    distances = {
        1: {"km": 5, "label": "5km", "example": "20:00"},
        2: {"km": 10, "label": "10km", "example": "40:00"},
        3: {"km": 21.0975, "label": "Halve marathon", "example": "1:30:00"},
        4: {"km": 42.195, "label": "Marathon", "example": "3:00:00"},
    }

    while True:
        # os.system('cls' if os.name == 'nt' else 'clear')


        show_menu(distances)

        choice = get_user_choice()

        if choice not in distances:
            console.print(f"[bold red]Dit is geen geldige invoer[/bold red]\n")
            continue

        if choice in distances:
            from_distance = distances[choice].get('km')
            distance_label = distances[choice].get('label')
            example_distance = distances[choice].get('example')

            user_time = console.input(f"[cyan]Voer een {distance_label} tijd in (bijv. {example_distance}): [/cyan]")
            predicted_times = calculate_predicted_time(user_time, from_distance, distances)

            predicted_times_to_table(predicted_times)


def show_menu(menu_items: dict) -> None:
    for index, menu_item in menu_items.items():
        print(f"{index}) {menu_item['label']}")
    print("0) terug naar menu")


def get_user_choice() -> int | None:
    try:
        return int(console.input("\n[bold][cyan]Maak een keuze: [/bold][/cyan]"))
    except ValueError:
        return None


# # TODO functie wat opschonen, zodat hij overzichtelijker is: opsplitsen in meerdere functies

def calculate_predicted_time(user_time: str, from_distance: float, distances: dict) -> dict[str, dict[str, str]]:
    """Return predicted times as a dict"""
    time_in_seconds = to_seconds(user_time)
    predicted_times: dict[str, dict[str, str]] = {}

    for _, metric in distances.items():
        predicted = est_time_in_seconds(metric['km'], time_in_seconds, from_distance)
        formatted = format_timedelta(datetime.timedelta(seconds=predicted))
        min_per_km = est_min_per_km(metric['km'], predicted)
        metrics= {'time': formatted, 'pace': min_per_km}

        predicted_times[metric['label']] = metrics

    print()

    return predicted_times


def est_time_in_seconds(distance: float, time_in_seconds: int, from_distance: float) -> int:
    return round(time_in_seconds * (distance / from_distance) ** 1.06)


def est_min_per_km(distance: float, time: int) -> str:
    pace_sec_per_km = time / distance
    return f"{format_timedelta(datetime.timedelta(seconds=pace_sec_per_km))}/km"


def predicted_times_to_table(predicted_times):
    table = Table(title="🏃 Voorspelde tijden")

    table.add_column("Afstand", style="cyan")
    table.add_column("Tijd", style="green", justify="right")
    table.add_column("Tempo", style="yellow", justify="right")

    for distance, metric in predicted_times.items():
        table.add_row(distance, metric['time'], metric['pace'])

    console.print()
    console.print(table)
    input("Druk op enter om door te gaan...")

    return


# TODO weghalen. is nu voor tesen fucties
my_dict =  {'5km': {'time': '20:00', 'pace': '4:00/km'},
            '10km': {'time': '41:42', 'pace': '4:10/km'},
            'Halve marathon': {'time': '1:32:00', 'pace': '4:21/km'},
            'Marathon': {'time': '3:11:49', 'pace': '4:32/km'}
            }

# predicted_times_to_table(my_dict)
calculate_performances()
# to_seconds("00:20:00")
# calculate_predicted_time("00:20:00", 5)

