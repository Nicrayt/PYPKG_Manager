try:
    import requests
    import json
    import os
except (ImportError, ModuleNotFoundError):  print("Error: module is not installed. Please install it to run this script."); exit()

try:
    base_upgrade_link = "https://pypkg-manager.vercel.app/up.json"


    print("Downloading the upgrade list...")



    req = requests.get(base_upgrade_link)
    with open("up.json", "wb") as f:
        f.write(req.content)

    os.system('cls' if os.name == 'nt' else 'clear')

    with open("up.json", "r") as upgrade_file:
        upgradelist = json.load(upgrade_file)

    version_new_update = upgradelist[0]["ver"]

    print(f"PyPKG Manager Installer\nA package manager to install applications from alternative links (mirrors)")
    usrchoice = input(f"Install the v{version_new_update}?\nY or N >").lower().strip()

    if usrchoice == "yes" or usrchoice == "y":
        os.system('cls' if os.name == 'nt' else 'clear')
        for paquet in upgradelist:
            print(f"Installing : {paquet['filename']}...")
            req = requests.get(paquet['url'])

            with open(paquet['filename'], 'wb') as fichier:
                    fichier.write(req.content)

        print("Finished with Success!")
        input("PyPKG Manager Installer Finished> ")
        if os.path.exists("installer.py"):
            os.remove("installer.py")
    else:
        exit()

except (json.JSONDecodeError, requests.ConnectionError, requests.ConnectTimeout, requests.HTTPError):
    print("An error occurred with the update file, or you do not have an Internet connection.")
except KeyboardInterrupt:
    if os.path.exists("up.json"):
        os.remove("up.json")
    exit()

if os.path.exists("up.json"):
    os.remove("up.json")