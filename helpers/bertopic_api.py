import requests

from helpers.config_loader import ConfigLoader


class BertopicAPI:
    config = ConfigLoader()

    def __init__(self, base_url, api_key):
        self.base_url = base_url
        self.headers = {
            "API-Key": api_key,
        }

    def request_export_intercom_chat(self, app, name, query, creator_email):
        url = f"{self.base_url}/api/v1/intercom_chat_export_requests"
        body = {"app": app, "name": name, "query": query, "creator_email": creator_email}
        response = requests.post(url, json=body, headers=self.headers)

        if response.status_code == 200:
            return response.json()
        else:
            response.raise_for_status()

    def get_intercom_chat_info(self, uuid):
        url = f"{self.base_url}/api/v1/intercom_chat_export_requests/{uuid}"
        response = requests.get(url, headers=self.headers)

        if response.status_code == 200:
            return response.json()
        else:
            response.raise_for_status()
