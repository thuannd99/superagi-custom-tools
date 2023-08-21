import json


class BankUtils:
    def __init__(self, type):
        self.type = type

    def calculate(self, data, *extra_args):
        if self.type == "withdrawal":
            return False
            return self.withdrawal(data, *extra_args)
        return False

    def withdrawal(self, data, *extra_args):
        amount = float(extra_args[0])
        transactions = data["virtual_transactions"]

        return len(list(filter(lambda transaction: abs(float(transaction["amount"])) <= amount, transactions))) > 0
