from superagi.tools.base_tool import BaseToolkit, BaseTool
from typing import List

from chat import Chat
from instruction_document import InstructionDocument
from deposit_info import DepositInfo
from sub_payment_info import SubPaymentInfo
from vtx_list_info import VtxListInfo
from user_info import UserInfo
from fiat_deposit_info import FiatDepositInfo
from fiat_withdrawal_info import FiatWithdrawalInfo
from trade_info import TradeInfo
from bank_client_info import BankClientInfo
from payment_info import PaymentInfo

from intercom_chat_export_request import IntercomChatExportRequest
from intercom_chat_info import IntercomChatInfo

class BankingAssistantToolkit(BaseToolkit):
    name: str = "Banking Assistant Toolkit"
    description: str = "Banking Assistant Toolkit contains all tools to support banking assistant."

    def get_tools(self) -> List[BaseTool]:
        return [InstructionDocument(),
                DepositInfo(), SubPaymentInfo(), VtxListInfo(),
                UserInfo(), TradeInfo(), BankClientInfo(), PaymentInfo(),
                # FiatDepositInfo(), FiatWithdrawalInfo(), # These tools has not used yet
        ]

    def get_env_keys(self) -> List[str]:
        return ["BACKEND_URL", "MESH_URL", "APP_NAME", "AUTHORIZATION", "REMIGPT_URL"]

class BertopicToolkit(BaseToolkit):
    name: str = "Bertopic Toolkit"
    description: str = "Bertopic Toolkit contains all tools to support running daily Bertopic."

    def get_tools(self) -> List[BaseTool]:
        return [
            IntercomChatExportRequest(), IntercomChatInfo()
        ]

    def get_env_keys(self) -> List[str]:
        return ["BERTOPIC_URL", "API_KEY"]

class BaseToolkit(BaseToolkit):
    name: str = "Base Toolkit"
    description: str = "Utility tools for Superagi."

    def get_tools(self) -> List[BaseTool]:
        return [
            Chat(),
        ]

    def get_env_keys(self) -> List[str]:
        return ["REMIGPT_URL"]
