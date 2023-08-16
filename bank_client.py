from superagi.tools.base_tool import BaseTool
from pydantic import BaseModel, Field
from typing import Type


class BankClientInput(BaseModel):
    id: str = Field(..., description="ID of the a bank client")

class BankClient(BaseTool):
    name: str = "Bank Client Tool"
    args_schema: Type[BaseModel] = BankClientInput
    description: str = "Return a status of a bank client"

    def _execute(self, id: str = None):
        id = int(id)
        return 10 if (id % 2) == 0 else 20
