import time

def validate_input(value):
    try:
        if float(value):
            return True, float(value)

        return False, float(value)
    except:
        return False, str(value)


def details(account):
    print(
        "========================= Here are your account details ========================="
    )
    return {
        "name": account["name"],
        "email": account["email"],
        "balance": account["balance"],
    }


def deposit(account, amount):
    account["balance"] += amount
    return account


def withdraw(account):
    prompt_message = "Please input the amount you want to withdraw: "
    flag, value = validate_input(input(prompt_message))
    while not flag or value <= 0 or value > account["balance"]:
        if not flag or value <= 0:
            flag, value = validate_input(input("Invalid input. {prompt_message}"))
        else:
            flag, value = validate_input(
                input(f"Insufficient funds. Please try amounts <= {account['balance']}: ")
            )
    account["balance"] -= value
    return True, account





def processing_sleep():
    print("=======Processing=======")
    time.sleep(2)


def banking_operations(account):
    while True:
        operation_message = "Please pick an operation you want to perform on your account.\n1- Account Details.\n2- Deposit.\n3- Withdraw.\n4- Exit.\nPlease input the action number: "
        operation_action, opereation_value = validate_input(input(operation_message))

        while not operation_action or operation_action not in [1, 2, 3, 4]:
            operation_action, opereation_value = validate_input(
                input(f"Invalid input.\m{operation_message}")
            )

        processing_sleep()

        if opereation_value == 4:
            return account

        if opereation_value == 1:
            print(details(account))

        if opereation_value == 2:
            prompt_message = "Please input the amount you want to deposit: "
            deposit_flag, deposit_amount = validate_input(input(prompt_message))

            while not deposit_flag or deposit_amount <= 0:
                deposit_flag, deposit_amount = validate_input(
                    input(f"Invalid input.\n{prompt_message}")
                )

            deposit(account, deposit_amount)

        if opereation_value == 3:
            withdraw(account)

        if opereation_value != 1:
            processing_sleep()
            print(details(account))
        print("----------------------------------------------------")
        time.sleep(2)
