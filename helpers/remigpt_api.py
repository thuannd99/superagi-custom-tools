import requests

from helpers.config_loader import ConfigLoader


class RemigptAPI:
    config = ConfigLoader()

    def __init__(self, base_url):
        self.base_url = base_url

    def get_banking_instruction(self, question):
        url = f"{self.base_url}/superagi/instruction"
        params = {"question": question, "collection": "banking_instruction"}
        response = requests.get(url, params=params)

        if response.status_code == 200:
            return response.json().get("instruction")
        else:
            response.raise_for_status()

    def save_chat(self, message, type):
        url = f"{self.base_url}/superagi/save_chat"
        body = {"message": message, "type": type}
        response = requests.post(url, json=body)

        if response.status_code == 200:
            return response.json()
        else:
            response.raise_for_status()
