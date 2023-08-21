from superagi.tools.base_tool import BaseTool
from pydantic import BaseModel, Field
from typing import Type

from helpers.remop_api import RemopAPI

class TradeInfoInput(BaseModel):
    id: str = Field(..., description="ID or ref of a trade")

class TradeInfo(BaseTool):
    name: str = "Trade Info Tool"
    args_schema: Type[BaseModel] = TradeInfoInput
    description: str = "Return information about a trade"

    def _execute(self, id: str = None):
        base_url = self.get_tool_config("BACKEND_URL")
        appname = self.get_tool_config("APP_NAME")
        authorization = self.get_tool_config("AUTHORIZATION")
        api = RemopAPI(base_url, appname, authorization)
        return api.get_trade(id)
