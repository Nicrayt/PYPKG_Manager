try:
    import json
    import classes.paquets
    from defs.install import *
    import defs.user_confirmations
    import os
except ImportError as error:
    print(f"You do not have the necessary libraries to run PyPKG : {error}")

def install_package(package_name: str = None, noconfirm: bool = False, noshow: bool = False) -> None:
    # Track whether the requested package has been found
    package_found = False

    # Browse every package list available in the .PKGLIST directory
    try:
        for file in os.listdir(".PKGLIST"):
            # Only process JSON package list files
            if file.endswith(".json"):
                # Open and load the current package list
                with open(f".PKGLIST/{file}", "r") as f:
                    data = json.load(f)

                    # Search for the requested package
                    for package in data:
                        if package_name.lower() == package["name"].lower():
                            # Mark the package as found
                            package_found = True
                            # Create a Package object using the package metadata
                            package_var = classes.paquets.Package(
                                name=package["name"],
                                version=package["version"],
                                description=package["description"],
                                operating_system=package["operating_system"],
                                url=package["url"],
                                dependency=package["dependency"]
                            )

                            # Check whether the package supports the current operating system
                            if package_var.is_os_compatible():
                                # Display package information before installation
                                if not noshow:
                                    package_var.display_package_info()

                                # Ask the user for confirmation before downloading the package
                                if noconfirm:
                                    print()
                                    # Download and install the selected package
                                    if package["dependency"] == "":
                                        print("No dependencies found")
                                    else:
                                        for package_dependency in package["dependency"]:
                                            if package_dependency == package_name:
                                                print(f"Dependency {package_dependency} is the same as the package being installed. Skipping installation of this dependency.")
                                            if package_dependency == "":
                                                print("No more dependencies found")
                                            install_package(package_dependency, noconfirm=True)
                                    package_var.install_package()
                                    return
                                
                                elif defs.user_confirmations.userconfirmation(message=f"Are you sure you want install {package_name}"):
                                    print("Installing dependencies")
                                    if package["dependency"] == "":
                                        print("No dependencies found")
                                    else:
                                        for package_dependency in package["dependency"]:
                                            if package_dependency == package_name:
                                                print(f"Dependency {package_dependency} is the same as the package being installed. Skipping installation of this dependency.")
                                            if package_dependency == "":
                                                print("No more dependencies found")
                                            install_package(package_dependency, noconfirm=True, noshow=True)

                                    print()                
                                    if package_var.install_package():
                                        print("\nThe installation was successful.")
                                    else:
                                        print("\nThe application download URL cannot be found.")
                                    return

                                else:
                                    print("Cancelled installations")

    except KeyboardInterrupt: return
    except Exception as error: print(f"An error occured {error}"); return


    # Display an error message if the package could not be found
    if not package_found:
        print("Package Not Found")