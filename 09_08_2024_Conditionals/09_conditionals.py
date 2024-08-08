# AUGUSTHON - #30DaysOfPython: Day 9 - Conditionals in Python

# Conditionals in Python allow for decision-making in code execution.

# Example 1: Basic If Condition
a = 3
if a > 0:
    print('A is a positive number')  # Output: A is a positive number

# If Else Condition
a = 3
if a < 0:
    print('A is a negative number')
else:
    print('A is a positive number')  # Output: A is a positive number

# If Elif Else Condition
a = 0
if a > 0:
    print('A is a positive number')
elif a < 0:
    print('A is a negative number')
else:
    print('A is zero')  # Output: A is zero

# Short Hand If Condition
a = 3
print('A is positive') if a > 0 else print('A is negative')  # Output: A is positive

# Nested Conditions
a = 0
if a > 0:
    if a % 2 == 0:
        print('A is a positive and even integer')
    else:
        print('A is a positive number')
elif a == 0:
    print('A is zero')  # Output: A is zero
else:
    print('A is a negative number')

# If Condition with Logical Operators (AND)
a = 0
if a > 0 and a % 2 == 0:
    print('A is an even and positive integer')
elif a > 0 and a % 2 != 0:
    print('A is a positive integer')
elif a == 0:
    print('A is zero')  # Output: A is zero
else:
    print('A is negative')

# If Condition with Logical Operators (OR)
user = 'Javed'
access_level = 1
if user == 'admin' or access_level >= 4:
    print('Access granted!')  # Output: Access denied!
else:
    print('Access denied!')  # Output: Access denied!


print('''
 #Created by: Ayesha Noreen |Follow us on www.linkedin.com/in/khatoonintech | We love #AUGUSTHON 💕
      ''')