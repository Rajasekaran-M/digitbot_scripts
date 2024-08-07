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


def validate_amount(context: "UserMessageWithContext") -> TaskEntityFunctionResponse:
    # amount_pattern = re.compile(r'^\d+$')
    amount_pattern = re.compile(r'^\d+(\.\d+)?$')
    input_amount = context.user_response
    ret_val = re.fullmatch(amount_pattern, input_amount)
    return TaskEntityFunctionResponse(success=ret_val is not None)


def get_loan_eligibility(context: "UserMessageWithContext") -> TaskEntityFunctionResponse:
    print(f"context.dialog_context.cache_for_entity_functions: {context.dialog_context.cache_for_entity_functions}")
    if 'loans' in context.dialog_context.entity_history:
        loans = context.dialog_context.entity_history['loans']
    else:
        loans = float(0)
    total_earnings = context.dialog_context.entity_history['total_earnings']
    deposits = context.dialog_context.entity_history['deposits']
    leave_travel_allowance = context.dialog_context.entity_history['leave_travel_allowance']
    total_deductions = context.dialog_context.entity_history['total_deductions']
    basic_salary = context.dialog_context.entity_history['basic_salary']

    try:
        adjusted_earnings = float(total_earnings) - float(leave_travel_allowance)
        adjusted_deductions = float(total_deductions) + ( float(basic_salary) / 3) - (float(leave_travel_allowance) * 0.3 )
        available_installment_amount = round(float(adjusted_earnings) - float(adjusted_deductions), 0)
        available_loan_amount = round((float(deposits) * 3) - float(loans), 0)
    except ValueError as e:
        print(f"Error: {e}")
        adjusted_earnings = adjusted_deductions = available_installment_amount = available_loan_amount = 0.0
    
    message = ""
    
    if available_installment_amount < 0:
        message += "There is not enough earnings to cover the installment.\n\n"
    if available_loan_amount < 0:
        message += "Sorry. The loan eligibility criteria has not been met. Please contact our branch for more details.\n\n"
    
    if message == "":
        message += f"Available Installment Amount: {available_installment_amount:,} KES.\n\nAvailable Loan Amount: {available_loan_amount:,} KES."
    return TaskEntityFunctionResponse(success=True, text_message=message)

def get_confirmation(context: "UserMessageWithContext") -> TaskEntityFunctionResponse:
    transfer_amount = context.dialog_context.entity_history['transfer_amount']
    transfer_amount_int = int(transfer_amount)
    from_account = context.dialog_context.entity_history['from_account']
    beneficiary = context.dialog_context.entity_history['beneficiery']
    remarks = context.dialog_context.entity_history['remarks']
    
    message = f"You have requested a transfer of MUR {transfer_amount_int:,} from {from_account} to {beneficiary} towards {remarks}."
    return TaskEntityFunctionResponse(success=True, text_message=message)

def show_outstanding_bill(context: "UserMessageWithContext") -> TaskEntityFunctionResponse:
    biller = context.dialog_context.entity_history['biller']
    
    message = f"You have an outstanding bill of MUR 2,000.00 from {biller} due on 18-Jul-2024."
    return TaskEntityFunctionResponse(success=True, text_message=message)

def show_final_confirmation(context: "UserMessageWithContext") -> TaskEntityFunctionResponse:
    biller = context.dialog_context.entity_history['biller']
    bill_amount = 2000
    
    message = f"You have requested to pay MUR {bill_amount:,} to {biller}."
    return TaskEntityFunctionResponse(success=True, text_message=message)


def get_and_display_account_balance(
    context: "UserMessageWithContext",
) -> TaskEntityFunctionResponse:
    message = "For account *XXXXXXX1234* Available Balance is 18,467.28 GHS\nUnclear Balance is 0.00 GHS"
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
