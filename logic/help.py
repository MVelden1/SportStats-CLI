from rich import box
from rich.console import Console
from rich.panel import Panel
from rich.table import Table

console = Console()


def help_info() -> None:
    console.print()

    _print_features_table()
    _print_section(
        "Bekijk laatste 10 activiteiten",
        "Haalt je meest recente activiteiten op via Strava en toont ze in een tabel:\n"
        "  • [green]Naam[/green]     — de naam die je aan de activiteit hebt gegeven\n"
        "  • [green]Afstand[/green]  — in kilometers (bijv. 10 of 10.5)\n"
        "  • [green]Tijd[/green]     — bewegingstijd in M:SS of H:MM:SS\n"
        "  • [green]Tempo[/green]    — gemiddeld tempo in min/km (bijv. 3:12/km)",
    )
    _print_section(
        "Filter activiteiten",
        "Toont je activiteiten en laat je live filters toepassen:\n"
        "  • [green]Periode[/green]           — afgelopen 7, 30, 90 dagen of dit jaar\n"
        "  • [green]Minimale afstand[/green]  — voer een waarde in km in (bijv. 10 of 10.5)\n"
        "  • [green]Minimaal tempo[/green]    — voer een tempo in als MM:SS (bijv. 5:00)\n\n"
        "  Filters stapelen zich op. Gebruik [bold]'Filters resetten'[/bold] om alles te wissen.",
    )
    _print_section(
        "Vergelijk weken",
        "Toont een overzichtstabel van je [bold]afgelopen 4 weken[/bold].\n"
        "Per week zie je:\n"
        "  • [green]Aantal activiteiten[/green]\n"
        "  • [green]Totale afstand[/green] in km\n"
        "  • [green]Totale bewegingstijd[/green]\n"
        "  • [green]Gemiddeld tempo[/green] in min/km",
    )
    _print_section(
        "Vergelijkbare prestaties berekenen",
        "Bereken verwachte racetijden op basis van een bekende tijd.\n\n"
        "  1. Kies de afstand waarvan je de tijd weet (5km, 10km, halve of marathon).\n"
        "  2. Voer je tijd in. Toegestane formaten:\n"
        "       [cyan]M:SS[/cyan]       bijv. [italic]45:30[/italic]  (45 minuten, 30 seconden)\n"
        "       [cyan]H:MM:SS[/cyan]    bijv. [italic]1:32:00[/italic] (1 uur, 32 minuten)\n"
        "  3. De app berekent voorspelde tijden voor alle vier afstanden\n"
        "     met de Riegel-formule: [italic]T₂ = T₁ × (D₂ / D₁)^1.06[/italic]",
    )
    _print_section(
        "Tips",
        "  • Gebruik [bold]'Terug naar menu'[/bold] in submenu's om terug te keren.\n"
        "  • Je access token wordt automatisch vernieuwd als het verlopen is.\n"
        "  • Activiteiten worden opgehaald van Strava. Een internetverbinding is vereist.",
    )

    input("Druk op enter om door te gaan...")


def _print_features_table() -> None:
    table = Table(title="Functies", box=box.ROUNDED, title_style="bold blue")
    table.add_column("Functie", style="cyan")
    table.add_column("Status", justify="center")

    table.add_row("Bekijk laatste 10 activiteiten", "[green]Beschikbaar[/green]")
    table.add_row("Vergelijkbare prestaties berekenen", "[green]Beschikbaar[/green]")
    table.add_row("Filter activiteiten", "[green]Beschikbaar[/green]")
    table.add_row("Vergelijk weken", "[green]Beschikbaar[/green]")

    console.print(table)
    console.print()


def _print_section(title: str, body: str) -> None:
    console.print(Panel(body, title=f"[bold]{title}[/bold]", border_style="blue", padding=(1, 2)))
    console.print()
