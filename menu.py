from api.strava_api import get_athlete, get_activities
from logic.compare import compare_weeks
from logic.filters import open_filters
from logic.statistics import open_statistics
from logic.welcome import welcome


def show_main_menu():
    # TODO: afhandeling bij API niet bereikbaar
    athlete = get_athlete()
    print(welcome(athlete['firstname'], athlete["lastname"]))

    while True:
        print("=== SportStats CLI ===")
        print("1) Bekijk statistieken")
        print("2) Filter activiteiten")
        print("3) Vergelijk weken")
        print("4) TEST API athlete")
        print("5) TEST API activities")
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
                get_athlete()

            elif choice == 5:
                print("TEST API (activities endpoint)...\n")
                get_activities()

            elif choice == 0:
                print("De applicatie wordt afgesloten...")
                break

            else:
                print("Dit is geen valide optie.\n")

        except ValueError:
            print("Ongeldige invoer!\n")
