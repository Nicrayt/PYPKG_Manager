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

version_of_pkg_manager_menu = "0.3"
name_of_package_manager_menu = "easy-menu"
user_index = 0

def clear_the_interface():
    os.system('cls' if os.name == 'nt' else 'clear') # Clear the screen

def menu():
    global user_index
    clear_the_interface()

    menu_print(user_index_menu=user_index)

    while True:
        event = keyboard.read_event()

        if event.event_type == keyboard.KEY_DOWN:
            if keyboard.is_pressed('up'):
                user_index -= 1
                time.sleep(0.1)
                clear_the_interface()
                menu_print(user_index_menu=user_index)


            elif keyboard.is_pressed('down'):
                user_index += 1
                time.sleep(0.1)
                clear_the_interface()
                menu_print(user_index)
            
            elif keyboard.is_pressed('enter'):
                menu_print(user_index_menu=user_index, enter=True)
                menu_print(user_index)


def menu_print(user_index_menu, enter=False):
    global user_index
    if user_index < 0:
        user_index = 4
        user_index_menu = 4
    if user_index > 4:
        user_index = 0
        user_index_menu = 0



    if user_index_menu == 0:
        print(f"""Welcome to {name_of_package_manager_menu} "v{version_of_pkg_manager_menu}".\n""")
        print("-> Install a Package\nSearch a Package\nUninstall a package\nUpgrade PyPKG\n\nExit")
        if enter:
            input("Press enter to continue...")
            clear_the_interface()
            print("Install a Package")
            install_package(pkg_name=input("Name of Package you want to install: "), noconfirm=False)
            input("Press enter to continue...")
            clear_the_interface()
            user_index = 0


    if user_index_menu == 1:
        print(f"""Welcome to {name_of_package_manager_menu} "v{version_of_pkg_manager_menu}".\n""")
        print("Install a Package\n-> Search a Package\nUninstall a package\nUpgrade PyPKG\n\nExit")
        if enter:
            input("Press enter to continue...")
            clear_the_interface()
            print("Search a Package")
            search_package(pkg_name=input("Name of Package you want to install: "))
            input("Press enter to continue...")
            clear_the_interface()

    if user_index_menu == 2:
        print(f"""Welcome to {name_of_package_manager_menu} "v{version_of_pkg_manager_menu}".\n""")
        print("Install a Package\nSearch a Package\n-> Uninstall a package\nUpgrade PyPKG\n\nExit")
        if enter:
            input("Press enter to continue...")
            clear_the_interface()
            print("Uninstall a package")
            uninstall_pkg(pkg_name=input("Name of Package you want to uninstall: "), noconfirm=False)
            input("Press enter to continue...")
            clear_the_interface()


    if user_index_menu == 3:
        print(f"""Welcome to {name_of_package_manager_menu} "v{version_of_pkg_manager_menu}".\n""")
        print("Install a Package\nSearch a Package\nUninstall a package\n-> Upgrade PyPKG\n\nExit")
        if enter:
            input("Press enter to continue...")
            clear_the_interface()
            default_upgrade()
            return

    if user_index_menu == 4:
        print(f"""Welcome to {name_of_package_manager_menu} "v{version_of_pkg_manager_menu}".\n""")
        print("Install a Package\nSearch a Package\nUninstall a package\nUpgrade PyPKG\n\n-> Exit")
        if enter:
            clear_the_interface()
            print("Goodbye!")
            time.sleep(1)
            exit()

try:
    if os.name == "nt":
        menu()

    else:
        if input("I do not recommend running this on a system other than Windows... The `keyboard` library might not work. Are you sure you want to launch the interface? (y/n): ").strip().lower() == 'y':
            menu()

    


except KeyboardInterrupt:
    print("Exiting the program")
    time.sleep(1)
    clear_the_interface()


except Exception as e:
    print(f"An error occurred: {e}")
    input("Press enter to continue...")
    time.sleep(1)
    clear_the_interface()
    menu()
