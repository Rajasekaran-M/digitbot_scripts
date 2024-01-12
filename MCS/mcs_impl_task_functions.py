# GiG

# This is a weird file. So we have to disable some of the linting errors
# We will be importing lot of functions from other files.
# So we disable Pylint errors : wildcard-import,unused-wildcard-import
# We also disable the corresponding flake errors F401,F403


# pylint: disable=wildcard-import,unused-wildcard-import

import random
import re
from typing import TYPE_CHECKING

from digidbot.caml_types.caml_other_types import TaskEntityFunctionResponse
from digidbot.task_entity_functions.entity_processing_functions import *  # noqa: F401,F403

# ###############Dont remove these imports################
# Note:  no need to pass the special_task_functions.py as it should not be exposed outside
from digidbot.task_entity_functions.entity_validation_functions import *  # noqa: F401,F403

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
    message = "For account *XXXXXXX1234* Available Balance is 18,467.28 MUR\nUnclear Balance is 0.00 MUR"
    return TaskEntityFunctionResponse(success=True, text_message=message)


def get_and_display_wallet_balance(
    context: "UserMessageWithContext",
) -> TaskEntityFunctionResponse:
    message = "Available Balance in your wallet is 1,987.72 MUR"
    return TaskEntityFunctionResponse(success=True, text_message=message)

def get_and_display_loan_balance(
    context: "UserMessageWithContext",
) -> TaskEntityFunctionResponse:
    loan_account_number = context.user_response
    message = "The loan balance in your loan account **" + loan_account_number + "** is 234,450.00 MUR."
    return TaskEntityFunctionResponse(success=True, text_message=message)

def get_and_display_deposit_account_balance(
    context: "UserMessageWithContext",
) -> TaskEntityFunctionResponse:
    deposit_account_number = context.user_response
    message = "For the deposit account **" + deposit_account_number + "**, available account balance is **2,677.72 MUR**."
    return TaskEntityFunctionResponse(success=True, text_message=message)

def get_loan_maturity_date(
    context: "UserMessageWithContext",
) -> TaskEntityFunctionResponse:
    message = "Your loan Maturity Date is 13-Dec-2030"
    return TaskEntityFunctionResponse(success=True, text_message=message)

def deposit_account_maturity_date(
    context: "UserMessageWithContext",
) -> TaskEntityFunctionResponse:
    message = "Maturity Date for your deposit account is 01-Dec-2035"
    return TaskEntityFunctionResponse(success=True, text_message=message)

def deposit_account_start_date(
    context: "UserMessageWithContext",
) -> TaskEntityFunctionResponse:
    message = "Start Date for your deposit account is 01-Dec-2023"
    return TaskEntityFunctionResponse(success=True, text_message=message)

def get_cif_id(
    context: "UserMessageWithContext",
) -> TaskEntityFunctionResponse:
    # print("context:", context)
    # print("context.dialog_context:", context.dialog_context)
    # print("context.dialog_context.cur_entity_name:", context.dialog_context.cur_entity_name)
    # print("context.dialog_context.cache_for_entity_functions:", context.dialog_context.cache_for_entity_functions)
    account_name = context.user_response
    # print("account_name:", account_name)
    message = "Dear Customer, your CIF ID is 34567892312."
    return TaskEntityFunctionResponse(success=True, text_message=message)

def get_loan_Status(
    context: "UserMessageWithContext",
) -> TaskEntityFunctionResponse:
    message = "Your loan status is Approved."
    return TaskEntityFunctionResponse(success=True, text_message=message)

def get_loan_amount_disbursed(
    context: "UserMessageWithContext",
) -> TaskEntityFunctionResponse:
    message = "Available loan amount is **2,671.32 MUR**."
    return TaskEntityFunctionResponse(success=True, text_message=message)

def get_emi_amount(
    context: "UserMessageWithContext",
) -> TaskEntityFunctionResponse:
    account_number = context.user_response
    message = "EMI Amount for your loan account " + account_number + " is **2,450.00 MUR**."
    return TaskEntityFunctionResponse(success=True, text_message=message)

def get_deposit_interest_rate(
    context: "UserMessageWithContext",
) -> TaskEntityFunctionResponse:
    account_number = context.user_response
    message = "For your deposit account **" + account_number + "**, the interest rate is **7.1%**."
    return TaskEntityFunctionResponse(success=True, text_message=message)

def get_interest_credit_number(
    context: "UserMessageWithContext",
) -> TaskEntityFunctionResponse:
    account_number = context.user_response
    message = "For your deposit account **" + account_number + "**, the interest is being paid to the Savings Account **SB12345678**."
    return TaskEntityFunctionResponse(success=True, text_message=message)

def get_deposit_interest_accrued(
    context: "UserMessageWithContext",
) -> TaskEntityFunctionResponse:
    account_number = context.user_response
    message = "For your deposit account **" + account_number + "**, the total interest accrued is **3560.00 MUR**."
    return TaskEntityFunctionResponse(success=True, text_message=message)

