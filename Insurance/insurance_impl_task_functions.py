# GiG

# This is a weird file. So we have to disable some of the linting errors
# We will be importing lot of functions from other files.
# So we disable Pylint errors : wildcard-import,unused-wildcard-import
# We also disable the corresponding flake errors F401,F403


# pylint: disable=wildcard-import,unused-wildcard-import

from typing import TYPE_CHECKING
import re

# ###############Dont remove these imports################
# Note:  no need to pass the special_task_functions.py as it should not be exposed outside
from digidbot.task_entity_functions.entity_validation_functions import *  # noqa: F401,F403
from digidbot.task_entity_functions.entity_processing_functions import *  # noqa: F401,F403
from digidbot.caml_types.caml_other_types import TaskEntityFunctionResponse

# ###############Dont remove these imports################

# Segregate imports done solely for static typing
if TYPE_CHECKING:
    from digidbot.channel_helpers.channel_messages import UserMessageWithContext


def validate_phone_number(context: "UserMessageWithContext") -> TaskEntityFunctionResponse:
    pattern = re.compile(r"(\+\d{1,3})?\s?\(?\d{1,4}\)?[\s.-]?\d{3}[\s.-]?\d{4}")
    phone_number = context.user_response
    match = re.search(pattern, phone_number)
    return TaskEntityFunctionResponse(success=match is not None)


def validate_email_address(context: "UserMessageWithContext") -> TaskEntityFunctionResponse:
    regex = r"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b"
    email = context.user_response
    ret_val = re.fullmatch(regex, email)
    return TaskEntityFunctionResponse(success=ret_val is not None)


def get_and_display_account_balance(
    context: "UserMessageWithContext",
) -> TaskEntityFunctionResponse:
    message = "Your account balance is 1 Million USD"
    return TaskEntityFunctionResponse(success=True, text_message=message)


def get_and_display_bank_account_transactions(
    context: "UserMessageWithContext",
) -> TaskEntityFunctionResponse:
    message = """Your recent 5 transactions for savings account '{account_number}' are:
    1. Debit of 50 GHS at Starbucks on 25-Mar-2023
    2. Debit of 100 GHS at Hilton on 20-Mar-2023
    3. Cash withdrawal of 1000 GHS at GCB Bank ATM in Accra on 18-Mar-2023
    4. Debit of 1000 GHS for Rent on 05-Mar-2023
    5. Salary credit of 10000 GHS from Google on 01-Mar-2023.
    """
    return TaskEntityFunctionResponse(success=True, text_message=message)


def validate_num_cheque_leaves(
    context: "UserMessageWithContext",
) -> TaskEntityFunctionResponse:
    resp = context.user_response
    return TaskEntityFunctionResponse(success=resp in ["16", "32", "64"])


def get_and_display_cheque_book_status(
    context: "UserMessageWithContext",
) -> TaskEntityFunctionResponse:
    message = f"""The cheque book has been processed successfully last Friday and mailed to your home address."""
    return TaskEntityFunctionResponse(success=True, text_message=message)


def send_OTP(context: "UserMessageWithContext") -> TaskEntityFunctionResponse:
    return TaskEntityFunctionResponse(success=True, text_message="Sending OTP")


def validate_OTP(context: "UserMessageWithContext") -> TaskEntityFunctionResponse:
    otp = context.user_response
    return TaskEntityFunctionResponse(success=otp == "1234", text_message="Validating OTP")


def validate_debit_or_credit_card(context: "UserMessageWithContext") -> TaskEntityFunctionResponse:
    resp = context.user_response
    success = resp.lower() in ["debit card", "credit card", "debit", "credit"]
    return TaskEntityFunctionResponse(success=success)


def set_user_as_authenticated(context: "UserMessageWithContext") -> TaskEntityFunctionResponse:
    return TaskEntityFunctionResponse(success=True, text_message="User is authenticated")
