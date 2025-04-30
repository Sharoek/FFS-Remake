from menus.base_menu import BaseMenu

class SuperAdminMenu(BaseMenu):
    def show_options(self):
        print("[1] Gebruiker toevoegen")
        print("[2] Lid registreren")
        print("[3] Logs bekijken")
        print("[q] Uitloggen")

    def handle_choice(self, choice):
        if choice == "1":
            print("Gebruiker toevoegen (super admin logic hier)")
        elif choice == "2":
            print("Lid registreren (super admin logic hier)")
        elif choice == "3":
            print("Logs weergeven (encrypted logs ontsleutelen)")
        elif choice == "q":
            print("Uitloggen...")
            return False
        else:
            print("Ongeldige keuze.")
        return True
