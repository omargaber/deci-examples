import random
import time
from utils import validate_input, banking_operations



banks = ["HSBC", "NBE", "CIB"]

main_prompt = (
    "Kidnly choose from the following actions:\n1- Create an account.\n2- Exit.\n"
)



def main():
    bank_name = random.choice(banks)
    print(f"Welcome to {bank_name} banking services.")
    time.sleep(2)

    input_flag, value = validate_input(input(main_prompt))
    while not input_flag or value not in [1, 2]:
        input_flag, value = validate_input(input(f"Invalid input.\n{main_prompt}"))

    if value == 2:
        print(f"Thank you for using {bank_name} banking services.")
        return

    time.sleep(2)
    name = input("Please enter your name: ")

    while len(name) == 0:
        name = input("Please enter a valid name, should have at least one character: ")

    email = input("Please enter your email address: ")
    while len(email) == 0:
        email = input("Please enter a valid name, should have at least one character: ")

    balance_flag, balance_amount = validate_input(
        input("Please input your initial balance: ")
    )
    while not balance_flag or balance_amount <= 0:
        balance_flag, balance_amount = validate_input(
            input("Please input a valid amount more than 0: ")
        )

    created_account = {
        "name": name,
        "email":email,
        "balance":balance_amount}

    banking_operations(created_account)
    print(f"Thank you for using {bank_name} banking services.")
    return


main()
