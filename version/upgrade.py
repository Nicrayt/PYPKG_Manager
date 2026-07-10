### Upgrade Script for PKG Manager Version 2.0
try:
    import requests
    import json
    from config_variable import base_upgrade_link, version_of_pkg_manager # base_upgrade_link is the link where we get the list of packages and their versions
    from download_pkg import *
except (ImportError, ModuleNotFoundError):  print("Error: module is not installed. Please install it to run this script."); exit()

def default_upgrade(noconfirm=False): # For the next version Not FINISHED
    try:
        print("Download upgrade list...") # Donwload the list of pkg
        download_pkg(base_upgrade_link, "up.json", ".", True)
        upgrade_json = json.load(open("up.json", "r"))

        print("Cheking for new versions...")

        latest_version:str = upgrade_json[0]['ver']
        changelog:str = upgrade_json[0]['changelog']

        if latest_version == version_of_pkg_manager: # Check the version of pkg manager
            print(f"Your PKG Manager is up to date. Version {version_of_pkg_manager}")
            exit()
        else:
            print(f"New versions available! {latest_version}\n Change Log:\n{changelog}")
            
            if noconfirm or input("You want to upgrade? (y/n): ").strip().lower() == 'y': # Upgrade
                print("Downloading new version...")
                for paquet in upgrade_json:
                    download_pkg(url=paquet["url"],pkg_file_name=paquet["filename"], path=".", dont_show=True)

                print(f"\nUpgrade successful! Version {latest_version} installed.")
            else: # Exit
                print("Upgrade cancelled.")

    except (requests.HTTPError, requests.ConnectionError, requests.ReadTimeout, requests.Timeout): print("\nError: 404, the file you want to download is unreachable.")
    except KeyboardInterrupt: print("\nUpgrade cancelled.")
    except Exception as e: print(f"\nError: {e}")