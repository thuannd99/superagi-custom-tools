import requests

from helpers.config_loader import ConfigLoader


class RemigptAPI:
    config = ConfigLoader()

    def __init__(self, base_url):
        self.base_url = base_url

    def get_banking_instruction(self, question):
        url = f"{self.base_url}/instruction"
        response = requests.get(url, params={"question": question, "collection": "banking_instruction"})

        if response.status_code == 200:
            return response.json()
        else:
            response.raise_for_status()
