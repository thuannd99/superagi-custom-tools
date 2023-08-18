from superagi.tools.base_tool import BaseTool
from pydantic import BaseModel, Field
from typing import Type

from helpers.remigpt_api import RemigptAPI

class InstructionDocumentInput(BaseModel):
    question: str = Field(..., description="Human question")

class InstructionDocument(BaseTool):
    name: str = "Instruction Document Tool"
    args_schema: Type[BaseModel] = InstructionDocumentInput
    description: str = "Tool you should go first to get instruction about a deposit"

    def _execute(self, question: str = None):
        base_url = self.get_tool_config("REMIGPT_URL")
        api = RemigptAPI(base_url)
        return api.get_banking_instruction(question)
