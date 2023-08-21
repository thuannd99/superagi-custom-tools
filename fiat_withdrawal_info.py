from superagi.tools.base_tool import BaseTool
from pydantic import BaseModel, Field
from typing import Type

from helpers.remop_api import RemopAPI

class FiatWithdrawalInfoInput(BaseModel):
    id: str = Field(..., description="ID or ref of a fiat withdrawal")

class FiatWithdrawalInfo(BaseTool):
    name: str = "Fiat Withdrawal Info Tool"
    args_schema: Type[BaseModel] = FiatWithdrawalInfoInput
    description: str = "Return information about a fiat withdrawal"

    def _execute(self, id: str = None):
        base_url = self.get_tool_config("BACKEND_URL")
        appname = self.get_tool_config("APP_NAME")
        authorization = self.get_tool_config("AUTHORIZATION")
        api = RemopAPI(base_url, appname, authorization)
        return api.get_fiat_withdrawal(id)
