from download_pkg import *
from config_variable import *
import os
import json


def install_pkg(pkg_name:str=None, noconfirm=False):
    try:
        pkg_found = False
        pkg_compatible = False
        download_pkg(default_link_list, "base.json", default_save_pkg_list_dir, True)            # Download the default pkg list
        for file in os.listdir(default_save_pkg_list_dir):                                      # Loop through the files in the directory
            if file.endswith(".json"):                                                          # If the file finished with a .json
                with open(f"{default_save_pkg_list_dir}/{file}", 'r') as f:                     # if yes open the file
                    pkg_list = json.load(f)                                                     # load the json file in dict
                    for paquet in pkg_list:                                                     # Loop through the packages in the json file
                        if paquet["pkgname"] == pkg_name:
                            pkg_found = True
                            if paquet["plateforme"] == os.name:                                 # If the platform is the same as the system
                                pkg_compatible = True
                                print("-" * 10 + name_of_package_manager + "-" * 10)
                                print(f"PKG Name     : {paquet['pkgname']}")
                                print(f"PKG Version  : {paquet['pkgversion']}")
                                print(f"File Name    : {paquet['pkgfilename']}")
                                print(f"Platform     : {paquet['plateforme']}")
                                print(f"Bits         : {paquet['bits']}bits")
                                print(f"Description  : {paquet['description']}")
                                print(f"URL          : {paquet['url']}\n")

                                try:
                                    if not noconfirm:
                                        usrchoice = input("You want to install it ?: Y or N  > ").lower().strip()
                                        print("")
                                        if usrchoice in ["y", "yes"]:
                                            download_pkg(paquet['url'], paquet['pkgfilename'])
                                            return
                                        else:
                                            break
                                    elif noconfirm:
                                        download_pkg(paquet['url'], paquet['pkgfilename'])
                                        return
                                except KeyboardInterrupt:
                                    exit()

        if pkg_found and not pkg_compatible:
            print("Package is not compatible with your system.")
        if not pkg_found:
            print("Package not found")
    
    except FileNotFoundError: print(f"Error: You didn't specify a name for your file. or you dind't specify the pkglist"); exit()
    except (requests.HTTPError, requests.ConnectionError, requests.ReadTimeout, requests.Timeout): print(f"Error: 404, the file you want to download is unreachable.") ; exit()
    except (requests.URLRequired, requests.exceptions.MissingSchema): print(f"Error: You did not specify a URL, or the one you specified is incorrect or misspelled.") ; exit()
    except KeyboardInterrupt: exit()
