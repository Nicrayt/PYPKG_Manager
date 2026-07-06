try:
    from config_variable import *
    from upgradeallpkg import *
    from download_pkg import *
    from install_pkg import *
    from search_pkg import *
    import argparse
    import os
except (ImportError, ModuleNotFoundError):  print("Error: The required modules are not installed or not found."); exit()

os.makedirs(default_save_pkg_list_dir, exist_ok=True)
os.makedirs(default_save_pkg_dir, exist_ok=True)

arg_parser = argparse.ArgumentParser()

# Get a file from the Internet using a URL
arg_parser.add_argument("-g", "--get", type=str, help="""Download a file from the Internet. Usage example: "python main.py -g "https://example.com/file.txt" -n "hey.txt" " to download the file.txt from the URL with the name "hey.txt".""")
arg_parser.add_argument("-n", "--name", type=str, help="""Name the file you want to download. Usage example: "python main.py -g "https://example.com/file.txt" -n "hey.txt" " to download the file.txt from the URL with the name "hey.txt".""")

# Get a PKG from list of pkg
arg_parser.add_argument("-i", "--install", type=str, help="""Install a PKG from all the list of pkg. Usage example: "python main.py -i "The name of your package" ".""")
arg_parser.add_argument("-se", "--search", type=str, help="""Search a PKG from all the list of pkg. Usage example: "python main.py -se "The name of your package" ".""")



# Store_True
arg_parser.add_argument("-up", "--upgrade", action="store_true", help="""Upgrade the package. Usage example: "python main.py -up".""")
# arg_parser.add_argument("-upl", "--upgrade-list", action="store_true", help="""Upgrade all packages list. Usage example: "python main.py -upl".""")


args = arg_parser.parse_args()


try:
    if args.get: # Get package.
        downloadpkg(args.get, args.name)


    if args.upgrade: # Upgrade PyPKG
        from upgrade import *

    if args.install: # Install pkg
        install_pkg(args.install)
    
    if args.search: # Search pkg
        search_pkg(pkg_name=args.search)







# In the next version
#    if args.upgrade_list:
#        upgradeallpkg()


except Exception as e: print(f"An error occured: {e}"); exit()
