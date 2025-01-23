# tests/unit_tests/test_payman_tools.py

from typing import Type
import pytest
from pydantic import ValidationError  # for schema validation checks

from langchain_tests.unit_tests import ToolsUnitTests

# Import your Payman tool classes
from langchain_payman_tool.tools import (
    SendPaymentTool,
    SearchPayeesTool,
    AddPayeeTool,
    AskForMoneyTool,
    GetBalanceTool,
)


class TestSendPaymentToolUnit(ToolsUnitTests):
    @property
    def tool_constructor(self) -> Type[SendPaymentTool]:
        return SendPaymentTool

    @property
    def tool_constructor_params(self) -> dict:
        # If SendPaymentTool's constructor required arguments, place them here.
        return {}

    @property
    def tool_invoke_params_example(self) -> dict:
        # Matches the Pydantic schema in SendPaymentInput
        return {
            "amount_decimal": 10.00,
            "payment_destination_id": "fake_dest_123",
            "customer_id": "cust_001",
            "memo": "Test payment"
        }

class TestSendPaymentToolCustomChecks:
    """Custom parameter checks for SendPaymentTool that are not part of ToolsUnitTests."""

    def test_send_payment_missing_required(self):
        """
        Omit a required field (amount_decimal) to ensure we get a ValidationError.
        """
        tool = SendPaymentTool()
        with pytest.raises(ValidationError):
            tool.invoke({"payment_destination_id": "fake_dest_123"})

    def test_send_payment_wrong_type(self):
        """
        Pass the wrong type (string) for amount_decimal to ensure we get a ValidationError.
        """
        tool = SendPaymentTool()
        with pytest.raises(ValidationError):
            tool.invoke({
                "amount_decimal": "not_a_float",
                "payment_destination_id": "dest_123"
            })


class TestSearchPayeesToolUnit(ToolsUnitTests):
    @property
    def tool_constructor(self) -> Type[SearchPayeesTool]:
        return SearchPayeesTool

    @property
    def tool_constructor_params(self) -> dict:
        return {}

    @property
    def tool_invoke_params_example(self) -> dict:
        return {
            "name": "John",
            "contact_email": "john@example.com",
            "type": "CRYPTO_ADDRESS"
        }

    # Optionally add custom schema tests similar to above if you'd like:
    # def test_missing_fields(self):
    #     ...


class TestAddPayeeToolUnit(ToolsUnitTests):
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
            "name": "My Crypto Wallet",
            "address": "0xFAKE1234ABCDE...",
            "currency": "USDC",
            "tags": ["demo", "crypto"]
        }

    # Similarly, add extra param tests if you want to ensure "address" is required, etc.


class TestAskForMoneyToolUnit(ToolsUnitTests):
    @property
    def tool_constructor(self) -> Type[AskForMoneyTool]:
        return AskForMoneyTool

    @property
    def tool_constructor_params(self) -> dict:
        return {}

    @property
    def tool_invoke_params_example(self) -> dict:
        return {
            "amount_decimal": 25.00,
            "customer_id": "cust_ABC",
            "customer_email": "customer@example.com",
            "memo": "Pay for services"
        }

    # Add any custom tests, e.g. missing amount_decimal


class TestGetBalanceToolUnit(ToolsUnitTests):
    @property
    def tool_constructor(self) -> Type[GetBalanceTool]:
        return GetBalanceTool

    @property
    def tool_constructor_params(self) -> dict:
        return {}

    @property
    def tool_invoke_params_example(self) -> dict:
        return {
            "customer_id": "cust_ABC",
            "currency": "USD"
        }

    # Add custom tests if you like: e.g. invalid currency type or such.
