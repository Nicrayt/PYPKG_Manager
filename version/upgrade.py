try:
    import requests
    import json
    import argparse
except (ImportError, ModuleNotFoundError):  print("Error: module is not installed. Please install it to run this script."); exit()

arg_parser = argparse.ArgumentParser()
arg_parser.add_argument("-f", "--force", type=str, help="""force upgrade with url""")
args = arg_parser.parse_args()

def force_upgrade(url="https://pypkg-manager.vercel.app/up.json"):
    print("Force upgrade mode activate")
    try:
        print("Downloading the upgrade list...")
        req = requests.get(url)
        with open("up.json", "wb") as f:
            f.write(req.content)

        with open("up.json", "r") as upgrade_file:
            upgradelist = json.load(upgrade_file)

        usrchoice = input("Force upgrade ? Y or N > ").lower().strip()

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
    except (UnicodeDecodeError, UnicodeTranslateError, json.JSONDecodeError):
        print("\nThe upgrade list is not an upgrade list")


def default_upgrade():
    from config_variable import base_upgrade_link, version_of_pkg_manager
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


if type(args.force) == str:
    force_upgrade(args.force)
else:
    default_upgrade()