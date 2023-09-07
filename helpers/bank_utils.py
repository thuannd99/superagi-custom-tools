import datetime
from helpers.time import convert_to_timestamp

class BankUtils:
    def __init__(self, type):
        self.type = type


    def calculate(self, data, **kwargs):
        if self.type == "withdrawal":
            api = kwargs["api"]
            return self.withdrawal(data, api)
        if self.type == "deposit":
            amount = float(kwargs["amount"])
            return self.deposit(data, amount)
        if self.type == "revert":
            api = kwargs["api"]
            return self.revert(data, api)
        if self.type == "propose":
            api = kwargs["api"]
            return self.revert(data, api)
        return f"Error. Does not support this type: {self.type}"


    def withdrawal(self, data, api):
        sub_payments = data["sub_payments"]
        vtx_list = []
        for sub_payment in sub_payments:
            vtx_list += self.proper_vtx_for_withdrawal(sub_payment, api)

        return vtx_list


    def revert(self, data, api):
        sub_payments = data["sub_payments"]
        vtx_list = []
        for sub_payment in sub_payments:
            vtx_list += self.proper_vtx_for_revert(sub_payment, api)

        return vtx_list


    def propose(self, data, api):
        sub_payments = data["sub_payments"]
        vtx_list = []
        for sub_payment in sub_payments:
            vtx_list += self.proper_vtx_for_propose(sub_payment, api)

        return vtx_list


    def deposit(self, data, amount):
        transactions = data["virtual_transactions"]
        proper_transactions = list(filter(
        lambda transaction:
            transaction["status"] != "expired" and
            transaction["finalized"] == False and
            amount - 100 <= float(transaction["amount"]) <= amount,
            transactions
        ))

        return list(map(lambda transaction: transaction["id"], proper_transactions))


    def proper_vtx_for_withdrawal(self, sub_payment, api):
        amount = float(sub_payment["amount"])
        bank_client_id = sub_payment["bank_client_id"]
        from_time = convert_to_timestamp(sub_payment["start_paying_at"])
        to_time = (datetime.datetime.fromtimestamp(from_time) + datetime.timedelta(hours=24)).timestamp()

        proper_transactions = []
        next_page = 1
        while next_page is not None:
            vtx_list = api.get_vtx_list(bank_client_id, from_time, to_time, page=next_page)
            transactions = vtx_list["virtual_transactions"]
            next_page = vtx_list["meta"]["next_page"]

            proper_transactions += list(filter(
            lambda transaction:
                amount - 100 <= abs(float(transaction["amount"])) <= amount,
                transactions
            ))

        return list(map(lambda transaction: transaction["id"], proper_transactions))


    def proper_vtx_for_revert(self, sub_payment, api):
        amount = float(sub_payment["amount"])
        bank_client_id = sub_payment["bank_client_id"]
        from_time = convert_to_timestamp(sub_payment["start_paying_at"])
        to_time = (datetime.datetime.fromtimestamp(from_time) + datetime.timedelta(hours=48)).timestamp()

        proper_transactions = []
        next_page = 1
        while next_page is not None:
            vtx_list = api.get_vtx_list(bank_client_id, from_time, to_time, page=next_page)
            transactions = vtx_list["virtual_transactions"]
            next_page = vtx_list["meta"]["next_page"]

            proper_transactions += list(filter(
            lambda transaction:
                transaction["status"] != "expired" and
                transaction["finalized"] == False and
                amount - 100 <= float(transaction["amount"]) <= amount,
                transactions
            ))

        return list(map(lambda transaction: transaction["id"], proper_transactions))


    def proper_vtx_for_propose(self, sub_payment, api):
        amount = float(sub_payment["amount"])
        bank_client_id = sub_payment["bank_client_id"]
        from_time = convert_to_timestamp(sub_payment["start_paying_at"])
        to_time = (datetime.datetime.fromtimestamp(from_time) + datetime.timedelta(hours=24)).timestamp()

        proper_transactions = []
        next_page = 1
        while next_page is not None:
            vtx_list = api.get_vtx_list(bank_client_id, from_time, to_time, page=next_page)
            transactions = vtx_list["virtual_transactions"]
            next_page = vtx_list["meta"]["next_page"]

            proper_transactions += list(filter(
            lambda transaction:
                transaction["status"] != "expired" and
                transaction["finalized"] == False and
                amount - 100 <= float(transaction["amount"]) <= amount,
                transactions
            ))

        return list(map(lambda transaction: transaction["id"], proper_transactions))
