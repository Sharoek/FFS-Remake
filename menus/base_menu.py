from abc import ABC, abstractmethod
from menus.super_admin_menu import SuperAdminMenu


class BaseMenu(ABC):
    def __init__(self, username):
        self.username = username

    def run(self):
        self.display_header()
        while True:
            self.show_options()
            choice = input("Voer een keuze in: ").strip().lower()
            if not self.handle_choice(choice):
                break

    def display_header(self):
        print(f"\nIngelogd als: {self.username}\n")

    @abstractmethod
    def show_options(self):
        pass

    @abstractmethod
    def handle_choice(self, choice):
        pass

