# AUGUSTHON - Day 11 - Functions in Python

# Declaring a function
def function_name():
    # codes
    pass  # Placeholder for function body

# Calling a function
function_name()  # No output, just calls the function

# Function without Parameters
def generate_full_name():
    first_name = 'Ayesha'
    last_name = 'Noreen'
    space = ' '
    full_name = first_name + space + last_name
    print(full_name)

generate_full_name()  # Output: Ayesha Noreen

def add_two_numbers():
    num_one = 2
    num_two = 3
    total = num_one + num_two
    print(total)

add_two_numbers()  # Output: 5

# Function Returning a Value - Part 1
def generate_full_name():
    first_name = 'Ayesha'
    last_name = 'Noreen'
    space = ' '
    full_name = first_name + space + last_name
    return full_name

print(generate_full_name())  # Output: Ayesha Noreen

def add_two_numbers():
    num_one = 2
    num_two = 3
    total = num_one + num_two
    return total

print(add_two_numbers())  # Output: 5

# Function with Parameters
def greetings(name):
    message = name + ', welcome to AUGUSTHON!'
    return message

print(greetings('Ayesha'))  # Output: Ayesha, welcome to AUGUSTHON!

def add_ten(num):
    ten = 10
    return num + ten

print(add_ten(90))  # Output: 100

def square_number(x):
    return x * x

print(square_number(2))  # Output: 4

def area_of_circle(r):
    PI = 3.14
    area = PI * r ** 2
    return area

print(area_of_circle(10))  # Output: 314.0

def sum_of_numbers(n):
    total = 0
    for i in range(n + 1):
        total += i
    return total

print(sum_of_numbers(10))  # Output: 55
print(sum_of_numbers(100))  # Output: 5050

# Two Parameters
def generate_full_name(first_name, last_name):
    space = ' '
    full_name = first_name + space + last_name
    return full_name

print('Full Name: ', generate_full_name('Ayesha', 'Noreen'))  # Output: Full Name: Ayesha Noreen

def sum_two_numbers(num_one, num_two):
    sum = num_one + num_two
    return sum

print('Sum of two numbers: ', sum_two_numbers(1, 9))  # Output: Sum of two numbers: 10

def calculate_age(current_year, birth_year):
    age = current_year - birth_year
    return age

print('Age: ', calculate_age(2021, 1819))  # Output: Age: 202

def weight_of_object(mass, gravity):
    weight = str(mass * gravity) + ' N'  # Convert weight to string
    return weight

print('Weight of an object in Newtons: ', weight_of_object(100, 9.81))  # Output: Weight of an object in Newtons: 981 N

# Passing Arguments with Key and Value
def print_fullname(firstname, lastname):
    space = ' '
    full_name = firstname + space + lastname
    print(full_name)

print(print_fullname(firstname='Ayesha', lastname='Noreen'))  # Output: Ayesha Noreen

def add_two_numbers(num1, num2):
    total = num1 + num2
    print(total)

print(add_two_numbers(num2=3, num1=2))  # Output: 5

# Function Returning a Value - Part 2
def print_name(firstname):
    return firstname

print(print_name('Ayesha'))  # Output: Ayesha

def print_full_name(firstname, lastname):
    space = ' '
    full_name = firstname + space + lastname
    return full_name

print(print_full_name(firstname='Ayesha', lastname='Noreen'))  # Output: Ayesha Noreen

# Returning a number
def add_two_numbers(num1, num2):
    total = num1 + num2
    return total

print(add_two_numbers(2, 3))  # Output: 5

# Returning a boolean
def is_even(n):
    if n % 2 == 0:
        print('even')
        return True  # Stops further execution of the function
    return False

print(is_even(10))  # Output: True
print(is_even(7))  # Output: False

# Returning a list
def find_even_numbers(n):
    evens = []
    for i in range(n + 1):
        if i % 2 == 0:
            evens.append(i)
    return evens

print(find_even_numbers(10))  # Output: [0, 2, 4, 6, 8, 10]

# Function with Default Parameters
def greetings(name='Peter'):
    message = name + ', welcome to AUGUSTHON!'
    return message

print(greetings())  # Output: Peter, welcome to AUGUSTHON!
print(greetings('Ayesha'))  # Output: Ayesha, welcome to AUGUSTHON!

def generate_full_name(first_name='Ayesha', last_name='Noreen'):
    space = ' '
    full_name = first_name + space + last_name
    return full_name

print(generate_full_name())  # Output: Ayesha Noreen
print(generate_full_name('David', 'Smith'))  # Output: David Smith

def calculate_age(birth_year, current_year=2021):
    age = current_year - birth_year
    return age

print('Age: ', calculate_age(1821))  # Output: Age: 200

def weight_of_object(mass, gravity=9.81):
    weight = str(mass * gravity) + ' N'  # Convert weight to string
    return weight

print('Weight of an object in Newtons: ', weight_of_object(100))  # Output: Weight of an object in Newtons: 981 N
print('Weight of an object in Newtons: ', weight_of_object(100, 1.62))  # Output: Weight of an object in Newtons: 162.0 N

# Arbitrary Number of Arguments
def sum_all_nums(*nums):
    total = 0
    for num in nums:
        total += num  # same as total = total + num
    return total

print(sum_all_nums(2, 3, 5))  # Output: 10

# Default and Arbitrary Number of Parameters in Functions
def generate_groups(team, *args):
    print(team)
    for i in args:
        print(i)

print(generate_groups('Team-1', 'Ayesha', 'Burak', 'Danish'))
# Output:
# Team-1
# Ayesha
# Burak
# Danish

# Function as a Parameter of Another Function
def square_number(n):
    return n * n

def do_something(f, x):
    return f(x)

print(do_something(square_number, 3))  # Output: 9

print('''
 #Created by: Ayesha Noreen |Follow us on www.linkedin.com/in/khatoonintech | We love #AUGUSTHON 💕
      ''')