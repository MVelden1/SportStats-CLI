from dotenv import load_dotenv
from menu import show_main_menu
from utils import get_valid_access_token


def main():
    load_dotenv()

    access_token = get_valid_access_token()
    show_main_menu(access_token)


if __name__ == "__main__":
    main()
