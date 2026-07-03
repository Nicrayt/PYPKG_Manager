try:
    from config_variable import *
    from def_download import *
    import json
except (ImportError, ModuleNotFoundError):  print("Error: The required modules are not installed or not found."); exit()
try: import requests
except (ImportError, ModuleNotFoundError): print("Error: The 'requests' module is not installed. Please install it to run this script."); exit()

os_name = os.name


def installpkg(package_list_file_name:str=base_pkg_filename, name_the_pkg:str=None):
    try:
        with open(package_list_file_name, "r") as file:
            pkglist = json.load(file)

        compatible_packages = False
        package_found = False
        
        for paquet in pkglist:
            if name_the_pkg.strip().lower() == paquet["pkgname"].strip().lower():
                package_found = True  
                if os_name == paquet['plateforme']:
                    compatible_packages = True  

                    print("-" * 10 + name_of_package_manager + "-" * 10)
                    print(f"PKG Name     : {paquet['pkgname']}")
                    print(f"PKG Version  : {paquet['pkgversion']}")
                    print(f"File Name    : {paquet['pkgfilename']}")
                    print(f"Platform     : {paquet['plateforme']}")
                    print(f"Bits         : {paquet['bits']}bits")
                    print(f"Description  : {paquet['description']}")
                    print(f"URL          : {paquet['url']}\n")

                    try:
                        usrchoice = input("You want to install it ?: Y or N  > ").lower().strip()
                        print("")
                        if usrchoice in ["y", "yes"]:
                            downloadpkg(paquet['url'], paquet['pkgfilename'], view=False)
                            return
                        elif usrchoice in ["ys", "yeshow"]:
                            downloadpkg(paquet['url'], paquet['pkgfilename'], view=True)
                            return
                    except KeyboardInterrupt:
                        exit()

        if not package_found:
            print(f"{name_the_pkg}: not found, in this PKG list: {package_list_file_name}")
            exit()
            
        if package_found and not compatible_packages:
            print(f"the package {name_the_pkg} is not compatible with your OS: {os_name}")
            exit()

    except FileNotFoundError:
        print(f"Error: You didn't specify a name for your file. or you dind't specify the pkglist")
    except (requests.HTTPError, requests.ConnectionError, requests.ReadTimeout, requests.Timeout):
        print(f"Error: 404, the file you want to download is unreachable.")
    except (requests.URLRequired, requests.exceptions.MissingSchema):
        print(f"Error: You did not specify a URL, or the one you specified is incorrect or misspelled.")
    except KeyboardInterrupt:
        exit()
