default_link_list = "http://192.168.1.18:5500/base.json"
base_pkg_filename = "base.json"
base_upgrade_link = "http://192.168.1.18:5500/up.json"
save_pkg_dir = "pkg/" # Not now
name = " PasBeau - PKG Manager "
ver = "0.2.1"

change_log = r"""
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
