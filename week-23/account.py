import random
import time

def validate_input(value):
    try:
        if eval(value):
            return True, eval(value)
    except:
        print("ECC")
        print(value, type(value))
        return False, str(value)


def banking_operations(account):
    while True:
        operation_message = "Please pick an operation you want to perform on your account.\n1- Account Details.\n2- Deposit.\n3- Withdraw.\n4- Exit.\n"
        operation_action, opereation_value = validate_input(input(operation_message))

        while not operation_action or operation_action not in [1,2,3,4]:
            operation_action, opereation_value = validate_input(input(f"Invalid input.\m{operation_message}"))

        if opereation_value == 4:
            break

        if opereation_value == 1:
            account.details()

        if opereation_value == 2:
            prompt_message = "Please input the amount you want to deposit: "
            deposit_flag, deposit_amount = validate_input(input(prompt_message))

            while not deposit_flag or deposit_amount <= 0:
                deposit_flag, deposit_amount = validate_input(input(f"Invalid input.\n{prompt_message}"))

            account.deposit(deposit_amount)
            
        
        if opereation_value == 3:
            prompt_message = "Please input the amount you want to withdraw: "
            deposit_flag, withdraw_amount = validate_input(input(prompt_message))

            while not deposit_flag or withdraw_amount <= 0:
                deposit_flag, deposit_amount = validate_input(input(f"Invalid input.\n{prompt_message}"))

            account.withdraw(withdraw_amount)
        
        print(account.details())
        
    
class Account:
    
    name: str = None
    email: str = None
    balance: float = 0
    
    def __init__(self, name, email, balance=0):
        self.name = name
        self.email = email
        self.balance = balance
        
        print(self.details())
    
    def details(self):
        return {
            "name": self.name,
            "email": self.email,
            "balance": self.balance
        }
        
    
    def deposit(self, amount):
        self.balance += amount
        return True
    
    def withdraw(self, amount):
        flag, value = validate_input(amount)
        while not flag or value <= 0:
            flag, value = validate_input(input("Invalid input. Please input the amount you want to withdraw: "))
        
        while not flag or value > self.balance:
            flag, value = validate_input(input(f"Insufficient funds. Please try amounts <= {self.balance}: "))
        
        self.balance -= value
        return True, self.balance
    

banks = [
    "HSBC",
    "NBE",
    "CIB"
]

main_prompt = "Kidnly choose from the following actions:\n1- Create an account.\n2- Exit.\n"
def main():
    bank_name = random.choice(banks)
    print(f"Welcome to {bank_name} banking services.")
    time.sleep(2)

    input_flag, value = validate_input(input(main_prompt))
    while not input_flag or value not in [1,2]:
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
        email = input(
            "Please enter a valid name, should have at least one character: "
        )
    
    
    balance_flag, balance_amount = validate_input(input("Please input your initial balance: "))
    while not balance_flag or balance_amount <= 0:
        balance_flag, balance_amount = validate_input(input("Please input a valid amount more than 0: "))
        
    created_account = Account(
        name=name,
        email=email,
        balance=balance_amount
    )
    
    banking_operations(created_account)
    return


main()    
    