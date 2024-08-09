# AUGUSTHON - Day 10 - Loops in Python

# While Loop Example
count = 0
while count < 5:
    print(count)  # prints 0, 1, 2, 3, 4
    count = count + 1

# Using else with While Loop
count = 0
while count < 5:
    print(count)  # prints 0, 1, 2, 3, 4
    count = count + 1
else:
    print(count)  # prints 5

# Break Example in While Loop
count = 0
while count < 5:
    print(count)  # prints 0, 1, 2
    count = count + 1
    if count == 3:
        break  # exits loop when count is 3

# Continue Example in While Loop
count = 0
while count < 5:
    if count == 3:
        count = count + 1
        continue  # skips 3
    print(count)  # prints 0, 1, 2, 4
    count = count + 1

# For Loop with List
numbers = [0, 1, 2, 3, 4, 5]
for number in numbers:
    print(number)  # prints 0, 1, 2, 3, 4, 5

# For Loop with String
language = 'Python'
for letter in language:
    print(letter)  # prints P, y, t, h, o, n

# For Loop with Tuple
numbers = (0, 1, 2, 3, 4, 5)
for number in numbers:
    print(number)  # prints 0, 1, 2, 3, 4, 5

# For Loop with Dictionary
person = {
    'first_name': 'Ayesha',
    'last_name': 'Noreen',
    'age': 10,
    'country': 'Pakistan',
    'is_single': True,
    'skills': ['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
    'address': {
        'street': 'Space street',
        'zipcode': '66666'
    }
}
for key in person:
    print(key)  # prints keys of the dictionary
for key, value in person.items():
    print(key, value)  # prints key-value pairs

# For Loop with Set
it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}
for company in it_companies:
    print(company)  # prints each company in the set

# Break Example in For Loop
numbers = (0, 1, 2, 3, 4, 5)
for number in numbers:
    print(number)  # prints 0, 1, 2, 3, 4, 5
    if number == 3:
        break  # exits loop when number is 3

# Continue Example in For Loop
numbers = (0, 1, 2, 3, 4, 5)
for number in numbers:
    print(number)  # prints 0, 1, 2, 3, 4, 5
    if number == 3:
        continue  # skips the next print statement for number 3
    print('Next number should be ', number + 1)  # prints next number for others
print('outside the loop')  # final print statement outside the loop

# The Range Function
lst = list(range(11)) 
print(lst)  # prints [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
st = set(range(1, 11))    
print(st)  # prints {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
lst = list(range(0, 11, 2))
print(lst)  # prints [0, 2, 4, 6, 8, 10]
st = set(range(0, 11, 2))
print(st)  # prints {0, 2, 4, 6, 8, 10}

# Nested For Loop Example
for key in person:
    if key == 'skills':
        for skill in person['skills']:
            print(skill)  # prints each skill in the skills list

# For Else Example
for number in range(11):
    print(number)  # prints 0 to 10
else:
    print('The loop stops at', number)  # prints 'The loop stops at 10'

# Pass Example
for number in range(6):
    pass  # does nothing, serves as a placeholder
