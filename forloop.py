# What is for loop?
# A loop is used to repeat a block of code multiple times until a condition is met.

# Types of Loops in Python

    ## 1. for loop
    # Used when we know how many times we want to repeat.

# Syntax:
# for variable in sequence:
#   #code

# range() function is commonly used to generate a
# sequence of numbers.

# range comes with 3 parameters:
# 1. start (inclusive)
# 2. stop (exclusive)
# 3. step (optional, default is 1)

# range(start, stop-1, stop)

# Example:
# for i in range(5):
#     print(i)



    ## 2. while loop
    # Used when we repeat until a condition becomes false.

# syntax:
# while condition:
#   #code

# Example:
# i = 1
# while i <= 5:
#     print(i)
#     i += 1

### Loop Control Statements
    # 1. break 
    # stops the loop immediately

    #example:
# for i in range(1, 6):
#     if i == 3:
#         break
#     print(i)
    #Output: 1, 2

    # 2. continue
    # skips the current iteration

    # example:
# for i in range(1, 6):
#     if i == 3:
#         continue
#         print(i)
    # Output: 1, 2, 4, 5

    # 3. Pass
    # does nothing (placeholder)

    #example:
# for i in range(5):
#     pass


#-----------------------------------------------------------------------------------------------

# Task 1 : Print number 1 to 10 using for loop
for i in range(1, 11):
     print(i)

#Output: 1, 2, 3, 4, 5, 6, 7, 8, 9, 10
print("------------------------------------------------------------------------------------------")




# Task 2 : Print even numbers from 1 to 20 using for loop
for i in range(1, 21):
     if i % 2 == 0:
        print(i)

# Output: 2, 4, 6, 8, 10, 12, 14, 16, 18, 20

#alternative
# for i in range(2,21,2):
# print(i, end="")
print("------------------------------------------------------------------------------------------")



# Task 3 : Print odd numbers from 1 to 15 using for loop
#alternative for descending
# for i in range(21,2,-2):
# print(i, end="")

for i in range(1, 16):
    if i % 2 != 0:
        print(i)

# Output: 1, 3, 5, 7, 9, 11, 13, 15
print("------------------------------------------------------------------------------------------")




# Task 4 : Print each character of the string.
# text = "Python"
for char in "Python":
    print(char)

# Output: P
#         y
#         t
#         h
#         o
#         n
print("------------------------------------------------------------------------------------------")



#Task 5 : Print all items in the list.
fruits = ["Data", "Science", "AI"]
for fruit in fruits:
    print(fruit)

# Output: Data
#         Science
#         AI
print("------------------------------------------------------------------------------------------")


# Task 6 : Find the sum of all number from 1 to 10 using for loop
total = 0
for i in range(1, 11):
    total += i
print("Sum of numbers from 1 to 10:", total)


# Output: Sum of numbers from 1 to 10: 55
print("------------------------------------------------------------------------------------------")

#Task 7 : Print the multiplication table of 5 using for loop
    #alternative
    # num = 5
    # for i in range(1, 11):
    #     print(num, "x", i, "=", num * i)

for i in range(1, 11):
    print(f"5 x {i} = {5 * i}")

# f = format string, allows embedding expressions inside string literals using {}

# Output: 5 x 1 = 5
#         5 x 2 = 10
#         5 x 3 = 15
#         5 x 4 = 20
#         5 x 5 = 25
#         5 x 6 = 30
#         5 x 7 = 35
#         5 x 8 = 40
#         5 x 9 = 45
#         5 x 10 = 50
print("------------------------------------------------------------------------------------------")

# Task 8 : Count how many vowels are in the string.
text = "Hello World"
vowels = "aeiouAEIOU"
count = 0
for char in text:
    if char in vowels:
        count += 1
print("Number of vowels in the string:", count)

# Output: Number of vowels in the string: 3
print("------------------------------------------------------------------------------------------")





# Task 9 : Print numbers in reverse order from 10 to 1 using for loop
for i in range(10, 0, -1):
    print(i, end=" ")

# Output: 10, 9, 8, 7, 6, 5, 4, 3, 2, 1
print("\n------------------------------------------------------------------------------------------")




#Task 10 : Print squares of numbers from 1 to 5 using for loop
    #Alternative
    # for i in range(1, 6):
    #     print(f"Square of {i} is {i**2}")
    #     print("Square of", i, "is", i**2)
    
for i in range(1, 6):
    print(i ** 2)
# Output: 1
#         4
#         9
#         16
#         25
print("------------------------------------------------------------------------------------------")
