try:
    import defs.install as install
    import json
    import os
 
if os.name == 'nt':
    import library.nicray.keyboard.keyboard_windows as keyboard
else:
    import library.jasonrdsouza.key_detect_for_linux as keyboard

def choice_packages():
    global user_index
    user_index = 1

    while True:
        key = keyboard.get_keyboard_input()
        print(key)

        package_count = count_packages()

        if key == "arrow_down":
            user_index += 1

            if user_index > package_count:
                user_index = 1

            display_packages(user_index)

        elif key == "arrow_up":
            user_index -= 1

            if user_index < 1:
                user_index = package_count

            display_packages(user_index)

        elif key == "enter":
            display_packages(user_index, enter=True)



def count_packages():
    count = 0

    for file in os.listdir(".PKGLIST"):
        if file.endswith(".json"):
            with open(f".PKGLIST/{file}", "r") as f:
                data = json.load(f)

            for package in data:
                if os.name == package["operating_system"]:
                    count += 1

    return count




def display_packages(user_index, enter=False):
    clear()
    print("Use the arrow keys to move the cursor (don't worry, an exit option will be added).\n\n")

    i = 1

    for file in os.listdir(".PKGLIST"):
        # Only process JSON package list files
        if file.endswith(".json"):
            # Open and load the current package list
            with open(f".PKGLIST/{file}", "r") as f:
                data = json.load(f)

            # Display every compatible package name in the list
            for package in data:
                if os.name == package["operating_system"]:
                    if i == user_index and enter:
                        clear()
                        install.install(package["name"])
                    elif i == user_index:
                        print("-> " + package["name"])
                    else:
                        print(package["name"])

                    i += 1
def clear():
    os.system("cls" if os.name == "nt" else "clear")

try:
    display_packages(user_index=1, enter=False)
    choice_packages()
except Exception as error: print(f"An error occurred: {error}")