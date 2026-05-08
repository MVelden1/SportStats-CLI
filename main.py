from dotenv import load_dotenv
from requests import RequestException
from rich.console import Console

from menu import show_main_menu
from utils import get_valid_access_token

console = Console()


def main() -> None:
    load_dotenv()

    try:
        access_token = get_valid_access_token()
    except FileNotFoundError:
        console.print("[bold red]tokens.json niet gevonden. Zorg dat het bestand aanwezig is in de utils map.[/bold red]")
        return

    except RequestException:
        console.print("[bold red]Kon het access token niet vernieuwen. Controleer je internetverbinding.[/bold red]")
        return

    show_main_menu(access_token)


if __name__ == "__main__":
    main()
