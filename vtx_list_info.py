from superagi.tools.base_tool import BaseTool
from pydantic import BaseModel, Field
from typing import Type
from helpers.time import convert_to_timestamp

from helpers.remop_api import RemopAPI
from helpers.bank_utils import BankUtils

class VtxListInfoInput(BaseModel):
    bank_client_id: str = Field(..., description="bank_client_id of a vtx list")
    from_time_timestamp: str = Field(..., description="from_time_timestamp of a vtx list")
    to_time_timestamp: str = Field(..., description="to_time_timestamp of a vtx list")
    amount: str = Field(..., description="amount of a payment")
    payable_id: str = Field(..., description="payable_id of a payment")
    type: str = Field(..., description="type of a request")

class VtxListInfo(BaseTool):
    name: str = "Vtx List Info Tool"
    args_schema: Type[BaseModel] = VtxListInfoInput
    description: str = "Return list of proper vtx ids"

    def _execute(self, bank_client_id: str = None, from_time_timestamp: str = None, to_time_timestamp: str = None, amount: str = None, payable_id: str = None, type: str = None):
        base_url = self.get_tool_config("MESH_URL")
        appname = self.get_tool_config("APP_NAME")
        authorization = self.get_tool_config("AUTHORIZATION")
        api = RemopAPI(base_url, appname, authorization)

        if type == "deposit":
            from_time = convert_to_timestamp(from_time_timestamp)
            to_time = convert_to_timestamp(to_time_timestamp)
            
            transactions = []
            next_page = 1
            while next_page is not None:
                vtx_list = api.get_vtx_list(bank_client_id, from_time, to_time, page=next_page)
                transactions += vtx_list["virtual_transactions"]
                next_page = vtx_list["meta"]["next_page"]
            data = {"virtual_transactions": transactions}
        else:
            api = RemopAPI(base_url, appname, authorization)
            data = api.get_payment(payable_id)

        return BankUtils(type).calculate(data, amount=amount, api=api)
