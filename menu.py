import questionary
from rich.console import Console
from rich.panel import Panel

from api import get_athlete, get_activities
from logic.compare import compare_weeks
from logic.filters import open_filters
from logic.help import help_info
from logic.performances import calculate_performances
from logic.open_last_10_activities import open_last_10_activities
from logic.welcome import welcome

console = Console()
def show_main_menu(access_token: str) -> None:
    # TODO: afhandeling bij API niet bereikbaar
    athlete = get_athlete(access_token)
    console.print(
        Panel.fit(
            f"[bold cyan]SportStats CLI[/bold cyan]\n"
            f"{welcome(athlete['firstname'], athlete['lastname'])}",
            border_style="cyan"
        )
    )

    menu_choices = [
        questionary.Choice(
            "Bekijk laatste 10 activiteiten",
            value=lambda: open_last_10_activities(access_token, limit=10)
        ),
        questionary.Choice(
            "Filter activiteiten",
            value=lambda: open_filters(access_token, limit=100)
        ),
        questionary.Choice(
            "Vergelijk weken",
            value=lambda: compare_weeks(access_token, limit=100)
        ),
        questionary.Choice(
            "Vergelijkbare prestaties berekenen",
            value=lambda: calculate_performances()
        ),
        questionary.Choice(
            "Help",
            value=lambda: help_info()
        ),
        questionary.Choice(
            "Afsluiten",
            value="quit"
        ),
    ]

    while True:
        action = questionary.select(
            "Wat wil je doen\n",
            choices=menu_choices
        ).ask()

        if action == "quit":
            console.print("[bold red]Programma afgesloten.")
            break

        action()
