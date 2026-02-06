from logic.compare import compare_weeks
from logic.filters import open_filters
from logic.statistics import open_statistics


def show_main_menu():

    while True:
        print("=== SportStats CLI ===")
        print("1) Bekijk statistieken")
        print("2) Filter activiteiten")
        print("3) Vergelijk weken")
        print("4) Afsluiten\n")

        try:
            choice = int(input("Selecteer een optie (1-4): "))

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
                print("De applicatie wordt afgesloten.")
                break

            else:
                print("Dit is geen valide optie.\n")

        except ValueError:
            print("Ongeldige invoer!\n")
