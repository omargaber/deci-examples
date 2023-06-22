
# While loop that prints numbers from 1 to 10
num = 1
while num <= 10:
    print(num)
    num += 1



# This is a normal for loop that return the sum of even numbers from 1 to 10
total = 0
for i in range(11):
    if i % 2 == 0:
        total += i

# This is how we transform it into a while loop implementation
# Explain to the students the differences between two approaches. Use print statements
# at every iteration to better visualize it for the students
num = 1
total = 0
while num <= 10:
    # print('CURRENT ITERATION -->', num)
    if num % 2 == 0:
        # print(f"NUMBER {num} IS AN EVEN NUMBER")
        total += num
    num += 1
print(total)



# Integrating user input and while loops
while True:
    response = input("Do you like Python? (yes or no) ")
    if response.lower() == "yes":
        print("Great!")
        break
    elif response.lower() == "no":
        print("That's too bad.")
        break
    else:
        print("Invalid response. Please enter 'yes' or 'no'.")


# Make sure you tell the students that user input is always parsed as a string

# Validating user numeric input
# A while loop that asks the user to enter a number and keeps asking until a valid integer is entered:
while True:
    try:
        num = int(input("Enter a number: "))
        break
    except ValueError:
        print("Invalid input. Please enter a valid integer.")

# Another method
num = input("Enter a number: ")
while not num.isdigit():
    print("Invalid input. Please enter a valid integer.")
    num = input("Enter a number: ")
num = int(num)






# Exercises driven by student participation - combination of functions, while loop and validating user input


def get_circle_info(radius):
    circumference = 2 * 3.14 * radius
    area = 3.14 * radius ** 2
    return circumference, area

# For the above example, Ask the students to indentify the function components
# Function name?
# Function parameters?
# Function logic?
# Function return?
# How can I call this function?
# Make the input of the get_circle_info function a user input that needs to be verified to be a numeric value




# ANSWER
# Function name: get_circle_info
# Function parameters: takes one argument upon function call: radius (SHOULD BE A NUMERIC VALUE)
# Function logic: Calculates the circumference and are of the circle from the provided radius
# Function return: Returns two values first is the circumference and second is the are of the circle
# How to call the function?
circumference, area = get_circle_info(5)



radius = input("Enter the radius of the circle: ")
while not radius.isdigit():
    print("Invalid input. Please enter a valid number.")
    radius = input("Enter a number: ")
radius = float(radius)
circumference, area = get_circle_info(radius)
print("Circumference of the circle: ", circumference)
print("Area of the circle: ", area)