from superagi.tools.base_tool import BaseTool
from pydantic import BaseModel, Field
from typing import Type

from helpers.remop_api import RemopAPI

class UserInfoInput(BaseModel):
    id_or_username: str = Field(..., description="user id or username of a user")

class UserInfo(BaseTool):
    name: str = "User Info Tool"
    args_schema: Type[BaseModel] = UserInfoInput
    description: str = "Return information about a user"

    def _execute(self, id_or_username: str = None):
        base_url = self.get_tool_config("BACKEND_URL")
        appname = self.get_tool_config("APP_NAME")
        authorization = self.get_tool_config("AUTHORIZATION")
        api = RemopAPI(base_url, appname, authorization)
        return api.get_user(id_or_username)
