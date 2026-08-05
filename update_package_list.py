try:
    import os
    import json
    import classes.download as download
    import defs.user_confirmations
except ImportError as error: print(f"You do not have the necessary libraries to run PyPKG : {error}")

def update_list(show=False, noconfirm=False):
    if noconfirm or defs.user_confirmations.userconfirmation("Are you sure you want to update all the package lists?"):
        with open("repositories.json", "r") as file:
            repositories = json.load(file)

        for repo in repositories["repositories"]:
            url = repo

            # Download the master package list
            try: req = download.Download(url=url, name="list", path=".TMP", nofolder=True); req.download()
            except download.DownloadError as error: print(f"An error occured: {error}")

            # Load the master package list into memory
            try:
                with open(".TMP/lists.json", "r") as f:
                    all_list = json.load(f)
            except (json.JSONDecodeError, FileNotFoundError) as error: print(f"An error occured: {error}"); return

            # Download every package list referenced in the master list
            for package_list in all_list:  
                package_file_name = package_list["url"].split("/")[-1]
                try: 
                    pkglist = download.Download(url=package_list["url"], name=package_file_name, path=".PKGLIST", nofolder=True)
                    if pkglist.download():
                        print("\nSuccessfully completed")
                    else:
                        print("\nAn unknown error occurred while the packages were being downloaded.")
                    
                except download.DownloadError as error: print(f"An error occured: {error}")