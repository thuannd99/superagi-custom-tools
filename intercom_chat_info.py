from superagi.tools.base_tool import BaseTool
from pydantic import BaseModel, Field
from typing import Type

from helpers.bertopic_api import BertopicAPI

class IntercomChatInfoInput(BaseModel):
    uuid: str = Field(..., description="uuid of an intercom chat")

class IntercomChatInfo(BaseTool):
    name: str = "Intercom Chat Info Tool"
    args_schema: Type[BaseModel] = IntercomChatInfoInput
    description: str = "Return information about an intercom chat"

    def _execute(self, uuid: str = None):
        base_url = self.get_tool_config("BERTOPIC_URL")
        api_key = self.get_tool_config("BERTOPIC_API_KEY")
        api = BertopicAPI(base_url, api_key)
        return api.get_intercom_chat_info(uuid)
