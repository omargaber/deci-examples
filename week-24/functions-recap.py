# In this document, there will be a few examples along 
# with exercises for the students that you will prompt them
# to answer during the session


# FUNCION COMPONENTS
# Function name
# Function parameters
# Function logic
# Function return


def adder(x, y):
    value = x+y
    return value

# Also
# def adder(x, y):
#     return x+y

x = adder(3, 4)

# For the above example, we can identify the components of the function
# Function name: adder
# Function parameters: takes two arguments upon function call: x and y (BOTH SHOULD BE NUMERIC VALUES)
# Function logic: Adds the arguments passed together
# Function return: Expects to return one value (summation of passed arguments)



def average(numbers):
    return sum(numbers) / len(numbers)

# For the above example, we can identify the components of the function
# Function name: average
# Function parameters: takes one argument upon function call: numbers (SHOULD BE A LIST OF NUMERIC VALUES)
# Function logic: Returns the average by summing the list elements and dividing them by the number of elements.
# Function return: Expects to return one value (average of passed arguments)

x = average([1,2,3,4,5,6])




# Multi value return function
def square_numbers_passed(x,y):
    return x**2, y**2

# For the above example, we can identify the components of the function
# Function name: square_numbers_passed
# Function parameters: akes two arguments upon function call: x and y (BOTH SHOULD BE NUMERIC VALUES)
# Function logic: Returns the square of the arguments passed to the function
# Function return: Expects to return TWO values (square of both numebrs)


# For multi-value return functions show them students how the function should be called

num1, num2 = square_numbers_passed(2,3)
# Notice here that the function call that has 2 returns needs to have values stored in 
# variables with the same number of return values





# Exercises drive by students participation

def longest_string(strings):
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
x = longest_string(["THIS IS", "THE LONGEST STRING", "Hello"])
