# what is Function?
# A function is a block of code that runs only when it is called.

# why use function?

# 1. Avoid repetition code
# 2. Makes program clean & organised.
# 3. easy to debug and reuse

# #syntax
# def function_name():
#     #code to execute

#example:
# def greet():
#     print("hello students")

# greet() #calling the function
#-------------------------------------------------------------------------------------
# function with parameters:
# used to pass values

# def greet (name="student"):
#     print(f"hello {name}")

# greet()
# greet("shreyarth")
# greet("AICW")

#----------------------------------------------------------------------------------------

# function with return type:
#used when we want to send result back 

# def add (a,b):
#     return a+b

# result = add(2,3)
# print(result)

#------------------------------------------------------------------------------------------

# Task 1 : Create a function for calculator.
def calculator(num1, num2, operator):
    if operator == "+":
        return num1 + num2
    elif operator == "-":
        return num1 - num2
    elif operator == "*":
        return num1 * num2
    elif operator == "/":
        if num2 != 0:
            return num1 / num2
        else:
            return "Error: Division by zero is not allowed."
    else:
        return "Error: Invalid operator."
number1 = float(input("Enter first number: "))
number2 = float(input("Enter second number: "))
operator = input("Enter operator (+, -, *, /): ")
result = calculator(number1, number2, operator)
print("Result:", result)

# Output: Enter first number: 10
# Enter second number: 5
# Enter operator (+, -, *, /): *
# Result: 50.0
print("------------------------------------------------------------------------------------------")



# Task 2: Create a function to check if a number is even or odd.
# Hint: use modulus operator %
#Alternative:
# def check_even_odd(num):
#     if num % 2 == 0:
#         return "Even"
#     else:
#         return "Odd"

# # Test cases
# print(check_even_odd(4))  # Output: Even
# print(check_even_odd(7))  # Output: Odd


def check_even_odd(num):
    if num % 2 == 0:
        return "Even"
    else:
        return "Odd"
number = int(input("Enter a number: "))
result = check_even_odd(number)
print("The number is:", result)

#Output: Enter a number: 5
# The number is: Odd
print("------------------------------------------------------------------------------------------")


# Task 3 : Create a function to calculate the factorial of a number.
# Hint: use for loop or recursion
def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)
number = int(input("Enter a number: "))
result = factorial(number)
print("Factorial of", number, "is", result)

# Output: Enter a number: 5
# Factorial of 5 is 120
print("------------------------------------------------------------------------------------------")




#Task 4 : Create a function to find the maximum of three numbers.
# Hint: use if-elif-else statements
def find_maximum(a, b, c):
    if a >= b and a >= c:
        return a
    elif b >= a and b >= c:
        return b
    else:
        return c
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
num3 = float(input("Enter third number: "))
result = find_maximum(num1, num2, num3)
print("The maximum number is:", result)

# Output: Enter first number: 5
# Enter second number: 10       
# Enter third number: 3
# The maximum number is: 10.0
print("------------------------------------------------------------------------------------------")




# Task 5 : Create a function to check if a string is palindrome
def is_palindrome(s):
    # Remove non-alphanumeric characters and convert to lowercase
    s = ''.join(c.lower() for c in s if c.isalnum())
    # Check if the string is equal to its reverse
    return s == s[::-1]

# Test the function
test_string = input("Enter a string: ")
if is_palindrome(test_string):
    print("The string is a palindrome.")
else:
    print("The string is not a palindrome.")

# Output: Enter a string: Madam
# The string is a palindrome.   
print("------------------------------------------------------------------------------------------")





# Task 6 : Create a function to calculate the area of a circle.

def area_of_circle(radius):
    if radius < 0:
        return "Error: Radius cannot be negative."
    pi = 3.14159
    return pi * (radius ** 2)

radius = float(input("Enter the radius of the circle: "))
area = area_of_circle(radius)
print(f"The area of the circle with radius {radius} is {area}.")

# Output: Enter the radius of the circle: 5
# The area of the circle with radius 5.0 is 78.53975.
print("------------------------------------------------------------------------------------------")



