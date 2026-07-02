from config_variable import *
import json
try:    import requests
except (ImportError, ModuleNotFoundError):  print("Error: The 'requests' module is not installed. Please install it to run this script."); exit()


try:
    print("Downloading the upgrade list...")
    req = requests.get(base_upgrade_link)
    with open("up.json", "wb") as f:
        f.write(req.content)

    with open("up.json", "r") as upgrade_file:
        upgradelist = json.load(upgrade_file)

    version = upgradelist[0]["ver"]
    change_log_new_update = upgradelist[0]["changelog"]

    if version == ver:
        usrchoice = input(f"You are already on the latest version {ver}. Do you want to reinstall the latest version {version}? Y or N > ").lower().strip()
    else:
        usrchoice = input(f"Do you want to update to the v{version}? The current version is {ver}. \n Change Log: \n{change_log_new_update}  \nY or N >").lower().strip()

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
    print("The update was interrupted; this may not be serious, but run '-up' again to restart the update.")
