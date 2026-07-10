try:
    from config_variable import *
    import shutil
    import os
except: print("Error: The required modules are not installed or not found."); exit()

def uninstall_pkg(pkg_name, noconfirm=False):
    try:
        if os.path.exists(f"{default_save_pkg_dir}/{pkg_name}"):
            if noconfirm or input(f"Are you sure you want to uninstall {pkg_name}? (y/n): ").strip().lower() == 'y':
                shutil.rmtree(f"{default_save_pkg_dir}/{pkg_name}") # remove the folder
                print(f"""{pkg_name} has been successfully uninstalled.""")
                return
            else: return
        else: print(f"{pkg_name} is not installed."); return
    except Exception as e: print(f"Error: An error occurred while uninstalling {pkg_name}. Error: {e}")