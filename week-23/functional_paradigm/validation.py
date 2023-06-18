import time


def parse_num(candidate: str):
    """Parse string to number if possible
    It work equally well with negative and positive numbers, integers and floats.

    Args:
        candidate (str): string to convert

    Returns:
        float | int | None: float or int if possible otherwise None
    """
    try:
        float_number: float = float(candidate)
    except ValueError:
        return None
    else:
        if float_number.is_integer():
            return int(float_number)
        return float_number


def validate_name(name: str):
    """validate user name

    Args:
        name (str): user name

    Returns:
        bool: True if name len >= 1, otherwise False
    """
    return len(name) >= 1


def validate_email(email: str):
    """validate email address

    Args:
        email (str): user email

    Returns:
        bool: True if email contain @ symbol, otherwise False
    """
    return "@" in email


def validate_new_balance(balance: str):
    """validate initial balance

    Args:
        balance (str): account balance

    Returns:
        bool: True if can be parsed to number greater than zero, otherwise False
    """
    return parse_num(balance) and parse_num(balance) > 0
