from rich.console import Console
from rich.panel import Panel

console = Console()


def help_info() -> None:
    help_text = (
        "[bold]Zo werkt SportStats CLI[/bold]\n\n"
        "[cyan]Bekijk laatste 10 activiteiten[/cyan]\n"
        "Toont je meest recente activiteiten met afstand, tijd en tempo.\n\n"
        "[cyan]Filter activiteiten[/cyan]\n"
        "Deze functie is nog niet geimplementeerd.\n\n"
        "[cyan]Vergelijk weken[/cyan]\n"
        "Deze functie is nog niet geimplementeerd.\n\n"
        "[cyan]Vergelijkbare prestaties berekenen[/cyan]\n"
        "Bereken verwachte tijden voor 5km, 10km, halve marathon en marathon.\n\n"
        "[cyan]Tip[/cyan]\n"
        "Gebruik 'Terug naar menu' in submenu's om terug te keren."
    )

    panel = Panel.fit(help_text, title="Help", border_style="blue")
    console.print(panel)
    input("Druk op enter om door te gaan...")
