### Importation ###
try:
    # Import all required modules for PyPKG
    import os
    import argparse
    import defs.search
    import defs.install
    import defs.rm_package
    import defs.list
    import defs.run
    import defs.update_package_list
    import defs.add_repository
except KeyboardInterrupt: exit()
except (ImportError, ImportWarning) as error: print(f"You do not have the necessary libraries to run PyPKG : {error}")
except Exception as error: print(f"An error occurred while importing libraries: {error}")

def main():
    ### Create folders and file ###
    try:
        # Create the package installation directory if it does not already exist
        os.makedirs(".PKG", exist_ok=True)

        # Create the package list directory if it does not already exist
        os.makedirs(".PKGLIST", exist_ok=True)

        found = False

        for file in os.listdir("."):
            if file == "repositories.json":
                found = True
        if not found:
            with open("repositories.json", "w") as file:
                file.write("""{\n    "repositories": [\n        "https://pypkg-manager.vercel.app/list/lists.json"\n    ]\n}\n""")

    except (PermissionError):
        # Display an operating system specific permission error
        os.name == "posix" if print("To be able to write, you must be logged in as root or a sudo.") else print("You do not have permission to write here... You must run PyPKG as an administrator.")


    ### argparse ###
    # Create the command-line argument parser
    parser = argparse.ArgumentParser("PyPKG Manager", description="A litle PKG Manager in python")

    parser.add_argument("-se", "--search", type=str, help="Search a package from the PyPKG repository.") # Option to search a package
    parser.add_argument("-i", "--install", type=str, help="Install a package from the PyPKG repository.") # Option to install a package
    parser.add_argument("-rm", "--uninstall", type=str, help="Remove an installed package from the system.") # Option to uninstall a package
    parser.add_argument("-update-list", "--update-list", action="store_true", help="Update all available package lists.") # Option to update all package lists
    parser.add_argument("-show", "--show", action="store_true", help="Display detailed operation information.") # Option to show logs
    parser.add_argument("-l", "--list", type=str, help="HELP...") # Option to list all available packages
    parser.add_argument("-y", "--noconfirm", action="store_true", help="Skip confirmation prompts during operations.") # Option to disable confirmations
    parser.add_argument("-run", "--run-package", type=str, help="Run your installed Package (Only for Windows).")



    parser.add_argument("-ar", "--add-repository", type=str, help="Add another repository.") # Add Another list of packages
    parser.add_argument("-rp", "--remove-repository", type=str, help="Remove repository.")


    # Parse command-line arguments
    args = parser.parse_args()


    # Execute the requested action
    try:
        if args.install:
            defs.install.install_package(package_name=args.install, noconfirm=args.noconfirm)

        elif args.search:
            defs.search.search_package(package_name=args.search, noconfirm=args.noconfirm)

        elif args.update_list:
            defs.update_package_list.update_list(show=args.show, noconfirm=args.noconfirm)

        elif args.uninstall:
            defs.rm_package.remove_package(args.uninstall)

        elif args.list:
            defs.list.list(args.list)

        elif args.add_repository:
            defs.add_repository.add_repository(args.add_repository)

        elif args.remove_repository:
            defs.add_repository.remove_repository(args.remove_repository)

        elif args.run_package:
            defs.run.run_package(args.run_package)

        else:
            try:input(f"{parser.print_help()}\nPress Enter to continue: ")
            except: exit()

    except KeyboardInterrupt:
        exit()

    except (PermissionError):
        # Display an operating system specific permission error
        os.name == "posix" if print("To be able to write, you must be logged in as root or a sudo.") else print("You do not have permission to write here... You must run PyPKG as an administrator.")
        exit()

    except Exception as error:
        print(f"An error occured: {error}")


    try: # Remove the temporary master list file
        if os.path.exists(".TMP"):
            for file in os.listdir(".TMP"):
                os.remove(f".TMP/{file}")

            # Remove the temporary directory
            os.rmdir(".TMP")
    except: 
        print("The temporary file cannot be deleted; you must delete it manually.")


if __name__ == "__main__":
    main()