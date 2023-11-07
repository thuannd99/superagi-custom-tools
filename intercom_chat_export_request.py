from superagi.tools.base_tool import BaseTool
from pydantic import BaseModel, Field
from typing import Type

from helpers.bertopic_api import BertopicAPI

class IntercomChatExportRequestInput(BaseModel):
    app: str = Field(..., description="app name of intercom chat export request")
    name: str = Field(..., description="name of intercom chat export request")
    query: str = Field(..., description="query of intercom chat export request")
    creator_email: str = Field(..., description="email of creater of intercom chat export request")

class IntercomChatExportRequest(BaseTool):
    name: str = "Intercom Chat Export Request Tool"
    args_schema: Type[BaseModel] = IntercomChatExportRequestInput
    description: str = "Request to export intercom chat and return the intercom chat uuid"

    def _execute(self, app: str = None, name: str = None, query: str = None, creator_email: str = None):
        base_url = self.get_tool_config("BERTOPIC_URL")
        api_key = self.get_tool_config("BERTOPIC_API_KEY")
        api = BertopicAPI(base_url, api_key)
        return api.request_export_intercom_chat(app, name, query, creator_email)
