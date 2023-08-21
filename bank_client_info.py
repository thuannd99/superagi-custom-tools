from superagi.tools.base_tool import BaseTool
from pydantic import BaseModel, Field
from typing import Type

from helpers.remop_api import RemopAPI

class BankClientInfoInput(BaseModel):
    id: str = Field(..., description="ID or ref of a bank client")

class BankClientInfo(BaseTool):
    name: str = "Bank Client Info Tool"
    args_schema: Type[BaseModel] = BankClientInfoInput
    description: str = "Return information about a bank client"

    def _execute(self, id: str = None):
        base_url = self.get_tool_config("MESH_URL")
        appname = self.get_tool_config("APP_NAME")
        authorization = self.get_tool_config("AUTHORIZATION")
        api = RemopAPI(base_url, appname, authorization)
        return api.get_bank_client(id)
