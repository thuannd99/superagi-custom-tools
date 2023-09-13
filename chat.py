from superagi.tools.base_tool import BaseTool
from pydantic import BaseModel, Field
from typing import Type

from helpers.remigpt_api import RemigptAPI

class ChatInput(BaseModel):
    message: str = Field(..., description="message of a chat")
    requester_id: str = Field(..., description="requester id")
    channel_name: str = Field(..., description="channel name")

class Chat(BaseTool):
    name: str = "Chat Tool"
    args_schema: Type[BaseModel] = ChatInput
    description: str = "Return status chat and confirm chat"

    def _execute(self, message: str = None, requester_id: str = None, channel_name: str = None):
        base_url = self.get_tool_config("REMIGPT_URL")
        api = RemigptAPI(base_url)
        response = api.save_chat(message, requester_id, channel_name)
        return response
