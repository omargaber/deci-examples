# Exercises on functions

# Design a function that takes in a value and return the sum of all even numbers
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




# Design a function that takes in a value n and returns a list of n elements composed
# of random numbers between 1 and 1000

import random
def random_generator(n):
    final_list = []
    while len(final_list) < n:
        final_list.append(random.randint(1, 1000))
    return final_list





# Design a function that uses the random_generator funtion to generate a list
# of n randomly generated numbers and returns the average of said list

def get_average(n):
    random_list = random_generator(n)
    return sum(random_list) / len(random_list)





# Tweak the random_generator function so that there would not be any duplicates of randomly chosen numbers
# using while loops
import random
def random_generator(n):
    final_list = []
    while len(final_list) < n:
        generated_number = random.randint(1, 1000)
        while generated_number in final_list:
            generated_number = random.randint(1, 1000)
        final_list.append(generated_number)
    return final_list



# Design a function that uses the random_generator funtion to return a list of x random elements (using random.sample or random.choices) 
# from the randomly generated list of n elements.


def get_random_numbers(n, x):        
    random_list = random_generator(n)
    return random.choices(random_list, k=x)
