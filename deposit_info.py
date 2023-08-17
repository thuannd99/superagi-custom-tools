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

    def _execute(self, id: str = None):
        base_url = self.get_tool_config("MESH_URL")
        appname = self.get_tool_config("APP_NAME")
        authorization = self.get_tool_config("AUTHORIZATION")
        api = RemopAPI(appname, authorization, base_url)
        return api.get_deposit(id)
