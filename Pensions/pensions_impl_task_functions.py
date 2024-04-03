# GiG

# This is a weird file. So we have to disable some of the linting errors
# We will be importing lot of functions from other files.
# So we disable Pylint errors : wildcard-import,unused-wildcard-import
# We also disable the corresponding flake errors F401,F403


# pylint: disable=wildcard-import,unused-wildcard-import

import random
import re
from typing import TYPE_CHECKING
from datetime import datetime

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


def validate_amount(context: "UserMessageWithContext") -> TaskEntityFunctionResponse:
    # amount_pattern = re.compile(r'^\d+$')
    amount_pattern = re.compile(r'^\d+(\.\d+)?$')
    input_amount = context.user_response
    ret_val = re.fullmatch(amount_pattern, input_amount)
    return TaskEntityFunctionResponse(success=ret_val is not None)


def get_retirement_calc(context: "UserMessageWithContext") -> TaskEntityFunctionResponse:
    date_of_birth = context.dialog_context.entity_history['date_of_birth']
    retirement_age = context.dialog_context.entity_history['retirement_age']
    annual_income = context.dialog_context.entity_history['annual_income']
    existing_retirement_savings = context.dialog_context.entity_history['existing_retirement_savings']
    annual_contribution = context.dialog_context.entity_history['annual_contribution']
    rate_of_return = context.dialog_context.entity_history['rate_of_return']

    expected_till_age = 95

    current_date = datetime.now()
    dob = datetime.strptime(date_of_birth, "%d-%m-%Y")
    age = current_date.year - dob.year - ((current_date.month, current_date.day) < (dob.month, dob.day))
    # print(f"{date_of_birth} -- {dob} -- {age}")
    
    remaining_years = int(expected_till_age) - int(retirement_age)
    remaining_working_years = int(retirement_age) - int(age)
    # print(f"{remaining_years} -- {remaining_working_years}")
    yearly_need = float(annual_income) * 0.75
    total_amount_needed = yearly_need * remaining_years
    # print(f"{yearly_need} -- {total_amount_needed}")
    future_invested_value = float(annual_contribution) * ((1 + (float(rate_of_return) / 100)) ** remaining_working_years - 1) / (float(rate_of_return) / 100)
    total_estimated_savings = round(future_invested_value + float(existing_retirement_savings), 2)
    # print(f"{total_estimated_savings} -- {future_invested_value}")

    if total_estimated_savings < total_amount_needed:
        message = f"Total amount needed for retirement: {total_amount_needed:,} GHS.\n\nYour estimated retirement savings: {total_estimated_savings:,} GHS.\n\nWe would recommend considering increasing your contributions or adjusting your requirement goals to bridge this gap."
    elif total_estimated_savings > total_amount_needed:
        message = f"Total amount needed for retirement: {total_amount_needed:,} GHS.\n\nYour estimated retirement savings: {total_estimated_savings:,} GHS.\n\nYou are set."
    return TaskEntityFunctionResponse(success=True, text_message=message)


def get_and_display_account_balance(
    context: "UserMessageWithContext",
) -> TaskEntityFunctionResponse:
    retirement_account_number = context.user_response
    message = "For the retirement account *" + retirement_account_number + "*, available account balance is *213,211.72 GHS*."
    return TaskEntityFunctionResponse(success=True, text_message=message)


def get_and_display_claim_status(
    context: "UserMessageWithContext",
) -> TaskEntityFunctionResponse:
    claim_number = context.user_response
    message = "Your claim request *" + claim_number + "* has been successfully filed on *25-Mar-2024*. Status is *'Under Verification'*. Verifications usually take _4-5_ business days."
    return TaskEntityFunctionResponse(success=True, text_message=message)


def get_and_display_wallet_balance(
    context: "UserMessageWithContext",
) -> TaskEntityFunctionResponse:
    message = "Available Balance in your wallet is 1,987.72 GHS"
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


def choose_next_entity(context: "UserMessageWithContext") -> TaskEntityFunctionResponse:
    resp = context.user_response
    next_entity_name = None

    if resp == 'No':
        next_entity_name = "loan_eligibility"
        if 'loans' in context.dialog_context.entity_history:
            context.dialog_context.entity_history['loans'] = '0'
    elif resp == 'Yes':
        next_entity_name = "loans"

    return TaskEntityFunctionResponse(success=True, text_message=next_entity_name)


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
        "recent_transaction_and_amount": "75K GHS at Pizza Hut".lower(),
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
