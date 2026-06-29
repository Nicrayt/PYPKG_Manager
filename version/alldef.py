import json
import os
import requests
import zipfile
from allvariable import *

os.makedirs(save_pkg_dir, exist_ok=True)

 # Download All
def downloadpkg(url=default_link_list, name_pkglist="Please_use_-n_the_next_time", view=True, path=save_pkg_dir):
    try:
        if url == default_link_list or name_pkglist == "up.json":
            req = requests.get(default_link_list)
            open("base.json", "wb").write(req.content)
            print("Default Pkg list downloaded!")
        else:
            download = path.strip() + "/".strip() + name_pkglist.strip()
            req = requests.get(url)
            open(download, "wb").write(req.content)
            if view:
                print(req.text)
            elif ".zip" in name_pkglist:
                with zipfile.ZipFile(download, 'r') as easteregg:
                    easteregg.extractall(path.strip())
                    print("Unzip completed")
                    print("Finished with Success!")
            else:
                print("Finished with Success!")

    except FileNotFoundError:
        print(f"Error: You didn't specify a name for your file. or you dind't specify the pkglist")
    except (requests.HTTPError, requests.ConnectionError, requests.ReadTimeout, requests.Timeout):
        print(f"Error: 404, the file you want to download is unreachable.")
    except (requests.URLRequired, requests.exceptions.MissingSchema):
        print(f"Error: You did not specify a URL, or the one you specified is incorrect or misspelled.")
    except KeyboardInterrupt:
        exit()




 # Interactive list PKG
def interactivelistpkg(name_pkglist=base_pkg_filename):
    try:
        with open(name_pkglist, "r") as file:
            pkglist = json.load(file)

        for paquet in pkglist:
            os.system('cls' if os.name == 'nt' else 'clear')
            print("-"*20)
            print(f"PKG Name : {paquet['pkgname']}")
            print(f"File Name : {paquet['pkgfilename']}")
            print(f"Description   : {paquet['description']}")
            print(f"URL   : {paquet['url']}")
            print("")
            try:
                usrchoice = input("Press Enter for the Next pkg or i for install > ")
                if usrchoice == "i":
                    downloadpkg(paquet['url'], paquet['pkgfilename'], False)
                    break

            except KeyboardInterrupt:
                break
        print("finished")

    except FileNotFoundError:
        print(f"Error: You didn't specify a name for your file. or you dind't specify the pkglist")
    except (requests.HTTPError, requests.ConnectionError, requests.ReadTimeout, requests.Timeout):
        print(f"Error: 404, the file you want to download is unreachable.")
    except (requests.URLRequired, requests.exceptions.MissingSchema):
        print(f"Error: You did not specify a URL, or the one you specified is incorrect or misspelled.")
    except KeyboardInterrupt:
        exit()




 # Search PKG on a PKG List
def searchpkg(name_pkglist, name=None):
    try:
        with open(name_pkglist, "r") as file:
            pkglist = json.load(file)
        for paquet in pkglist:
            if name in paquet['pkgname']:
                os.system('cls' if os.name == 'nt' else 'clear')
                print("-"*20)
                print(f"PKG Name : {paquet['pkgname']}")
                print(f"File Name : {paquet['pkgfilename']}")
                print(f"Description   : {paquet['description']}")
                print(f"URL   : {paquet['url']}")
                print("")
                try:
                    usrchoice = input("press i if you want to install it > ").lower().strip()
                    if usrchoice == "i":
                        downloadpkg(paquet['url'], paquet['pkgfilename'], False)
                        break
                    elif usrchoice == "exit":
                        break
                except KeyboardInterrupt:
                    break

    except FileNotFoundError:
        print(f"Error: You didn't specify a name for your file. or you dind't specify the pkglist")
    except (requests.HTTPError, requests.ConnectionError, requests.ReadTimeout, requests.Timeout):
        print(f"Error: 404, the file you want to download is unreachable.")
    except (requests.URLRequired, requests.exceptions.MissingSchema):
        print(f"Error: You did not specify a URL, or the one you specified is incorrect or misspelled.")
    except KeyboardInterrupt:
        exit()




 # Install a PKG
def installpkg(name_pkglist=base_pkg_filename, name_pkg=None):
    try:
        with open(name_pkglist, "r") as file:
            pkglist = json.load(file)

        for paquet in pkglist:
            if paquet["pkgname"].strip().lower() == name_pkg.strip().lower():
                print("-"*10 + name + "-"*10)
                print(f"PKG Founded   : {paquet['pkgname']}")
                print(f"PKG version : {paquet['pkgversion']}")
                print(f"File Name : {paquet['pkgfilename']}")
                print(f"Description   : {paquet['description']}")
                print("")
                try:
                    usr = input("You want to install it ?: Y or n  > ").lower()
                    if usr == "y" or usr == "yes":
                        downloadpkg(paquet['url'], paquet['pkgfilename'], view=False)
                        break

                    elif usr == "ys" or usr == "yeshow":
                        downloadpkg(paquet['url'], paquet['pkgfilename'], view=True)
                        break
                except KeyboardInterrupt:
                    exit()
                else:
                    break
        else:
            print(f"{name_pkg}: not found, in this PKG list: {name_pkglist}")
        return
    except FileNotFoundError:
        print(f"Error: You didn't specify a name for your file. or you dind't specify the pkglist")
    except (requests.HTTPError, requests.ConnectionError, requests.ReadTimeout, requests.Timeout):
        print(f"Error: 404, the file you want to download is unreachable.")
    except (requests.URLRequired, requests.exceptions.MissingSchema):
        print(f"Error: You did not specify a URL, or the one you specified is incorrect or misspelled.")
    except KeyboardInterrupt:
        exit()



def upgrade():
    try:
        print("Downloading the upgrade list...")
        req = requests.get(base_upgrade_link)
        with open("up.json", "wb") as f:
            f.write(req.content)
            
        with open("up.json", "r") as upgrade_file:
            upgradelist = json.load(upgrade_file)

        for paquet in upgradelist:
            print(f"Upgrading : {paquet['filename']}...")
            downloadpkg(paquet['url'], paquet['filename'], view=False, path=".")
            
        print("Finished with Success!")

    except FileNotFoundError:
        print("Error: You didn't specify a name for your file. or you dind't specify the pkglist")
    except (requests.HTTPError, requests.ConnectionError, requests.ReadTimeout, requests.Timeout):
        print("Error: 404, the file you want to download is unreachable.")

 test_for_new_update = """I test the update"""
