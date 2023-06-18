import random
import time
from validation import parse_num, validate_email, validate_name, validate_new_balance
from operations import create_account, deposit, withdraw, get_details


BANKS = ["HSBC", "NBE", "CIB", "NBK"]

MAIN_PROMPT = (
    "Kindly choose from the following actions:\n1- Create an account.\n2- Exit.\n"
)
OPERATION_MESSAGE = """Please pick an operation you want to perform on your account.
    1- Account Details.
    2- Deposit.
    3- Withdraw.
    4- Exit.
    Please input the action number: """


def create_account_view():
    """a view for creating bank account via terminal

    Returns:
        dict: the new bank account
        str | None: None if the process completed successfully, otherwise and error message returned
    """
    name = input("Please enter your name: ")

    while not validate_name(name):
        name = input("Please enter a valid name, should have at least one character: ")

    email = input("Please enter your email address: ")
    while not validate_email(email):
        email = input("Please enter a valid name, should contain @ symbol : ")

    balance_amount = input("Please input your initial balance: ")

    while not validate_new_balance(balance_amount):
        balance_amount = input("Please input a valid number greater than 0: ")
    account, error = create_account(name, email, parse_num(balance_amount))

    return account, error


def account_operations_view(account: dict):
    """a view for selecting and executing an account operation via terminal

    Args:
        account (dict):
    """
    while True:
        operation_value = parse_num(input(OPERATION_MESSAGE))

        while operation_value == None or operation_value not in [1, 2, 3, 4]:
            operation_value = input(f"Invalid input.\n{OPERATION_MESSAGE}")

        print(f"You select number: {operation_value}")
        if operation_value == 4:
            return
        elif operation_value == 1:
            error = details_view(account)
        elif operation_value == 2:
            account, error = deposit_view(account)
        elif operation_value == 3:
            account, error = withdraw_view(account)
        if error:
            print(f"operation error!\n{error}")
        else:
            print(f"operation successfully completed!")

        if operation_value != 1:
            print(f"available balance now is {account['balance']}")
        print("----------------------------------------------------")


def details_view(account):
    """a view for printing the account information to terminal

    Args:
        account (dict):
    """
    account, error = get_details(account)
    if error:
        print(f"operation error!\n{error}")
    else:
        print(
            "========================= Here are your account details ========================="
        )
        print("account owner: ", account["name"])
        print("Email address: ", account["email"])
        print("Available Balance: ", account["balance"])
    return error


def deposit_view(account: dict):
    """a view for depositing operation

    Args:
        account (dict):
    Returns:
        dict: the modified bank account
        str | None: None if the process completed successfully, otherwise and error message returned
    """
    prompt_message = "Please input the amount you want to deposit: "
    deposit_amount = parse_num(input(prompt_message))

    while deposit_amount == None or deposit_amount <= 0:
        deposit_amount = parse_num(input(f"Invalid input.\n{prompt_message}"))
    account, error = deposit(account, deposit_amount)
    return account, error


def withdraw_view(account):
    """a view for withdrawing operation

    Args:
        account (dict):
    Returns:
        dict: the modified bank account
        str | None: None if the process completed successfully, otherwise and error message returned
    """
    prompt_message = "Please input the amount you want to withdraw: "
    withdraw_amount = parse_num(input(prompt_message))

    while withdraw_amount == None or withdraw_amount <= 0:
        withdraw_amount = parse_num(input(f"Invalid input.\n{prompt_message}"))

    account, error = withdraw(account, withdraw_amount)
    return account, error


def main():
    """CLI bank management system"""
    bank_name = random.choice(BANKS)
    print(f"Welcome to {bank_name} banking services.")
    time.sleep(2)
    while True:
        value = parse_num(input(MAIN_PROMPT))
        while value is None or value not in [1, 2]:
            value = parse_num(input(f"Invalid input.\n{MAIN_PROMPT}"))

        if value == 2:
            print(f"Thank you for using {bank_name} banking services.")
            break

        account, error = create_account_view()
        if error:
            print("we have difficulties to process your request now due to an error")
            print(f"Error: {error}")
            continue
        else:
            account_operations_view(account)
        print(f"Thank you for using {bank_name} banking services.")


if __name__ == "__main__":
    main()
