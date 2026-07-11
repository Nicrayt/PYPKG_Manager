try:
    from upgrade_all_pkg_list import *
    from config_variable import *
    from uninstall_pkg import *
    from download_pkg import *
    from install_pkg import *
    from search_pkg import *
    from upgrade import *
    import keyboard
    import time
    import os
except (ImportError, ModuleNotFoundError):  print("Error: The required modules are not installed or not found."); exit()



global select, version_of_pkg_manager_menu, name_of_package_manager_menu
version_of_pkg_manager_menu = "0.4"
name_of_package_manager_menu = "easy-menu"
select = 1

user_option = {"Install": 1, "uninstall": 2, "search": 3, "upgrade": 4, "help": 5,  "exit": 6}


def clear_the_interface():
    os.system('cls' if os.name == 'nt' else 'clear') # Clear the screen

def cafonctionnejegarde():
    input("")

def menu():
    global select, version_of_pkg_manager_menu, name_of_package_manager_menu
    while True:
        event = keyboard.read_event()
        if event.event_type == keyboard.KEY_DOWN:
            if keyboard.is_pressed("down"):
                select += 1
                time.sleep(0.01)
                print_menu()
            elif keyboard.is_pressed("up"):
                select -= 1
                time.sleep(0.01)
                print_menu()
            elif keyboard.is_pressed("enter"):
                clear_the_interface()
                if select == 1:
                    install()
                if select == 2:
                    uninstall()
                if select == 3:
                    search()
                if select == 4:
                    default_upgrade()
                if select == 5:
                    print(help)
                if select == 6:
                    break
                

def install():
    cafonctionnejegarde()
    clear_the_interface()
    print(f"{name_of_package_manager_menu} v{version_of_pkg_manager_menu}")
    print("Install:")
    install_package(input("Please enter the name of the package you would like to install: "))
    input("Press any enter to continue...")
    print_menu()
    menu() 

def uninstall():
    cafonctionnejegarde()
    clear_the_interface()
    print(f"{name_of_package_manager_menu} v{version_of_pkg_manager_menu}")
    print("Uninstall:")
    uninstall_package(input("Please enter the name of the package you would like to uninstall: "))
    print_menu()
    menu() 

def search():
    cafonctionnejegarde()
    clear_the_interface()
    print(f"{name_of_package_manager_menu} v{version_of_pkg_manager_menu}")
    print("Search:")
    search_package(input("Please enter the name of the package you would like to search for: "))
    print_menu()
    menu() 





def print_menu():
    global select, version_of_pkg_manager_menu, name_of_package_manager_menu
    if select < 1:
        select = 6
    if select > 6:
        select = 1


    clear_the_interface()
    print(f"{name_of_package_manager_menu} v{version_of_pkg_manager_menu}")
    print("Welcome to the easy-menu package manager!")
    print("\nPlease select an option from the list below:")

    for option in user_option:
        if user_option[option] == select:
            print(f">> {option}") # Highlight the current selected option
        else:
            print(f". {option}") # Display other options
    

try:
    print_menu()
    menu()

except KeyboardInterrupt:
    exit()


except Exception as e:
    print(f"An error occurred: {e}")
    input("Press enter to continue...")
    time.sleep(1)
    clear_the_interface()
    menu()
