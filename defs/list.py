import os

# I know that better with Enum but yeah (Full Fleme)


def list(list) -> None:
    if list == "package" or list == "pkg":
        list_package()
        return

def list_package() -> None:
    """return nothing just diplay a dir"""
    print("== Installed packages ==")
    for folder in os.listdir(".PKG/"):
        stockage = 0
        for file in os.listdir(f".PKG/{folder}"):            
            info = os.stat(f".PKG/{folder}/{file}")
            stockage += info.st_size
            stockage /= 1048576

        print(f"name: {folder} | size: {stockage:.2f}Mb")