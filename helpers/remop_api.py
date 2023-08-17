import requests

from helpers.config_loader import ConfigLoader


class RemopAPI:
    config = ConfigLoader()

    def __init__(self, appname, authorization):
        self.headers = {
            "Appname": appname,
            "Authorization": authorization,
        }

    def get_deposit(self, deposit_id):
        mesh_url = self.config.get("MESH_URL")
        url = f"{mesh_url}/api/ml/deposits/{deposit_id}"
        response = requests.get(url, headers=self.headers)

        if response.status_code == 200:
            return response.json()  # Return the JSON data
        else:
            response.raise_for_status()  # Raises an HTTPError if the HTTP request returned an unsuccessful status code
