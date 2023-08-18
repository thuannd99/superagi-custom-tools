from superagi.tools.base_tool import BaseTool
from pydantic import BaseModel, Field
from typing import Type
from helpers.time import convert_to_timestamp

from helpers.remop_api import RemopAPI

class VtxListInfoInput(BaseModel):
    bank_client_id: str = Field(..., description="bank_client_id of a vtx list")
    from_time_timestamp: str = Field(..., description="from_time_timestamp of a vtx list")
    to_time_timestamp: str = Field(..., description="to_time_timestamp of a vtx list")

class VtxListInfo(BaseTool):
    name: str = "Vtx List Info Tool"
    args_schema: Type[BaseModel] = VtxListInfoInput
    description: str = "Return information about a vtx list"

    def _execute(self, bank_client_id: str = None, from_time_timestamp: str = None, to_time_timestamp: str = None):
        base_url = self.get_tool_config("MESH_URL")
        appname = self.get_tool_config("APP_NAME")
        authorization = self.get_tool_config("AUTHORIZATION")
        api = RemopAPI(base_url, appname, authorization)
        from_time = convert_to_timestamp(from_time_timestamp)
        to_time = convert_to_timestamp(to_time_timestamp)
        return api.get_vtx_list(bank_client_id, from_time, to_time)
