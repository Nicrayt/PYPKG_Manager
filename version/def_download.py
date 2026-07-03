try:
    from config_variable import *
    import zipfile
    import os
except (ImportError, ModuleNotFoundError):  print("Error: The required modules are not installed or not found."); exit()
try:    import requests
except (ImportError, ModuleNotFoundError): print("Error: The 'requests' module is not installed. Please install it to run this script."); exit()


 # Download All
def downloadpkg(url=default_link_list, name="Please_use_-n_the_next_time", view=True, path=save_pkg_dir):
    try:
        if url == default_link_list or name == "up.json":
            req = requests.get(default_link_list)

            open("base.json", "wb").write(req.content)
            print("Default Pkg list downloaded!")
        else:
            download = path.strip() + "/" + name.strip() + "/" + name.strip()
            os.makedirs(path.strip() + "/" + name.strip(), exist_ok=True)
            req = requests.get(url)
            open(download, "wb").write(req.content)
            if view:
                print(req.text)
            elif ".zip" in name:
                with zipfile.ZipFile(download, 'r') as unzipper:
                    unzipper.extractall(path.strip() + "/" + name.strip())
                    print("Unzip completed")
                    print("Finished with Success!")
            else:
                print("Finished with Success!")
                exit()

    except FileNotFoundError:
        print(f"Error: You didn't specify a name for your file. or you dind't specify the pkglist")
    except (requests.HTTPError, requests.ConnectionError, requests.ReadTimeout, requests.Timeout):
        print(f"Error: 404, the file you want to download is unreachable.")
    except (requests.URLRequired, requests.exceptions.MissingSchema):
        print(f"Error: You did not specify a URL, or the one you specified is incorrect or misspelled.")
    except KeyboardInterrupt:
        exit()
