try:
    from upgrade_all_pkg_list import *
    from config_variable import *
    from download_pkg import *
    from install_pkg import *
    from search_pkg import *
    from upgrade import *
    import time
    import os
except (ImportError, ModuleNotFoundError):  print("Error: The required modules are not installed or not found."); exit()

version_of_pkg_manager_menu = "0.1"
name_of_package_manager_menu = "easy-menu"


def menu():
    try:
        while True:
            os.system('cls' if os.name == 'nt' else 'clear')

            print(f"""Welcome to easy-menu of {name_of_package_manager} version:"{version_of_pkg_manager_menu}".""")
            print("\nThis version is strongly discouraged because it is in the ultra-alpha stage; the menu is buggy and barely works.\n")
            print("What would you like to do?")
            print("1. Search for a package")
            print("2. Install a package")
            print(f"3. Upgrade {name_of_package_manager}")
            print("4. Download a package")
            print("5. Exit")

            user_input:str = input("Enter your choice (1-5): ").strip()

            if user_input == "1":
                user_input = input("Enter the name of the package you want to search > ")
                search_pkg(user_input)
            elif user_input == "2":
                user_input = input("Enter the name of the package you want to install > ")
                install_pkg(user_input)
            elif user_input == "3":
                print("Not now/not finished yet...")
                time.sleep(3)
            elif user_input == "4":
                user_url = input("Enter the URL > ")
                user_file_name = input("Enter the filename > ")
                download_pkg(user_url, user_file_name, default_save_pkg_list_dir, True)
            elif user_input == "5":
                break
            else:
                print("Invalid input. Please try again.")

    except KeyboardInterrupt: menu()
    except Exception as e: print(f"Error: {e}"); input("Press any key to continue..."); menu()

    os.system('cls' if os.name == 'nt' else 'clear')
    print(f"{name_of_package_manager} has been exited.")

menu()