def get_and_display_last_dividend_payout(
    context: "UserMessageWithContext",
) -> TaskEntityFunctionResponse:
    investment_type = context.user_response
    message = "The last dividend payment for your **" + investment_type + "** was on **28-Dec-2023**. The dividend amount was **1255.00 MUR**."
    return TaskEntityFunctionResponse(success=True, text_message=message)

def get_and_display_shares_and_dividends(
    context: "UserMessageWithContext",
) -> TaskEntityFunctionResponse:
    investment_type = context.user_response
    message = "You currently have **505** shares with the Association, and the last dividend payment for your **" + investment_type + "** was on **28-Dec-2023**. The dividend amount was **1255.00 MUR**."
    return TaskEntityFunctionResponse(success=True, text_message=message)

def get_fd_certificates(
    context: "UserMessageWithContext",
) -> TaskEntityFunctionResponse:
    message = "FD Certificate for your FD Account will be ready by 31-Mar-2024."
    return TaskEntityFunctionResponse(success=True, text_message=message)

def get_fixed_deposit_number(
    context: "UserMessageWithContext",
) -> TaskEntityFunctionResponse:
    message = "Following are the Fixed Deposit Accounts Link to your mobile number\n\n1. 7896543211\n2. 3421590876"
    return TaskEntityFunctionResponse(success=True, text_message=message)

def get_and_display_bank_account_transactions(
    context: "UserMessageWithContext",
) -> TaskEntityFunctionResponse:
    message = """Your recent 5 transactions for savings account '{account_number}' are:
    1. Debit of 50 MUR at Starbucks on 25-Mar-2023
    2. Debit of 100 MUR at Hilton on 20-Mar-2023
    3. Cash withdrawal of 1000 MUR at GCB Bank ATM in Accra on 18-Mar-2023
    4. Debit of 1000 MUR for Rent on 05-Mar-2023
    5. Salary credit of 10000 MUR from Google on 01-Mar-2023.
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
    message = (
        f"""The cheque book has been processed successfully last Friday and mailed to your home address."""
    )
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


######PBU POC randomized authentication related functions
def validate_secret_questions(context: "UserMessageWithContext") -> TaskEntityFunctionResponse:
    answers_to_secret_questions: dict[str, str] = {
        "date_of_birth": "01-01-2000",
        "mother_maiden_name": "rebecca",
        "last_4_digits_of_debit_card": "1234",
        "last_4_digits_of_account_number": "1234",
        "nominee_name": "john",
        "first_pet_name": "krypto",
        "city_of_birth": "accra",
        "recent_transaction_and_amount": "750 MUR at Pizza Hut".lower(),
    }

    answer = context.user_response
    assert (
        answer is not None
        and context.dialog_context is not None
        and context.dialog_context.cur_entity_name is not None
    )
    answer = answer.lower()

    secret_q_dict = context.dialog_context.cache_for_entity_functions.get("secret_q_dict", {})

    if answer == answers_to_secret_questions[context.dialog_context.cur_entity_name]:
        secret_q_dict["num_correct_answers"] = secret_q_dict.get("num_correct_answers", 0) + 1
    else:
        secret_q_dict["num_incorrect_answers"] = secret_q_dict.get("num_incorrect_answers", 0) + 1

    context.dialog_context.cache_for_entity_functions["secret_q_dict"] = secret_q_dict
    # Always return True
    return TaskEntityFunctionResponse(success=True)


def choose_next_security_question(context: "UserMessageWithContext") -> TaskEntityFunctionResponse:
    secret_question_entity_names = [
        "date_of_birth",
        "mother_maiden_name",
        "last_4_digits_of_debit_card",
        "last_4_digits_of_account_number",
        "nominee_name",
        "first_pet_name",
        "city_of_birth",
        "recent_transaction_and_amount",
    ]
    next_entity_name = None

    assert context.dialog_context is not None
    secret_q_dict = context.dialog_context.cache_for_entity_functions.get("secret_q_dict", {})

    num_correct_answers = secret_q_dict.get("num_correct_answers", 0)
    num_incorrect_answers = secret_q_dict.get("num_incorrect_answers", 0)

    # User entered two incorrect values
    # So reset the cache and jump to error
    if num_incorrect_answers >= 2:
        context.dialog_context.cache_for_entity_functions["secret_q_dict"] = {}
        next_entity_name = "exit_message_failure"
    elif num_correct_answers >= 2:
        context.dialog_context.cache_for_entity_functions["secret_q_dict"] = {}
        next_entity_name = "credit_or_debit_card"
    else:
        questions_already_asked = secret_q_dict.get("questions_already_asked", [])
        for q_name in questions_already_asked:
            secret_question_entity_names.remove(q_name)
        next_entity_name = random.choice(secret_question_entity_names)
        questions_already_asked.append(next_entity_name)

        secret_q_dict["questions_already_asked"] = questions_already_asked
        context.dialog_context.cache_for_entity_functions["secret_q_dict"] = secret_q_dict

    return TaskEntityFunctionResponse(success=True, text_message=next_entity_name)


######PBU POC randomized authentication related functions
