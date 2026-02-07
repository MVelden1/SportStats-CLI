from dotenv import load_dotenv
from logic.welcome import welcome
from menu import show_main_menu


def main():
    load_dotenv()
    print(welcome())
    show_main_menu()


if __name__ == "__main__":
    main()
