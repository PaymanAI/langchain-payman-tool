# tests/integration_tests/test_payman_tools.py

from typing import Type

# Import the standard LangChain test harness for integration testing
from langchain_tests.integration_tests import ToolsIntegrationTests

# Import your Payman tool classes
from langchain_payman_tool.tools import (
    SendPaymentTool,
    SearchPayeesTool,
    AddPayeeTool,
    AskForMoneyTool,
    GetBalanceTool,
)


class TestSendPaymentToolIntegration(ToolsIntegrationTests):
    @property
    def tool_constructor(self) -> Type[SendPaymentTool]:
        return SendPaymentTool

    @property
    def tool_constructor_params(self) -> dict:
        # Possibly pass real credentials or environment details here if the constructor needs them
        return {}

    @property
    def tool_invoke_params_example(self) -> dict:
        return {
            "amount_decimal": 1.23,
            "payment_destination_id": "some_real_dest_id",
            "memo": "Integration test"
        }


class TestSearchPayeesToolIntegration(ToolsIntegrationTests):
    @property
    def tool_constructor(self) -> Type[SearchPayeesTool]:
        return SearchPayeesTool

    @property
    def tool_constructor_params(self) -> dict:
        return {}

    @property
    def tool_invoke_params_example(self) -> dict:
        return {
            "name": "Alice",
            "contact_email": "alice@example.com"
            # Possibly real or sandbox data
        }


class TestAddPayeeToolIntegration(ToolsIntegrationTests):
    @property
    def tool_constructor(self) -> Type[AddPayeeTool]:
        return AddPayeeTool

    @property
    def tool_constructor_params(self) -> dict:
        return {}

    @property
    def tool_invoke_params_example(self) -> dict:
        return {
            "type": "CRYPTO_ADDRESS",
            "name": "Integration Crypto Wallet",
            "address": "0x1234567890abcdef",
            "currency": "USDC",
            "tags": ["integration_test"]
        }


class TestAskForMoneyToolIntegration(ToolsIntegrationTests):
    @property
    def tool_constructor(self) -> Type[AskForMoneyTool]:
        return AskForMoneyTool

    @property
    def tool_constructor_params(self) -> dict:
        return {}

    @property
    def tool_invoke_params_example(self) -> dict:
        return {
            "amount_decimal": 5.00,
            "customer_id": "test_customer_integration",
            "memo": "Integration money request"
        }


class TestGetBalanceToolIntegration(ToolsIntegrationTests):
    @property
    def tool_constructor(self) -> Type[GetBalanceTool]:
        return GetBalanceTool

    @property
    def tool_constructor_params(self) -> dict:
        return {}

    @property
    def tool_invoke_params_example(self) -> dict:
        return {
            "customer_id": "test_customer_integration",
            "currency": "USD"
        }
