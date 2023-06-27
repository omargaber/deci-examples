# User inputs in python

# input() function is used to take user input
# input() function always returns a string
# to convert the input to a number, we need to use int() or float() functions
# but we need to make sure that the input is a number before converting it to a number in order to avoid errors


# Validate user input (numbers, strings, etc.)


#  validate user input as a string:
#  we will use isalpha() function to check if the input is a alphabetic string or not
#  ***Note: isalpha() function returns True if all characters in the string are alphabetic and there is at least one character, False otherwise.***
#  spaces are not considered alphabetic characters

def validate_string(name):
    if name.isalpha():
        print("Valid name")
        return True
    else:
        print("Invalid name")
        return False

user_name = input("Enter your name: ")

validate_string(user_name)

while not validate_string(user_name):
    user_name = input("Enter your name: ")
# ----------------------------------------------

# validate user input as a number:
# we will use isdigit() function to check if the input is a number or not
# note: isdigit() function returns True if all characters in the string are digits and there is at least one character, False otherwise.
# spaces are not considered digits

def validate_number(number):
    if number.isdigit():
        print("Valid number")
        return True
    else:
        print("Invalid number")
        return False

id = input("Enter your ID: ")

validate_number(id)

while not validate_number(id):
    id = input("Enter your ID: ")

# ----------------------------------------------
