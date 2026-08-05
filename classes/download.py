import os
import library.requests as requests

class Download:
    def __init__(self, url, name, path=".PKG", nofolder=False) -> None:
        self.url = url
        self.name = name
        self.path = path
        self.folder = nofolder


    def download(self) -> bool:
        """Download the package and save it to disk."""
        try:
            # Get the package filename from the download URL.
            package_file_name = self.url.split("/")[-1]
            if not self.folder:
                # Define the local path where the package will be stored.
                package_path = f"{self.path}/{self.name}/{package_file_name}"
                # Create the package directory if it does not exist.
                os.makedirs(f"{self.path}/{self.name}/", exist_ok=True)
            else:
                # Define the local path where the package will be stored.
                package_path = f"{self.path}/{package_file_name}"
                # Create the package directory if it does not exist.
                os.makedirs(f"{self.path}/", exist_ok=True)

            # Start the package download using streaming mode.
            try:
                download_package_get = requests.get(self.url, stream=True)
            except (requests.HTTPError, requests.ConnectionError, requests.ConnectTimeout): raise DownloadError()

            # Get the total package size from the server headers.
            total_size = int(download_package_get.headers.get("content-length", 0))
            if total_size == 0:
                print(f"\nWarning: The server did not provide the total size for '{self.name}'. Progress will not be displayed.")
                total_size = -10  # Set to -10 to avoid division by zero in progress calculation

            # Initialize the downloaded size counter.
            downloaded = 0

            # Open the destination file in binary write mode.
            with open(package_path, 'wb') as downloaded_file:

                # Download the package chunk by chunk.
                for chunk in download_package_get.iter_content(chunk_size=1024 * 1024):
                    # Ignore empty chunks.
                    if chunk:
                        # Write the current chunk into the file.
                        downloaded_file.write(chunk)
                        # Update the downloaded byte counter.
                        downloaded += len(chunk)
                        # Calculate the current download percentage.
                        percent = downloaded * 100 / total_size
                        # Convert the percentage into progress bar units.
                        unit = int(percent/2)
                        # Display the download progress bar.
                        print(f"\r{self.name:<10} [{('#' * unit).ljust(50, '-')}]    {percent:6.2f}%", end="")
                # True is download as finished with successe
                return True
        except (requests.ConnectionError, requests.ConnectTimeout, requests.HTTPError): raise DownloadError()
        except (KeyboardInterrupt): return False

class DownloadError(Exception):
    """When there is an error somewhere with requests"""
    pass