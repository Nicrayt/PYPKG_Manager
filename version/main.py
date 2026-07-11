try:
    from upgrade_all_pkg_list import *
    from config_variable import *
    from uninstall_pkg import *
    from download_pkg import *
    from install_pkg import *
    from search_pkg import *
    from upgrade import *
    import argparse
    import os
except (ImportError, ModuleNotFoundError):  print("Error: The required modules are not installed or not found."); exit()

if os.path.exists(f"{default_save_pkg_list_dir}/up.json"):  
    os.remove(f"{default_save_pkg_list_dir}/up.json")
os.makedirs(default_save_pkg_list_dir, exist_ok=True)
os.makedirs(default_save_pkg_dir, exist_ok=True)

arg_parser = argparse.ArgumentParser()
# Get a file from the Internet using a URL
arg_parser.add_argument("-g", "--get", type=str, help="""Download a file from the Internet. Usage example: "python main.py -g "https://example.com/file.txt" -n "hey.txt" " to download the file.txt from the URL with the name "hey.txt".""")
arg_parser.add_argument("-n", "--name", type=str, help="""Name the file you want to download. Usage example: "python main.py -g "https://example.com/file.txt" -n "hey.txt" " to download the file.txt from the URL with the name "hey.txt".""")

# Get a PKG from list of pkg or Uninstall it
arg_parser.add_argument("-i", "--install", type=str, help="""Install a PKG from all the list of pkg. Usage example: "python main.py -i "The name of your package" ".""")
arg_parser.add_argument("-se", "--search", type=str, help="""Search a PKG from all the list of pkg. Usage example: "python main.py -se "The name of your package" ".""")
arg_parser.add_argument("-rm", "--uninstall", type=str, help="""Uninstall a PKG from all the list of pkg. Usage example: "python main.py -rm "The name of your package"".""")


# Store_True
arg_parser.add_argument("-up", "--upgrade", action="store_true", help="""Upgrade the package. Usage example: "python main.py -up".""")
arg_parser.add_argument("-noconfirm", "--noconfirm", action="store_true", help="""No confirm when you install a pkg or upgrade pypkg. Usage example: "python main.py -up -noconfirm" or "python main.py -i "The name of your package" -noconfirm".""")
# arg_parser.add_argument("-upl", "--upgrade-list", action="store_true", help="""Upgrade all packages list. Usage example: "python main.py -upl".""")

    # User interface
arg_parser.add_argument("-verppkg", "--versionppkg", action="store_true", help="""Show the version of pypkg.""")
arg_parser.add_argument("-menu", "--menu", action="store_true", help="""Show the version of pypkg.""")
arg_parser.add_argument("-noshow", "--noshow", action="store_false", help="""No show when you install a pkg and other. Usage example: "python main.py -i "The name of your package" -noshow".""")

args = arg_parser.parse_args()

try:
# All aboute pkg
    if args.get: # Get package.
        download_pkg(args.get, args.name)

    elif args.upgrade: # Upgrade PyPKG
        default_upgrade(args.noconfirm)

    elif args.install: # Install pkg
        install_package(args.install, args.noconfirm, args.noshow)
    
    elif args.search: # Search pkg
        search_package(args.search)

    elif args.uninstall: # Uninstall pkg
        uninstall_pkg(args.uninstall, args.noconfirm)

# Not importante, but it's important for the user experience.
    elif args.versionppkg: # Just show the version of PKG Manager
        print(f"""The current version of {name_of_package_manager} is "v{version_of_pkg_manager}".""") # Print the current version of PyPKG

    elif args.menu:
        from menu import *

# Not implemented yet.
#   if args.update: # Update PyPKG Manager
#       default_upgrade(args.noconfirm)

# In the next version we will be able to upgrade all list of packages. 
#    if args.upgrade_list:
#        upgradeallpkg()


# if nothing is entered.
    else: # show the help menu.
        arg_parser.print_help()
        try:
            input("Press enter to continue...")
        except:
            exit()

except KeyboardInterrupt: print("")
except Exception as e: print(f"Error: {e}") # Print the error message