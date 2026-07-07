### Upgrade Script for PKG Manager Version 2.0
try:
    import requests
    import json
    from config_variable import base_upgrade_link, version_of_pkg_manager # base_upgrade_link is the link where we get the list of packages and their versions
    from download_pkg import *
except (ImportError, ModuleNotFoundError):  print("Error: module is not installed. Please install it to run this script."); exit()

def default_upgrade():
    try:
        print("Download upgrade list...") # Donwload the list of pkg
        upgrade_list = requests.get(base_upgrade_link)
        upgrade_json = json.load(upgrade_list)
        print("Cheking for new versions...")

        latest_version = upgrade_json[0]["ver"]

        if latest_version == version_of_pkg_manager: # Check the version of pkg manager
            print(f"Your PKG Manager is up to date. Version {version_of_pkg_manager}")
            exit()
        else:
            print(f"New versions available!")
            user_input = input("You want to upgrade? (y/n): ").strip().lower()
            if user_input == 'y' or user_input == 'yes': # Upgrade
                print("Downloading new version...")
                for upgrade in upgrade_json['url']:
                    downloadpkg(upgrade, pkg_name=upgrade_json["filename"], path=".", dont_show=True)
                print(f"\nUpgrade successful! Version {version_of_pkg_manager}")
            else: # Exit
                print("Upgrade cancelled.")

    except (requests.HTTPError, requests.ConnectionError, requests.ReadTimeout, requests.Timeout): print("\nError: 404, the file you want to download is unreachable.")
    except KeyboardInterrupt: print("\nUpgrade cancelled.")
    except Exception as e: print(f"\nError: {e}")