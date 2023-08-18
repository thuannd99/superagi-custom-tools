from superagi.tools.base_tool import BaseToolkit, BaseTool
from typing import List

from instruction_document import InstructionDocument
from deposit_info import DepositInfo

class MyToolkit(BaseToolkit):
    name: str = "Banking Assistant Toolkit"
    description: str = "Banking Assistant Toolkit contains all tools to support banking assistant."

    def get_tools(self) -> List[BaseTool]:
        return [InstructionDocument(), DepositInfo()]

    def get_env_keys(self) -> List[str]:
        return ["MESH_URL", "APP_NAME", "AUTHORIZATION", "REMIGPT_URL"]
