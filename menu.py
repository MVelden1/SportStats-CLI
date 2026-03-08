import os

from rich.console import Console

from api import get_athlete, get_activities
from logic.compare import compare_weeks
from logic.filters import open_filters
from logic.help import help_info
from logic.performances import calculate_performances
from logic.statistics import open_statistics
from logic.welcome import welcome
from utils import refresh_access_token, get_valid_access_token

console = Console()

def show_main_menu(access_token):
    # TODO: afhandeling bij API niet bereikbaar
    athlete = get_athlete(access_token)
    print(welcome(athlete['firstname'], athlete["lastname"]))

    while True:
        print("=== SportStats CLI ===")
        print("1) Bekijk statistieken")
        print("2) Filter activiteiten")
        print("3) Vergelijk weken")
        print("4) Vergelijkbare prestaties berekenen")
        print("5) Help")
        print("0) Afsluiten\n")

        try:
            choice = int(console.input("[cyan]Selecteer een optie (0-5): [/cyan]").strip())

            match choice:
                case 1:
                    print("Statistieken worden geopend...\n")
                    open_statistics(access_token)
                case 2:
                    print("Filters worden geopend...\n")
                    open_filters(access_token)
                case 3:
                    print("Weken vergelijken...\n")
                    compare_weeks(access_token)
                case 4:
                    print("Vergelijkbare prestaties berekenen...\n")
                    os.system('cls' if os.name == 'nt' else 'clear')
                    calculate_performances()
                case 5:
                    print("Help...\n")
                    help_info()
                case 0:
                    print("De applicatie wordt afgesloten...")
                    break

# TODO weghalen als klaar, nu voor testen API functionaliteit
                case 6:
                    print("TEST API (athlete endpoint)...\n")
                    get_athlete(access_token)
                case 7:
                    print("TEST API (activities endpoint)...\n")
                    get_activities(access_token)
                case 8:
                    print("TEST API (refresh token)...")
                    refresh_access_token()
                case 9:
                    print("TEST Expired token...")
                    get_valid_access_token()
                case _:
                    print("Dit is geen valide optie.\n")

        except ValueError:
            console.print("[bold red]Ongeldige invoer![/bold red]\n")
        

        # if choice is not None and choice != 0:
        #     input("\nDruk op Enter om terug te keren naar het hoofdmenu...")

