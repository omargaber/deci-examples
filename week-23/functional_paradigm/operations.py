from validation import parse_num, validate_email, validate_name, validate_new_balance
from utilis import processing_sleep
from mockdb import exists_users

def create_account(name: str, email: str, new_balance: float | int):
    """Create a new bank account

    Args:
        name (str): owner name
        email (str): owner email address
        new_balance (float | int): the initial balance

    Returns:
        dict: dict contain account information
    """
    processing_sleep()
    # backend validation should goes here (check user is exists, etc)
    if name.lower() in exists_users:
        return {}, "user name is already exists!"
    return {"name": name, "email": email, "balance": new_balance}, None


def deposit(account: dict, amount: float | int):
    """deposit an amount to account

    Args:
        account (dict):
        amount (float | int):

    Returns:
        dict: modified account
        str | None: None if the process completed successfully, otherwise and error message returned
    """
    processing_sleep()
    account["balance"] += amount
    return account, None


def withdraw(account: dict, amount: float | int):
    """withdraw an amount from account

    Args:
        account (dict):
        amount (float | int):

    Returns:
        dict: modified account
        str | None: None if the process completed successfully, otherwise and error message returned
    """
    processing_sleep()
    if account["balance"] < amount:
        return (
            account,
            f"Insufficient funds. Please try amounts <= {account['balance']}",
        )
    account["balance"] -= amount
    return account, None


def get_details(account: dict):
    """return full account details

    Args:
        account (dict):

    Returns:
        dict: full account details
        str | None: None if the process completed successfully, otherwise and error message returned
    """
    processing_sleep()
    # just simulate a backend call, but no thing done here for real
    return {
        "name": account["name"],
        "email": account["email"],
        "balance": account["balance"],
    }, None
