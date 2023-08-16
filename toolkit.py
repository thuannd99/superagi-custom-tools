from superagi.tools.base_tool import BaseToolkit, BaseTool
from typing import List

from bank_client import BankClient
from user_info import UserInfo

class MyToolkit(BaseToolkit):
    name: str = "Banking Assistant Toolkit"
    description: str = "Banking Assistant Toolkit contains all tools to support banking assistant."

    def get_tools(self) -> List[BaseTool]:
        return [BankClient(), UserInfo()]

    def get_env_keys(self) -> List[str]:
        return ["USER_ID"]
