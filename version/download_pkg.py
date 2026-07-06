try:
    import zipfile
    import os
    import requests
    from config_variable import *
except (ImportError, ModuleNotFoundError):  print("Error: The required modules are not installed or not found."); exit()


def downloadpkg(url:str=None, pkg_name:str=None, path:str=default_save_pkg_dir, dont_show=False):
    # Variables
    zip_file:str = 0

    try:

        # Path
        download_path:str = (f"{path}/{pkg_name}/".strip()) # where is the pkg
        download_path_with_filename:str = (f"{download_path}{pkg_name}".strip()) # installed pkg is here

        # Download
        if ".json" in pkg_name: # check if it ends with json for pkg list
            download_pkg_get:str = requests.get(url) # save the content of the url on a variable
            with open(f"{default_save_pkg_list_dir}/{pkg_name}", 'wb') as downloaded_file:
                downloaded_file.write(download_pkg_get.content) # Install at /pkglist/namepkglist.json

        else: # Download
            os.makedirs(download_path, exist_ok=True)
            download_pkg_get:str = requests.get(url) # save the content of the url on a variable
            with open(download_path_with_filename, 'wb') as downloaded_file:
                    # Write content
                    downloaded_file.write(download_pkg_get.content) # write the content to the file


        # Unzip if it is a zip/tar/7z file
        if download_path_with_filename.endswith((".zip", ".tar", ".7z")): # check if it ends with zip or tar or 7z
            with zipfile.ZipFile(download_path_with_filename, 'r') as zip_ref: # use zipfile module to unzip the file
                zip_ref.extractall(path=download_path) # extract the file

        # End
        if not dont_show:
            if zip_file: print("Your download has completed successfully, and the file appears to have been extracted successfully.") # if it ends with zip, print this
            else: print("Your download has completed successfully.") # else print this



    except (requests.HTTPError, requests.ConnectionError, requests.ReadTimeout, requests.Timeout): print("Error: 404, the file you want to download is unreachable.")
    except (requests.URLRequired, requests.exceptions.MissingSchema): print("Error: You did not specify a URL, or the one you specified is incorrect or misspelled.")
    except PermissionError: print("Error: You do not have the right to write to the because you do not have the required permissions.")
    except Exception as e: print(f"An error occured: {e}")