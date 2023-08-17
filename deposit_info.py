from superagi.tools.base_tool import BaseTool
from pydantic import BaseModel, Field
from typing import Type

from helpers.remop_api import RemopAPI

class DepositInfoInput(BaseModel):
    id: str = Field(..., description="ID of a deposit")

class DepositInfo(BaseTool):
    name: str = "Deposit Info Tool"
    args_schema: Type[BaseModel] = DepositInfoInput
    description: str = "Return information about a deposit (ref, status, bank client id,...)"

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        appname = self.get_tool_config("APP_NAME")
        authorization = self.get_tool_config("AUTHORIZATION")
        self.api = RemopAPI(appname, authorization)

    def _execute(self, id: str = None):
        return self.api.get_deposit(id)
