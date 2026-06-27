from alldef import *

def listpkg(name_pkglist=base_pkg_filename):
    try:
        input("This script is deprecated. Press Enter if you really want to run it, or press Ctrl+C to exit. Use -il for an interactive PKG list.")
    except KeyboardInterrupt:
        exit()  
    try:
        with open(name_pkglist, "r") as file:
            pkglist = json.load(file)

        for paquet in pkglist:
            print("-"*20)
            print(f"PKG Name : {paquet['pkgname']}")
            print(f"Description   : {paquet['description']}")
            print("")

    except (FileNotFoundError, FileExistsError):
        print("You must either specify a list of packages or install the default one -dfpkg.")
    except KeyboardInterrupt:
        exit()
    except:
        print("An error occurred.")