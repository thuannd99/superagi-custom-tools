from superagi.tools.base_tool import BaseTool
from pydantic import BaseModel, Field
from typing import Type

from helpers.bank_utils import BankUtils

class BankHelperInput(BaseModel):
    type: str = Field(..., description="type of helper")
    data: str = Field(..., description="data of helper")
    amount: str = Field(..., description="amount of helper")

class BankHelper(BaseTool):
    name: str = "Bank Helper Tool"
    args_schema: Type[BaseModel] = BankHelperInput
    description: str = "Return calculated data"

    def _execute(self, type: str = None, data = None, amount = None):
        helper = BankUtils(type)
        return helper.calculate(data, amount)
