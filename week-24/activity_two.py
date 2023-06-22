
# Write a few pieces of code that asks the user for numeric input and validates 
# that the input was numeric
n = input("Enter a number: ")
while not n.isdigit():
    print("Invalid input. Please enter a valid number.")
    n = input("Enter a number: ")
n = int(n)




# The user validation scipt could be written as a function so we can re-use it. Encapsulate the 
# input validation into a function and re-use it in the upcoming tasks
def int_validator():
    n = input("Enter a number: ")
    while not n.isdigit():
        print("Invalid input. Please enter a valid number.")
        n = input("Enter a number: ")
    return int(n)



# Design a function that prompts the user to input a NUMERIC value and return the sum of all even numbers
# between 1 and the passed value. Write the function once using for loop and once using while loop

# While loop implementation

def get_sum_even_numbers(n):
    total = 0
    i = 2
    while i <= n:
        total += i
        i += 2
    return total

# For loop implementation
def get_sum_even_numbers(n):
    total = 0
    for i in range(n+1):
        if i%2 == 0:
            total += i
    return total

n = int_validator()
get_sum_even_numbers(n)


# Add the validator functionality for random_generator funciton
import random
def random_generator(n):
    final_list = []
    while len(final_list) < n:
        final_list.append(random.randint(1, 1000))
    return final_list

n = int_validator()
x = random_generator(n)



# Add the validator functionality for get_average function
def get_average(n):
    random_list = random_generator(n)
    return sum(random_list) / len(random_list)
n = int_validator()
x = get_average(n)



# Add the validator functionality for the get_random_numbers function. 
# The validation should apply for both arguments of the function
def get_random_numbers(n, x):        
    random_list = random_generator(n)
    return random.choices(random_list, k=x)

n = int_validator()
x = int_validator()
final = get_random_numbers(n, x)