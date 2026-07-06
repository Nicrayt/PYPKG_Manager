default_link_list:str = "https://pypkg-manager.vercel.app/base.json"
base_pkg_filename:str = "base.json"
base_upgrade_link:str = "https://pypkg-manager.vercel.app/up.json"
default_save_pkg_dir:str = "pkg"
default_save_pkg_list_dir:str = "pkglist"
name_of_package_manager:str = " Polie - PyPKG Manager "
version_of_pkg_manager:str = "0.4.001"

change_log:str = f"""The current version is v{version_of_pkg_manager} and the name of this version is{name_of_package_manager}
Ver 0.4.0 - Polie
- Modular Architecture (Complete Refactoring): "Spaghetti code" has been fully cleaned up. The project is now professionally structured into independent, specialized modules (`download_pkg.py`, `install_pkg.py`, `search_pkg.py`, `upgrade.py`, `config_variable.py`).
- Multi-repository Support: The manager no longer relies on a single, static list. It downloads the base data and then dynamically scans the entire `pkglist` folder; any `.json` file placed in this directory is now automatically read.
- Strict Cross-Platform Support (OS Checking): Native system check integration via `os.name`. The manager blocks installation and warns the user if the requested package is not designed for or compatible with their operating system (Windows NT vs. Linux POSIX).
- Static Typing (Type Hinting): Added data type declarations (e.g., `:str = None`) for global variables and function arguments. This ensures modern, more readable code and minimizes development bugs.
- Clean System Folder Management: Upon execution, `main.py` now automatically creates a proper directory structure, isolating package indexes in `./pkglist/` and downloaded programs in `./pkg/`.
- Expanded Archive Decompression Support: Decompression logic in `download_pkg.py` has been prepared to extend compatibility beyond `.zip` files to include `.tar` and `.7z` archive formats.
- System Permission Handling: Added handling for `PermissionError` during write operations. If the manager is launched in a protected folder without administrator privileges (sudo), it gracefully catches the crash and explains the issue to the user.

Ver 0.3.5
- Enhanced security
- Fewer bugs
- Reinstall the program if it is broken using `upgrade.py -f "URL"`
- Logging system for downloads

Ver 0.3.45
- If a package is not for your OS, it will let you know.
- Bugs have been fixed.

Ver 0.3.4
- Lots of bug fixes.
- Slightly optimized performance.
- Added cross-platform support (Linux, Windows).
- Tweaked the interface for a better look.
- Made library imports much more stable to prevent crashes.
- Cleaned up the code by removing a few unnecessary features.
- Added more details for package lists (OS, Bits, etc.).

Ver 0.3.3
- Numerous optimizations have been made.
- Some bugs have been fixed.
- The code is ten times more readable because I used proper variable names instead of names pulled out of thin air.
- The code is becoming slightly more robust.
- The code is much less resource-intensive for very low-end machines.

Ver 0.3.2
- Many bugs fixed: updates now work via their own download system, and ZIP files are extracted into their own dedicated folder.
- Added basic security measures: `try-except` blocks and a confirmation prompt to verify if you actually want to perform an update.
- Issues with this update: Minimal optimization (the code is becoming "spaghetti code"), and the same file is downloaded twice during the update process...

Ver 0.3.1
- Numerous bug fixes...
- The downloaded files are in a specific folder named after it.
-Nothing else...

Ver 0.3.0
- Numerous bug fixes; package searching is now 100% complete.
- Added support for extracting zip formats.
- Improved update management; 70% complete, with user interface enhancements (so you can see what is being downloaded...).
Nothing else...

Ver 0.2.1
- Significant robustness improvements to prevent Python crashes and properly handle errors using try/except blocks.
- Numerous bug fixes, including a fix for the issue in version 0.2.0 that completely prevented PKG downloads.
- The program is now much more user-friendly thanks to the addition of helpful tips.
- I’ve also added a new section—unfinished but 90% functional—for searching for a PKG within a PKG list.
- I’ve also added an update system, but it’s not quite polished yet, so I wouldn't recommend using it.
- Coming in version 0.3.0: planned support for file decompression, further optimizations, and reading multiple PKG lists.
Nothing else...

Ver 0.2.0
- Added Try/Except blocks to handle common errors, making it easier for the user to understand what went wrong.
- Added a basic interactive mode for PKG lists, allowing users to choose which application to download (incomplete).
- Fixed a few bugs regarding PKG lists.
Nothing else...

Ver 0.1.1
- Fixed a few bugs.
Nothing else...


Ver 0.1.0
- A "working" PKG manager.
Nothing else...
"""
