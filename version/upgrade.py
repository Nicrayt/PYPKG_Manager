### Upgrade Script for PKG Manager Version 2.0
try:
    import requests
    import json
    from config_variable import base_upgrade_link, version_of_pkg_manager # base_upgrade_link is the link where we get the list of packages and their versions
    from download_pkg import *
except (ImportError, ModuleNotFoundError):  print("Error: module is not installed. Please install it to run this script."); exit()

def default_upgrade(): # For the next version Not FINISHED
    try:
        print("Download upgrade list...") # Donwload the list of pkg
        downloadpkg(base_upgrade_link, "up.json", ".", True)
        upgrade_json = json.load(open("up.json", "r"))

        print("Cheking for new versions...")
        latest_version:str = upgrade_json["ver"]

        if latest_version == version_of_pkg_manager: # Check the version of pkg manager
            print(f"Your PKG Manager is up to date. Version {version_of_pkg_manager}")
            exit()
        else:
            print(f"New versions available! {latest_version}")
            user_input = input("You want to upgrade? (y/n): ").strip().lower()
            if user_input == 'y' or user_input == 'yes': # Upgrade
                print("Downloading new version...")
                for paquet in upgrade_json['filename']:
                    print(f"Upgrading : {paquet['filename']}...")
                    req = requests.get(paquet['url'])

                    with open(paquet['filename'], 'wb') as fichier:
                            fichier.write(req.content)
                print(f"\nUpgrade successful! Version {version_of_pkg_manager}")
            else: # Exit
                print("Upgrade cancelled.")

    except (requests.HTTPError, requests.ConnectionError, requests.ReadTimeout, requests.Timeout): print("\nError: 404, the file you want to download is unreachable.")
    except KeyboardInterrupt: print("\nUpgrade cancelled.")
    except Exception as e: print(f"\nError: {e}")


def upgrade_old():
    try:
        print("Downloading the upgrade list...")
        req = requests.get(base_upgrade_link)
        with open("up.json", "wb") as f:
            f.write(req.content)

        with open("up.json", "r") as upgrade_file:
            upgradelist = json.load(upgrade_file)

        version_new_update = upgradelist[0]["ver"]
        change_log_new_update = upgradelist[0]["changelog"]

        if version_new_update == version_of_pkg_manager:
            usrchoice = input(f"You are already on the latest version {version_of_pkg_manager}. Do you want to reinstall the latest version {version_new_update}? Y or N > ").lower().strip()
        else:
            usrchoice = input(f"Do you want to update to the v{version_new_update}? The current version is {version_of_pkg_manager}. \n Change Log: \n{change_log_new_update}  \nY or N >").lower().strip()

        if usrchoice == "yes" or usrchoice == "y":

            for paquet in upgradelist:
                print(f"Upgrading : {paquet['filename']}...")
                req = requests.get(paquet['url'])

                with open(paquet['filename'], 'wb') as fichier:
                        fichier.write(req.content)

            print("Finished with Success!")
        else:
            exit()

    except (requests.HTTPError, requests.ConnectionError, requests.ReadTimeout, requests.Timeout):
        print("Error: 404, the file you want to download is unreachable.")
    except KeyboardInterrupt:
        print("\nThe update was interrupted; this may not be serious, but run '-up' again to restart the update.")
