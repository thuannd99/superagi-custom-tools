from superagi.tools.base_tool import BaseTool
from pydantic import BaseModel, Field
from typing import Type

from helpers.remop_api import RemopAPI

class PaymentInfoInput(BaseModel):
    id: str = Field(..., description="ID or ref of a payment")

class PaymentInfo(BaseTool):
    name: str = "Payment Info Tool"
    args_schema: Type[BaseModel] = PaymentInfoInput
    description: str = "Return information about a payment"

    def _execute(self, id: str = None):
        base_url = self.get_tool_config("MESH_URL")
        appname = self.get_tool_config("APP_NAME")
        authorization = self.get_tool_config("AUTHORIZATION")
        api = RemopAPI(base_url, appname, authorization)
        return api.get_payment(id)
