try:
    from upgrade import default_upgrade
    from config_variable import *
    import argparse
    import os
except (ImportError, ModuleNotFoundError):  print("Error: The required modules are not installed or not found."); exit()

os.makedirs(save_pkg_dir, exist_ok=True)

arg_parser = argparse.ArgumentParser()

# Download default PKG list and upgrade it
arg_parser.add_argument("-dfpkgl", "--download-default-list", action="store_true", help="""Download the default PKG list and upgrade it""")

# All Log of Download Def
arg_parser.add_argument("-log", "--log", action="store_true", help="""When downloading something, you can use the `--log` flag to get a summary of everything that happened. Only work with the download def""")

# Get a file from the Internet using a URL
arg_parser.add_argument("-g", "--get", action="store_true", help="""Download a file from the Internet using a --url. Usage example: -g --url https://example.com/file.txt to download the file.txt from the URL.""")

# Upgrade the PKG Manager
arg_parser.add_argument("-up", "--upgrade", action="store_true", help="""Download the new version of PKG Manager. (You can launch it directly in case the version is broken.).""")

# Version of the PKG Manager
arg_parser.add_argument("-ver", "--versionpypkg", action="store_true", help="""This command tells you the pypkg version. Usage example: -ver to display the version of pypkg.""")

# URL to download a file from the Internet
arg_parser.add_argument("-u", "--url", type=str, help="""Often used for --get. Usage example: -g --url https://example.com/file.txt to download the file.txt from the URL.""")

# Name of the file to save the downloaded content
arg_parser.add_argument("-n", "--name", type=str, default="Next_time_use_--Name_for_your_download.pypkg", help="""Names the file downloaded via --get. Usage example: -g --url https://example.com/file.txt --name cool.txt to download the file.txt from the URL and save it as cool.txt.""")

# Show the contents of what you are downloading
arg_parser.add_argument("-s", "--show", action="store_true", help="""View the contents of what you are downloading. Usage example: -g --url https://example.com/file.txt --show to view the contents of file.txt while downloading it.""")

# Select the list of packets
arg_parser.add_argument("-sl", "--selist", type=str, default=base_pkg_filename, help="""Select the list of packets.""")

# Search for a package in a list of packages
arg_parser.add_argument('-se', '--searchpkg', type=str, help="""search for a package in a list of packages. Usage example: -s "package name" to search from the default package list, or use your own package list: -sl "packagelist.json" -se "search package" """)

# Install a package from a package list
arg_parser.add_argument('-i', '--install', type=str, help="""Install a package from a package list. Usage example: -i "package name" to install from the default package list, or use your own package list: -sl "packagelist.json" -i "package name" """)

args = arg_parser.parse_args()


try:
    if args.get:
        from def_download import *
        downloadpkg(url=args.url, name=args.name, view=args.show, log=args.log)

    elif args.install:
        from def_install_package import *
        installpkg(package_list_file_name=args.selist, name_the_pkg=args.install)

    elif args.download_default_list:
        from def_download import *
        downloadpkg(url=default_link_list, name="base.json", view=False, log=args.log)

    elif type(args.searchpkg) == str:
        from def_search_package import *
        searchpkg(package_list_file_name=args.selist, search_name=args.searchpkg)

    elif args.upgrade:
        default_upgrade()

    elif args.versionpypkg:
        print(f"""The current version is v{version_of_pkg_manager} and the name of this version is {name_of_package_manager}""")
        input("Press Enter to exit...")

    else:
        arg_parser.print_help()
        try:
            input("Press Enter to exit...")
        except KeyboardInterrupt:
            exit()

except (ImportError):
    print("An error occurred while importing one of the libraries.")


if os.path.exists("up.json"):
    os.remove("up.json")