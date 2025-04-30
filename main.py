from config.settings import SUPER_ADMIN_USERNAME, SUPER_ADMIN_PASSWORD
from services.auth_service import authenticate_user, get_user_role
from menus.super_admin_menu import SuperAdminMenu
from menus.admin_menu import AdminMenu
from menus.consultant_menu import ConsultantMenu
from crypto.rsa_crypto import load_keys
import getpass


def load_environment():
    print("Loading encryption keys...")
    load_keys()
    print("Environment initialized.\n")


def prompt_login():
    print("=== Unique Meal Member Management System ===\n")
    username = input("Username: ").strip()
    password = getpass.getpass("Password: ")
    return username, password


def handle_login(username, password):
    # Hardcoded Super Admin check
    if username == SUPER_ADMIN_USERNAME and password == SUPER_ADMIN_PASSWORD:
        print("Logged in as Super Admin.\n")
        SuperAdminMenu(username).run()
        return True

    # Authenticate other users via database
    if authenticate_user(username, password):
        role = get_user_role(username)
        print(f"Login successful. Role: {role}\n")

        if role == "admin":
            AdminMenu(username).run()
        elif role == "consultant":
            ConsultantMenu(username).run()
        else:
            print("Unknown role. Access denied.")
        return True

    print("Invalid credentials.\n")
    return False


def main():
    load_environment()

    for attempt in range(3):
        username, password = prompt_login()
        if handle_login(username, password):
            return

    print("Too many failed login attempts. Exiting...")


if __name__ == "__main__":
    main()
