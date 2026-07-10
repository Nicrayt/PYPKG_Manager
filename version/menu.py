try:
    from upgrade_all_pkg_list import *
    from config_variable import *
    from uninstall_pkg import *
    from download_pkg import *
    from install_pkg import *
    from search_pkg import *
    from upgrade import *
    import time
    import os
except (ImportError, ModuleNotFoundError):  print("Error: The required modules are not installed or not found."); exit()

version_of_pkg_manager_menu = "0.2"
name_of_package_manager_menu = "easy-menu"

def clear_the_interface():
    os.system('cls' if os.name == 'nt' else 'clear') # Clear the screen

def menu():
        clear_the_interface() # Clear the screen
        print(f"""Welcome to {name_of_package_manager_menu} "v{version_of_pkg_manager_menu}".""") # Print the menu

        while True:
            # Information
            print("1. Search for a package")
            print("2. Uninstall a package")
            print("3. Install a package")
            print("4. Upgrade PyPKG")
            print("5. Exit")

            user_input:str = input("What would you like to do? (1-5): ") # Input

            if user_input == '1': # search
                clear_the_interface()
                print("Search Package")
                user_input = input("Search for a package: ")
                search_package(pkg_name=user_input, show=True)
                input("Press enter to continue...")
                time.sleep(2)
            
            elif user_input == '2': # Uninstall
                clear_the_interface()
                print("Uninstall Package")
                user_input = input("Enter the name of the package you want to uninstall: ")
                uninstall_pkg(pkg_name=user_input, noconfirm=False)
                input("Press enter to continue...")
                time.sleep(2)
            
            elif user_input == '3': # Install
                clear_the_interface()
                print("Install a Package")
                user_input = input("Enter the name of the package you want to install: ")
                install_package(pkg_name=user_input, noconfirm=False)
                input("Press enter to continue...")
                time.sleep(2)
            
            elif user_input == '4': # Upgrade
                clear_the_interface()
                default_upgrade(noconfirm=True)
                input("Press enter to continue...")
                time.sleep(2)

            elif user_input == '5' or user_input == 'exit': # Exit
                clear_the_interface()
                time.sleep(1)
                return
            
            else: # If nothing in the list select.
                clear_the_interface()
                print("Invalid input. Please try again.")
                time.sleep(1)

try:
    menu()

except KeyboardInterrupt:
    print("\nExiting the program")
    time.sleep(1)
    clear_the_interface()


except Exception as e:
    print(f"An error occurred: {e}")
    input("Press enter to continue...")
    time.sleep(1)
    clear_the_interface()
    menu()
