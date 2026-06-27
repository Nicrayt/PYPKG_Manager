import argparse
from alldef import *
from allvariable import *
from abandon import *

arg_parser = argparse.ArgumentParser()
# Universal
arg_parser.add_argument("-dfpkg", "--download-default-list", action="store_true", help="Download the default PKG list and upgrade it")
arg_parser.add_argument("-g", "--get", action="store_true", help="Download a PKG list")
arg_parser.add_argument("-up", "--upgrade", action="store_true", help="Download the new version of PKG Manager (Not safe now but its work).")
arg_parser.add_argument("-chalog", "--changelog", action="store_true", help="If you want to see the change log.")
arg_parser.add_argument("-u", "--url", type=str, help="URL of the PKG list")

arg_parser.add_argument("-n", "--name", type=str, default=base_pkg_filename, help="Name")
arg_parser.add_argument("-s", "--show", action="store_true", help="Show the content of the PKG list")

arg_parser.add_argument("-il", "--interactlist", action="store_true", help="List all PKG in the PKG list interactivily")
arg_parser.add_argument("-sl", "--selist", type=str, default=base_pkg_filename, help="Name of the PKG list to list")
arg_parser.add_argument("-se", "--searchpkg", action="store_true", help="Search PKG on PKG list (no finished but it safe)")
arg_parser.add_argument("-i", "--install", type=str, help="Install a PKG from the PKG list")


args = arg_parser.parse_args()

if args.get:
    downloadpkg(args.url, args.name, args.show)

elif args.install:
    installpkg(args.selist, args.install)

elif args.download_default_list:
    downloadpkg(url=default_link_list, name_pkglist=args.selist)

elif args.interactlist:
    interactivelistpkg(args.selist)

elif args.searchpkg:
    searchpkg(name_pkglist=args.selist)

elif args.upgrade:
    upgrade()

elif args.changelog:
    print(change_log)

else:
    arg_parser.print_help()
    try:
        input("Press enter to exit...")
    except KeyboardInterrupt:
        exit()
