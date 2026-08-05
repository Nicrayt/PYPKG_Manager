# Credit      : Nicray-Teams / https://github.com/Nicrayt

# Description :
# This file defines the Packages class. It provides methods to
# display package information, verify operating system
# compatibility, and download packages from a remote URL.

# Python      : 3.11

import os

# Define the Package class used to represent downloadable packages.
import classes.download as download

class Package:
    """Represent a downloadable package."""

    # Initialize a package with all required metadata.
    def __init__(self, name: str, version: str, description: str, operating_system: str, url: str, dependency: list = None) -> None:
        """Initialize a package with its metadata."""
        # Store the package name.
        self.name = name
        # Store the package version.
        self.version = version
        # Store the package description.
        self.description = description
        # Store the supported operating system.
        self.operating_system = operating_system
        # Store the package download URL.
        self.url = url

        self.dependency = dependency

### Use OS to verify if the OS of the Package is compatible with the current OS of the Users ###
    # Check if the package is compatible with the user's current operating system.
    def is_os_compatible(self) -> bool:
        """Return True if the package is compatible with the current operating system."""
        try:
            # Compare the package operating system with the current system.
            if self.operating_system == os.name:
                return True
            else:
                return False

        except Exception as e:
            # Display an error if something unexpected happens.
            print(f"An error occurred while verifying your OS: {e}")
            return False



### Display All informations of Package ###
    # Display all available information about the package.
    def display_package_info(self) -> None:
        """Display package information."""
        print("-"*10 + " PyPKG Manager " + "-"*10)
        # Print the package name.
        print(f"Package Name        : {self.name}")
        # Print the package version.
        print(f"Package Version     : {self.version}\n")
        # Print the package description.
        print(f"Package Description : {self.description}")
        # Print the compatible operating system.
        print(f"Compatible Systeme  : {self.operating_system}")
        # Print the package download URL.
        print(f"Package URL         : {self.url}")
        # End the function.
        return


### Download and write package ###
    # Download the package from the remote URL and save it locally.
    def install_package(self) -> bool:
        """install the packages (return True If everything went well else, False)"""
        try:
            install = download.Download(url=self.url, name=self.name, path=".PKG")
            if install.download():
                return True
        except download.DownloadError:
            return False