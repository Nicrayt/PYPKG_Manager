import json

def add_repository(repository_url):
    try:
        # Load the existing repositories from the JSON file
        with open("repositories.json", "r") as file:
            repositories = json.load(file)

        # Check if the repository already exists
        for repo in repositories.get("repositories", []):
            if repository_url == repo:
                print(f"The repository '{repository_url}' is already added.")
                return

        # Add the new repository to the list
        repositories["repositories"].append(repository_url)

        # Save the updated repositories back to the JSON file
        with open("repositories.json", "w") as file:
            json.dump(repositories, file, indent=4)

        print(f"Repository '{repository_url}' has been added successfully.")

    except FileNotFoundError:
        print("The 'repositories.json' file was not found. Please ensure it exists.")
    except json.JSONDecodeError:
        print("Error decoding JSON from 'repositories.json'. Please check the file format.")
    except Exception as e:
        print(f"An error occurred while adding the repository: {e}")


def remove_repository(repository_url):
    try:
        # Load the existing repositories from the JSON file
        with open("repositories.json", "r") as file:
            repositories = json.load(file)

        # Check if the repository exists
        if repository_url not in repositories.get("repositories", []):
            print(f"The repository '{repository_url}' does not exist.")
            return

        # Remove the repository from the list
        repositories["repositories"].remove(repository_url)

        # Save the updated repositories back to the JSON file
        with open("repositories.json", "w") as file:
            json.dump(repositories, file, indent=4)

        print(f"Repository '{repository_url}' has been removed successfully.")

    except FileNotFoundError:
        print("The 'repositories.json' file was not found. Please ensure it exists.")
    except json.JSONDecodeError:
        print("Error decoding JSON from 'repositories.json'. Please check the file format.")
    except Exception as e:
        print(f"An error occurred while removing the repository: {e}")