try:
    from config_variable import *
    import zipfile
    import os
    import time
except (ImportError, ModuleNotFoundError):  print("Error: The required modules are not installed or not found."); exit()
try:    import requests
except (ImportError, ModuleNotFoundError): print("Error: The 'requests' module is not installed. Please install it to run this script."); exit()

all_log_variable = ""
log_path = os.path.join(f"{time.time()}_download_log.txt")

def write_log_to_file():
    global all_log_variable
    try:
        with open(log_path, "w") as log_file:
            log_file.write(all_log_variable)
    except (PermissionError):
        print("The log file does not have permission to write.")
    except:
        print("Error with the log file")


 # Download All
def downloadpkg(url=default_link_list, name="Please_use_-n_the_next_time", view=True, path=save_pkg_dir, log=False):
    global all_log_variable
    try:
        if url == default_link_list or name == "up.json":
            all_log_variable += "\nThe User want to download the default package list...\n"
            req = requests.get(default_link_list)
            open("base.json", "wb").write(req.content)
            all_log_variable += "\nThe default package list has been downloaded successfully.\n"
            print("Default Pkg list downloaded!")

        else:
            all_log_variable += f"\nDownloading {name}...\n"
            download = path.strip() + "/" + name.strip() + "/" + name.strip()
            os.makedirs(path.strip() + "/" + name.strip(), exist_ok=True)
            all_log_variable += f"\nCreated directory for {name}.\n"
            req = requests.get(url)
            open(download, "wb").write(req.content)
            if view:
                print(req.text)

            elif ".zip" in name:
                with zipfile.ZipFile(download, 'r') as unzipper:
                    all_log_variable += f"\nSince the file is a zip... Unzipping {name}...\n"
                    unzipper.extractall(path.strip() + "/" + name.strip())
                    print("Unzip completed")
                    all_log_variable +=   f"\nUnzip completed for {name}\n"
                    print("Finished with Success!")
                    all_log_variable += f"\nDownloaded {name} successfully.\n"
            
            else:
                print("Finished with Success!")
                all_log_variable += f"\nDownloaded {name} successfully.\n"

        if log:
            write_log_to_file()

    except FileNotFoundError:
        print(f"Error: You didn't specify a name for your file. or you dind't specify the pkglist")
        all_log_variable += f"\nError: You didn't specify a name for your file. or you dind't specify the pkglist\n"
        write_log_to_file()

    except (requests.HTTPError, requests.ConnectionError, requests.ReadTimeout, requests.Timeout):
        print(f"Error: 404, the file you want to download is unreachable.")
        all_log_variable += f"\nError: 404, the file you want to download is unreachable.\n"
        write_log_to_file()

    except (requests.URLRequired, requests.exceptions.MissingSchema):
        print(f"Error: You did not specify a URL, or the one you specified is incorrect or misspelled.")
        all_log_variable += f"\nError: You did not specify a URL, or the one you specified is incorrect or misspelled.\n"
        write_log_to_file()

    except (PermissionError):
        print("The file does not have permission to write.")
        all_log_variable += f"\nError: The file you want to download not have the permission to write here"
        write_log_to_file()
        

    except KeyboardInterrupt:
        all_log_variable += f"\nDownload interrupted by user.\n"
        write_log_to_file()
        exit()