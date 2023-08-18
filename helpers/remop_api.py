import requests


class RemopAPI:
    def __init__(self, base_url, appname, authorization):
        self.base_url = base_url
        self.headers = {
            "Appname": appname,
            "Authorization": authorization,
        }
    
    def jsonify(self, response):
        if response.status_code == 200:
            return response.json()
        else:
            response.raise_for_status()

    def get_deposit(self, deposit_id):
        url = f"{self.base_url}/api/ml/deposits/{deposit_id}"
        response = requests.get(url, headers=self.headers)
        return self.jsonify(response)

    def get_vtx_list(self, bank_client_id, from_time_timestamp, to_time_timestamp):
        url = f"{self.base_url}/api/ml/virtual_transactions"
        params = {
            "bank_client_id": bank_client_id,
            "from_time_timestamp": from_time_timestamp,
            "to_time_timestamp": to_time_timestamp,
        }
        response = requests.get(url, headers=self.headers, params=params)
        return self.jsonify(response)

    def get_sub_payment(self, id):
        url = f"{self.base_url}/api/ml/sub_payments/{id}"
        response = requests.get(url, headers=self.headers)
        return self.jsonify(response)

    def get_user(self, id):
        url = f"{self.base_url}/api/ml/users/{id}"
        response = requests.get(url, headers=self.headers)
        return self.jsonify(response)

    def get_fiat_deposit(self, id):
        url = f"{self.base_url}/api/ml/fiat_deposits/{id}"
        response = requests.get(url, headers=self.headers)
        return self.jsonify(response)