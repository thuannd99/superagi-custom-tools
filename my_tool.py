from superagi.tools.base_tool import BaseTool
from pydantic import BaseModel, Field
from typing import Type

class MyToolInput(BaseModel):
    message: str = Field(..., description="Greeting message to be sent")

class MyTool(BaseTool):
    name: str = "My Tool"
    args_schema: Type[BaseModel] = MyToolInput
    description: str = "Sends a Greeting Message"

    def _execute(self, message: str = None):
        from_name = self.get_tool_config('FROM')
        greetings_str = message + "\n" + from_name
        return greetings_str