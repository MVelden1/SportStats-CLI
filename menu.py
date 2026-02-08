from api import get_athlete, get_activities
from logic.compare import compare_weeks
from logic.filters import open_filters
from logic.statistics import open_statistics
from logic.welcome import welcome
from utils import refresh_access_token, get_valid_access_token

def show_main_menu(access_token):
    # TODO: afhandeling bij API niet bereikbaar
    # haalt de naam op voor het welkomstbericht
    athlete = get_athlete(access_token)
    print(welcome(athlete['firstname'], athlete["lastname"]))

    while True:
        print("=== SportStats CLI ===")
        print("1) Bekijk statistieken")
        print("2) Filter activiteiten")
        print("3) Vergelijk weken")
        print("4) TEST API athlete")
        print("5) TEST API activities")
        print("6) TEST Refresh token")
        print("7) TEST Expired token")
        print("0) Afsluiten\n")

        try:
            choice = int(input("Selecteer een optie (0-4): "))

            if choice == 1:
                print("Statistieken worden geopend...\n")
                open_statistics()

            elif choice == 2:
                print("Filters worden geopend...\n")
                open_filters()

            elif choice == 3:
                print("Weken vergelijken...\n")
                compare_weeks()

            elif choice == 4:
                print("TEST API (athlete endpoint)...\n")
                get_athlete(access_token)

            elif choice == 5:
                print("TEST API (activities endpoint)...\n")
                get_activities(access_token)

            elif choice == 6:
                print("TEST API (refresh token)...")
                refresh_access_token()

            elif choice == 7:
                print("TEST Expired token...")
                get_valid_access_token()

            elif choice == 0:
                print("De applicatie wordt afgesloten...")
                break

            else:
                print("Dit is geen valide optie.\n")

        except ValueError:
            print("Ongeldige invoer!\n")
