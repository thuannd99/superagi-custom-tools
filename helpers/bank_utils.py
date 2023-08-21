import json


class BankUtils:
    def __init__(self, type):
        self.type = type

    def calculate(self, data, *extra_args):
        if self.type == "withdrawal":
            return self.withdrawal(data, *extra_args)

    def withdrawal(self, data, *extra_args):
        amount = float(extra_args[0])
        jsonified_data = json.loads(data) 
        transactions = jsonified_data["virtual_transactions"]

        return len(list(filter(lambda transaction: abs(float(transaction["amount"])) <= amount, transactions))) > 0
