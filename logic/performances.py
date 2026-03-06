import datetime
import os

from rich.console import Console
from rich.table import Table

from utils import to_seconds, format_timedelta


def calculate_performances():
    # print("vergelijkbare prestaties berekenen is nog niet geimplementeerd...\n")
    print("Hier kun je vergelijkbare prestaties berekenen bijv. op basis van een recent gelopen pr.\n"
          "De afstanden die worden berekend zijn 5km, 10km, halve marathon en de marathon.\n")

    while True:
        os.system('cls' if os.name == 'nt' else 'clear')
        menu_items = {
            1: {"id": "5km"},
            2: {"id": "10km"},
            3: {"id": "Halve marathon"},
            4: {"id": "Marathon"},
            5: {"id": "Terug naar menu"},
        }
        distances = {
            1: {"km": 5, "label": "5km", "example": "20:00"},
            2: {"km": 10, "label": "10km", "example": "40:00"},
            3: {"km": 21.0975, "label": "Halve marathon", "example": "1:30:00"},
            4: {"km": 42.195, "label": "Marathon", "example": "3:00:00"},
            0: {"label": "Terug naar menu"}
        }

        for index, menu_item in menu_items.items():
            print(f"{index}) {menu_item['id']}")

        # print("1) 5km")
        # print("2) 10km")
        # print("3) halve marathon")
        # print("4) marathon")
        # print("0) Terug naar menu")

        try:
            choice = int(input("\nMaak een keuze uit een van de opties: "))

            if choice in distances and choice != 0:
                from_distance = distances[choice].get('km')
                print(from_distance)
                distance_label = distances[choice].get('label')
                print(distance_label)
                example_distance = distances[choice].get('example')
                print(example_distance)

                user_time = input(f"Voer een {distance_label} tijd in. voorbeeld: {example_distance}\n")

                predicted_times = calculate_predicted_time(user_time, from_distance)

                predicted_times_to_table(predicted_times)


        except ValueError:
            print("Dit is geen geldige invoer")



# # TODO functie wat opschonen, zodat hij overzichtelijker is: opsplitsen in meerdere functies

def calculate_predicted_time(user_time: str, from_distance: float) -> dict[str, str]:
    """Return predicted times as datetime.timedelta values."""
    time_in_seconds = to_seconds(user_time)
    user_td = datetime.timedelta(seconds=time_in_seconds)

    predicted_times: dict[str, str] = {
        '5km': format_timedelta(user_td),
        '10km': format_timedelta(datetime.timedelta(seconds=est_time_in_seconds(10, time_in_seconds, from_distance))),
        'Halve marathon': format_timedelta(datetime.timedelta(seconds=est_time_in_seconds(21.0975, time_in_seconds, from_distance))),
        'Marathon': format_timedelta(datetime.timedelta(seconds=est_time_in_seconds(42.195, time_in_seconds, from_distance)))
    }

    return predicted_times

def est_time_in_seconds(km: float, time_in_seconds: int, from_distance: float) -> int:
    return round(time_in_seconds * (km / from_distance) ** 1.06)


def predicted_times_to_table(predicted_times):
    console = Console()
    table = Table(title="Voorspelde tijden")

    table.add_column("Afstand", style="cyan")
    table.add_column("Tijd", style="green", justify="right")

    for distance, time in predicted_times.items():
        table.add_row(distance, time)

    console.print(table)

    input("Druk op enter om door te gaan")

    return




# TODO weghalen. is nu voor tesen fucties
my_dict = {'5k': '20:00', '10k': '41:42', 'Halve marathon': '1:32:00', 'marathon': '3:11:49'}
# predicted_times_to_table(my_dict)
calculate_performances()
# to_seconds("00:20:00")
# calculate_predicted_time("00:20:00", 5)

