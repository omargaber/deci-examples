# In this document, there will be a few examples along 
# with exercises for the students that you will prompt them
# to answer during the session

# 1. What is a function?
#  - A function is a block of code that performs a specific task.
#  - It is a reusable piece of code that can be called multiple times.
#  - It can take parameters and return values.
#  - It can be used to organize code into logical blocks.
#  - It can be used to avoid repetition of code.
#  - It can be used to make code easier to understand.


# FUNCION COMPONENTS
# Function name
# Function parameters
# Function logic
# Function return


def add_wo_numbers(x, y):
    value = x+y
    return value

# Also
# def add_wo_numbers(x, y):
#     return x+y

x = add_wo_numbers(3, 4)

# For the above example, we can identify the components of the function
# Function name: add_wo_numbers
# Function parameters: takes two arguments upon function call: x and y (BOTH SHOULD BE NUMERIC VALUES)
# Function logic: Adds the arguments passed together
# Function return: Expects to return one value (summation of passed arguments)



def get_average(numbers):
    return sum(numbers) / len(numbers)

# For the above example, we can identify the components of the function
# Function name: get_average
# Function parameters: takes one argument upon function call: numbers (SHOULD BE A LIST OF NUMERIC VALUES)
# Function logic: Returns the average by summing the list elements and dividing them by the number of elements.
# Function return: Expects to return one value (average of passed arguments)

x = get_average([1,2,3,4,5,6])




# Multi value return function
def square_two_numbers(x,y):
    return x**2, y**2

# For the above example, we can identify the components of the function
# Function name: square_two_numbers
# Function parameters: akes two arguments upon function call: x and y (BOTH SHOULD BE NUMERIC VALUES)
# Function logic: Returns the square of the arguments passed to the function
# Function return: Expects to return TWO values (square of both numebrs)


# For multi-value return functions show them students how the function should be called

num1, num2 = square_two_numbers(2,3)
# Notice here that the function call that has 2 returns needs to have values stored in 
# variables with the same number of return values





# Exercises drive by students participation

def get_longest_string(strings):
    longest_string = ""
    for string in strings:
        if len(string) > len(longest_string):
            longest_string = string
    return longest_string

# For the above example, Ask the students to indentify the function components
# Function name?
# Function parameters?
# Function logic?
# Function return?




# ANSWER
# Function name: longest_string
# Function parameters: takes one argument upon function call: strings (SHOULD BE A LIST OF STRINGS)
# Function logic: Stores the longest string from the passed arguments in a variable to return the longest string
# Function return: Returns one value that is of string format
x = get_longest_string(["THIS IS", "THE LONGEST STRING", "Hello"])
