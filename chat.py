from superagi.tools.base_tool import BaseTool
from pydantic import BaseModel, Field
from typing import Type

from helpers.remigpt_api import RemigptAPI

class ChatInput(BaseModel):
    message: str = Field(..., description="message of a chat")
    type: str = Field(..., description="type of a chat, should by 'dm' or 'channel'")

class Chat(BaseTool):
    name: str = "Chat Tool"
    args_schema: Type[BaseModel] = ChatInput
    description: str = "Return status chat and confirm chat"

    def _execute(self, message: str = None, type: str = None):
        base_url = self.get_tool_config("REMIGPT_URL")
        api = RemigptAPI(base_url)
        response = api.save_chat(message, type)
        return response
