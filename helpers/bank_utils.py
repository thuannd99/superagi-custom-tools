import json


class BankUtils:
    def __init__(self, type):
        self.type = type

    def calculate(self, data, *extra_args):
        if self.type == "withdrawal":
            return self.withdrawal(data, *extra_args)
        if self.type == "deposit":
            return self.deposit(data, *extra_args)
        return f"Error. Does not support this type: {self.type}"

    def withdrawal(self, data, *extra_args):
        amount = float(extra_args[0])
        transactions = data["virtual_transactions"]

        return len(list(filter(lambda transaction: abs(float(transaction["amount"])) <= amount, transactions))) > 0

    def deposit(self, data, *extra_args):
        amount = float(extra_args[0])
        transactions = data["virtual_transactions"]
        proper_transactions = list(filter(
        lambda transaction:
            transaction["status"] != "expired" and
            transaction["finalized"] == False and
            amount - 100 <= float(transaction["amount"]) <= amount,
            transactions
        ))

        return list(map(lambda transaction: transaction["id"], proper_transactions))
