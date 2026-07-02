#!/usr/bin/env python
from config_variable import *
import argparse

arg_parser = argparse.ArgumentParser()

arg_parser.add_argument("-dfpkg", "--download-default-list", action="store_true", help="Download the default PKG list and upgrade it")
arg_parser.add_argument("-g", "--get", action="store_true", help="Download a PKG list")
arg_parser.add_argument("-up", "--upgrade", action="store_true", help="Download the new version of PKG Manager (Not safe now but its work).")
arg_parser.add_argument("-chalog", "--changelog", action="store_true", help="If you want to see the change log.")
arg_parser.add_argument("-u", "--url", type=str, help="URL of the PKG list")

arg_parser.add_argument("-n", "--name", type=str, default=base_pkg_filename, help="Name")
arg_parser.add_argument("-s", "--show", action="store_true", help="Show the content of the PKG list")

arg_parser.add_argument("-sl", "--selist", type=str, default=base_pkg_filename, help="Name of the PKG list to list")
arg_parser.add_argument('-se', '--searchpkg', type=str, help="Search PKG on PKG list")
arg_parser.add_argument("-i", "--install", type=str, help="Install a PKG from the PKG list")

args = arg_parser.parse_args()

if args.get:
    from def_download import *
    downloadpkg(args.url, args.name, args.show)

elif args.install:
    from def_install_package import *
    installpkg(package_list_file_name=args.selist, name_the_pkg=args.install)

elif args.download_default_list:
    from def_download import *
    downloadpkg(url=default_link_list, name="base.json", view=False)

elif type(args.searchpkg) == str:
    from def_search_package import *
    searchpkg(package_list_file_name=args.selist, search_name=args.searchpkg)

elif args.upgrade:
    from upgrade import *

elif args.changelog:
    print(change_log)
    input("Press Enter to exit...")

else:
    arg_parser.print_help()
    try:
        input("Press Enter to exit...")
    except KeyboardInterrupt:
        exit()
