# AUGUSTHON -#30DaysOfPython: Day 13 - List Comprehension in Python
# Author: Ayesha Noreen
# Date: 13/08/2024

# 📘 Day 13

## List Comprehension

# List comprehension is a compact way of creating a list from a sequence.
# Syntax: [i for i in iterable if expression]

# Example 1: Changing a string to a list of characters
language = 'Python'
lst = list(language)  # Changing the string to a list
print(type(lst))      # <class 'list'>  # Output: list
print(lst)            # ['P', 'y', 't', 'h', 'o', 'n']  # Output: ['P', 'y', 't', 'h', 'o', 'n']

# Second way: Using list comprehension
lst = [i for i in language]
print(type(lst))      # <class 'list'>  # Output: list
print(lst)            # ['P', 'y', 't', 'h', 'o', 'n']  # Output: ['P', 'y', 't', 'h', 'o', 'n']

# Example 2: Generating a list of numbers
numbers = [i for i in range(11)]  # Generate numbers from 0 to 10
print(numbers)                    # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]  # Output: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Mathematical operations during iteration
squares = [i * i for i in range(11)]
print(squares)                    # [0, 1, 4, 9, 16, 25, 36, 49, 64, 81, 100]  # Output: [0, 1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

# List of tuples
numbers = [(i, i * i) for i in range(11)]
print(numbers)                    # [(0, 0), (1, 1), (2, 4), (3, 9), (4, 16), (5, 25)]  # Output: [(0, 0), (1, 1), (2, 4), (3, 9), (4, 16), (5, 25)]

# Example 3: Generating even numbers
even_numbers = [i for i in range(21) if i % 2 == 0]  # Generate even numbers in range 0 to 21
print(even_numbers)                    # [0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20]  # Output: [0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20]

# Generating odd numbers
odd_numbers = [i for i in range(21) if i % 2 != 0]  # Generate odd numbers in range 0 to 21
print(odd_numbers)                      # [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]  # Output: [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]

# Filter positive even numbers from a list
numbers = [-8, -7, -3, -1, 0, 1, 3, 4, 5, 7, 6, 8, 10]
positive_even_numbers = [i for i in numbers if i > 0]
print(positive_even_numbers)                    # [4, 6, 8, 10]  # Output: [4, 6, 8, 10]

# Flattening a three-dimensional array
list_of_lists = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
flattened_list = [number for row in list_of_lists for number in row]
print(flattened_list)    # [1, 2, 3, 4, 5, 6, 7, 8, 9]  # Output: [1, 2, 3, 4, 5, 6, 7, 8, 9]

## Lambda Function

# Lambda function is a small anonymous function.
# Syntax: x = lambda param1, param2: param1 + param2

# Example of a named function
def add_two_nums(a, b):
    return a + b

print(add_two_nums(2, 3))     # 5  # Output: 5

# Changing the above function to a lambda function
add_two_nums = lambda a, b: a + b
print(add_two_nums(2, 3))    # 5  # Output: 5

# Self-invoking lambda function
print((lambda a, b: a + b)(2, 3))  # 5  # Output: 5

# Lambda functions for square and cube
square = lambda x: x ** 2
print(square(3))    # 9  # Output: 9
cube = lambda x: x ** 3
print(cube(3))    # 27  # Output: 27

# Multiple variables in lambda
multiple_variable = lambda a, b, c: a ** 2 - 3 * b + 4 * c
print(multiple_variable(5, 5, 3)) # 22  # Output: 22

# Lambda function inside another function
def power(x):
    return lambda n: x ** n

cube = power(2)(3)   # 2 raised to the power of 3
print(cube)          # 8  # Output: 8
two_power_of_five = power(2)(5) 
print(two_power_of_five)  # 32  # Output: 32

# 🌕 Keep up the good work! You are making great progress!
print('''
 #Created by: Ayesha Noreen |Follow us on www.linkedin.com/in/khatoonintech | We love #AUGUSTHON 💕
      ''')