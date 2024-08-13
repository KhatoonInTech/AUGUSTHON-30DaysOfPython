# AUGUSTHON - 30DaysOfPython: Day 14 - Higher Order Functions in Python

# Higher Order Functions allow functions to be passed as parameters and returned as values.

# Function as a Parameter
def sum_numbers(nums):  # normal function
    return sum(nums)    # a sad function abusing the built-in sum function :<

def higher_order_function(f, lst):  # function as a parameter
    summation = f(lst)
    return summation

result = higher_order_function(sum_numbers, [1, 2, 3, 4, 5])
print(result)       # 15  # Output: 15

# Function as a Return Value
def square(x):          # a square function
    return x ** 2

def cube(x):            # a cube function
    return x ** 3

def absolute(x):        # an absolute value function
    if x >= 0:
        return x
    else:
        return -(x)

def higher_order_function(type): # a higher order function returning a function
    if type == 'square':
        return square
    elif type == 'cube':
        return cube
    elif type == 'absolute':
        return absolute

result = higher_order_function('square')
print(result(3))       # 9  # Output: 9
result = higher_order_function('cube')
print(result(3))       # 27 # Output: 27
result = higher_order_function('absolute')
print(result(-3))      # 3  # Output: 3

# Python Closures
def add_ten():
    ten = 10
    def add(num):
        return num + ten
    return add

closure_result = add_ten()
print(closure_result(5))  # 15  # Output: 15
print(closure_result(10))  # 20  # Output: 20

# Python Decorators
def greeting():
    return 'Welcome to Python'

# Decorator function
def uppercase_decorator(function):
    def wrapper():
        func = function()
        make_uppercase = func.upper()
        return make_uppercase
    return wrapper

g = uppercase_decorator(greeting)
print(g())          # WELCOME TO PYTHON  # Output: WELCOME TO PYTHON

# Using the decorator with the @ syntax
@uppercase_decorator
def greeting():
    return 'Welcome to Python'
print(greeting())   # WELCOME TO PYTHON  # Output: WELCOME TO PYTHON

# Applying Multiple Decorators to a Single Function
def split_string_decorator(function):
    def wrapper():
        func = function()
        splitted_string = func.split()
        return splitted_string
    return wrapper

@split_string_decorator
@uppercase_decorator
def greeting():
    return 'Welcome to Python'
print(greeting())   # WELCOME TO PYTHON  # Output: WELCOME TO PYTHON

# Accepting Parameters in Decorator Functions
def decorator_with_parameters(function):
    def wrapper_accepting_parameters(para1, para2, para3):
        function(para1, para2, para3)
        print("I live in {}".format(para3))
    return wrapper_accepting_parameters

@decorator_with_parameters
def print_full_name(first_name, last_name, country):
    print("I am {} {}. I love to teach.".format(
        first_name, last_name, country))

print_full_name("Ayesha", "Noreen", 'Pakistan')  
# Output: I am Ayesha Noreen. I love to teach. I live in Pakistan

# Built-in Higher Order Functions
# Python - Map Function
numbers = [1, 2, 3, 4, 5]  # iterable
def square(x):
    return x ** 2

# Using map() with a normal function
numbers_squared = map(square, numbers)
print(list(numbers_squared))    # [1, 4, 9, 16, 25]  # Output: [1, 4, 9, 16, 25]

# Using map() with a lambda function
numbers_squared = map(lambda x: x ** 2, numbers)
print(list(numbers_squared))    # [1, 4, 9, 16, 25]  # Output: [1, 4, 9, 16, 25]

# Example with strings
numbers_str = ['1', '2', '3', '4', '5']  # iterable
numbers_int = map(int, numbers_str)
print(list(numbers_int))    # [1, 2, 3, 4, 5]  # Output: [1, 2, 3, 4, 5]

# Changing names to upper case
names = ['Ahsan', 'Lidiya', 'Ermias', 'Abraham']  # iterable
names_upper_cased = map(lambda name: name.upper(), names)
print(list(names_upper_cased))    # ['AHSAN', 'LIDIYA', 'ERMIAS', 'ABRAHAM']  # Output: ['AHSAN', 'LIDIYA', 'ERMIAS', 'ABRAHAM']

# Python - Filter Function
numbers = [1, 2, 3, 4, 5]  # iterable
def is_even(num):
    return num % 2 == 0

even_numbers = filter(is_even, numbers)
print(list(even_numbers))       # [2, 4]  # Output: [2, 4]

# Example for odd numbers
odd_numbers = filter(lambda num: num % 2 != 0, numbers)
print(list(odd_numbers))       # [1, 3, 5]  # Output: [1, 3, 5]

# Filter long names
names = ['Asif', 'Lidiya', 'Ermias', 'Abraham']  # iterable
long_names = filter(lambda name: len(name) >= 7, names)
print(list(long_names))         # ['Abraham']  # Output: ['Abraham']

# Python - Reduce Function
from functools import reduce  # Importing reduce from functools

numbers_str = ['1', '2', '3', '4', '5']  # iterable
def add_two_nums(x, y):
    return int(x) + int(y)

total = reduce(add_two_nums, numbers_str)
print(total)    # 15  # Output: 15