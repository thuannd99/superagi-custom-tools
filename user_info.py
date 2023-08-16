from superagi.tools.base_tool import BaseTool
from pydantic import BaseModel, Field
from typing import Type


class UserInfoInput(BaseModel):
    id: str = Field(..., description="ID of the user")

class UserInfo(BaseTool):
    name: str = "User Info Tool"
    args_schema: Type[BaseModel] = UserInfoInput
    description: str = "Return a status of a user"

    def _execute(self, id: str = None):
        id = int(self.get_tool_config("USER_ID"))
        return id
