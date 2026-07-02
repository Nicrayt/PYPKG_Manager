default_link_list = "https://pypkg-manager.vercel.app/base.json"
base_pkg_filename = "base.json"
base_upgrade_link = "https://pypkg-manager.vercel.app/up.json"
save_pkg_dir = "pkg/"
name_of_package_manager = " Onyx - PyPKG Manager "
ver = "0.3.3"

change_log = f"""The current version is v{ver} and the name of this version is{name_of_package_manager}
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
