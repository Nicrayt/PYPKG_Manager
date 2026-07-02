from def_download import *
import json

try:    import requests
except (ImportError, ModuleNotFoundError):  print("Error: The 'requests' module is not installed. Please install it to run this script."); exit()

def searchpkg(package_list_file_name, search_name=None):
    try:
        with open(package_list_file_name, "r") as file:
            in_package_list = json.load(file)

        for paquet in in_package_list:
            if search_name in paquet['pkgname']:
                print("-"*10 + name_of_package_manager + "-"*10)
                print(f"PKG Name : {paquet['pkgname']}")
                print(f"File Name : {paquet['pkgfilename']}")
                print(f"Description   : {paquet['description']}")
                print(f"URL   : {paquet['url']}")
                print("")

                try:

                    usrchoice = input("press i if you want to install it > ").lower().strip()
                    print("")
                    if usrchoice == "i":
                        downloadpkg(paquet['url'], paquet['pkgfilename'], False)
                        break
                    elif usrchoice == "exit":
                        break

                except KeyboardInterrupt:   break

    except FileNotFoundError:   print(f"Error: You didn't specify a name for your file. or you dind't specify the pkglist")
    except (requests.HTTPError, requests.ConnectionError, requests.ReadTimeout, requests.Timeout):  print(f"Error: 404, the file you want to download is unreachable.")
    except (requests.URLRequired, requests.exceptions.MissingSchema):   print(f"Error: You did not specify a URL, or the one you specified is incorrect or misspelled.")
    except KeyboardInterrupt:   exit()
