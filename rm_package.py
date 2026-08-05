import shutil
import defs.user_confirmations
import defs.list
import os

def remove_package(package_name=None) -> None:
    # Track whether the requested package has been found
    found = False
    # Browse every package installed in the package directory
    
    if package_name == "all":
        print("Hum ok ???")
        if defs.user_confirmations.userconfirmation(message=f"Are you sure you want to delete {package_name}?"):
            try:
                for folder in os.listdir(".PKG"):
                    shutil.rmtree(f".PKG/{folder}")
            except (FileNotFoundError, shutil.Error) as error: print(f"An error occured: {error}"); return
            except KeyboardInterrupt: print("Interupted by users"); return
        return


    try:
        for folder in os.listdir(".PKG"):
            # Check if the current folder matches the requested package name
            if folder == package_name:
                # Mark the package as found
                found = True

                # Ask the user for confirmation before deleting the package
                if defs.user_confirmations.userconfirmation(message=f"Are you sure you want to delete {package_name}?"):
                    # Remove the package directory and all of its contents
                    shutil.rmtree(f".PKG/{package_name}")
                    print("The package has been successfully deleted.")
    except (FileNotFoundError, shutil.Error) as error: print(f"An error occured: {error}")
    except KeyboardInterrupt: print("Interupted by users"); return

    # Display an error message if the package was not found
    if not found:
        print("Package not found")
        return