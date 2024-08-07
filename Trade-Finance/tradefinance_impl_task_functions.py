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


def get_and_display_shipment_status(
    context: "UserMessageWithContext",
) -> TaskEntityFunctionResponse:
    shipment_number = context.user_response

    message = f"Your shipment {shipment_number} is currently at the port of Singapore, scheduled to depart tomorrow. Expected arrival in New York is on July 10th."
    return TaskEntityFunctionResponse(success=True, text_message=message)


def get_and_display_payment_status(
    context: "UserMessageWithContext",
) -> TaskEntityFunctionResponse:
    invoice_number = context.user_response

    message = f"The payment for invoice {invoice_number} has been processed and is expected to be credited to your account within 2 business days."
    return TaskEntityFunctionResponse(success=True, text_message=message)

def get_and_display_eligibility_details(
    context: "UserMessageWithContext",
) -> TaskEntityFunctionResponse:
    value_of_invoice = float(context.user_response)
    advance_amount = value_of_invoice * (80 / 100)

    message = f"Advance Amount: ${advance_amount:,} (80%)\n\nPeriod: 90 days from the issue of advance\n\nFactoring Fee: 2%\n\nInterest Rate: 4%"
    return TaskEntityFunctionResponse(success=True, text_message=message)

def get_and_display_transaction_details(
    context: "UserMessageWithContext",
) -> TaskEntityFunctionResponse:
    pending_transaction = context.user_response
    transaction_amount = 12500

    message = f"Details:\n\nValue Date: 2024-07-10\nSender Ref. No.: {pending_transaction}\nAmount: ${transaction_amount:,}"
    return TaskEntityFunctionResponse(success=True, text_message=message)

def get_confirmation(context: "UserMessageWithContext") -> TaskEntityFunctionResponse:
    credit_account = context.dialog_context.entity_history['credit_account']
    from_account = context.dialog_context.entity_history['from_account']
    purpose_category = context.dialog_context.entity_history['purpose_category']
    transaction_amount = 12500
    
    message = f"Credit Account: {credit_account}\nAmount: ${transaction_amount:,}\nPurpose Category: {purpose_category}\nDeduct Charges From: {from_account}"
    return TaskEntityFunctionResponse(success=True, text_message=message)


def get_and_display_report_summary(
    context: "UserMessageWithContext",
) -> TaskEntityFunctionResponse:
    report_name = context.dialog_context.entity_history['report_name']
    
    message = f"Your {report_name} report is ready.\n\nPlease find the same attached here. Thanks for choosing My Hospital."
    return TaskEntityFunctionResponse(success=True, text_message=message)

def get_the_estimated_bill_value(
    context: "UserMessageWithContext",
) -> TaskEntityFunctionResponse:
    service_name = context.dialog_context.entity_history['service_name']
    department_name = context.dialog_context.entity_history['department_name']

    services_and_cost: dict[str, str] = {
        "ENT": {
            "Consulting": "$150-$200",
            "Surgery": "$1000-$2000",
            "Emergency Services": "$750-$1500"
        },
        "General Medicine": {
            "Consulting": "$100-$150",
            "Surgery": "$1500-$2500",
            "Emergency Services": "$1000-$1700"
        },
        "Dermatology": {
            "Consulting": "$200-$250",
            "Surgery": "$3000-$4000",
            "Emergency Services": "$500-$1000"
        },
        "Gynaecology": {
            "Consulting": "$250-$300",
            "Surgery": "$1500-$2500",
            "Emergency Services": "$2000-$2500"
        },
        "Orthopaedics": {
            "Consulting": "$400-$500",
            "Surgery": "$2500-$3500",
            "Emergency Services": "$1500-$1750"
        },
        "Pediatrics": {
            "Consulting": "$50-$100",
            "Surgery": "$3500-$4500",
            "Emergency Services": "$1250-$1750"
        }
    }

    bill_value = services_and_cost[department_name][service_name]
    
    message = f"The tentative bill value:\n\nService: {service_name}\nDepartment: {department_name}\nBill Value: would be within the range of {bill_value}."
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
