try: 
    from def_download import *
    import json
    import os
except (ImportError, ModuleNotFoundError):  print("Error: The required modules are not installed or not found."); exit()

try:    import requests
except (ImportError, ModuleNotFoundError):  print("Error: The 'requests' module is not installed. Please install it to run this script."); exit()

def searchpkg(package_list_file_name:str, search_name:str=None):
    try:
        with open(package_list_file_name, "r") as file:
            in_package_list = json.load(file)

        for paquet in in_package_list:
            if search_name.strip().lower() in paquet['pkgname'].strip().lower() and os.name == paquet['plateforme']:
                print("-"*10 + name_of_package_manager + "-"*10)
                print(f"PKG Name    : {paquet['pkgname']}")
                print(f"File Name   : {paquet['pkgfilename']}")
                print(f"Platform    : {paquet['plateforme']}")
                print(f"Bits        : {paquet['bits']}bits")
                print(f"Description : {paquet['description']}")
                print(f"URL         : {paquet['url']}")
                print("")

                try:

                    usrchoice = input("You want to install it ?: Y or N  > ").lower().strip()
                    print("")
                    if usrchoice == "y" or usrchoice == "yes":
                        downloadpkg(paquet['url'], paquet['pkgfilename'], False)
                        exit()
                    elif usrchoice == "exit":
                        exit()

                except KeyboardInterrupt:   exit()

        
        print(f"{search_name}: not found, in this PKG list: {package_list_file_name}")
        exit()
    except FileNotFoundError:   print(f"Error: You didn't specify a name for your file. or you dind't specify the pkglist")
    except (requests.HTTPError, requests.ConnectionError, requests.ReadTimeout, requests.Timeout):  print(f"Error: 404, the file you want to download is unreachable.")
    except (requests.URLRequired, requests.exceptions.MissingSchema):   print(f"Error: You did not specify a URL, or the one you specified is incorrect or misspelled.")
    except KeyboardInterrupt:   exit()
