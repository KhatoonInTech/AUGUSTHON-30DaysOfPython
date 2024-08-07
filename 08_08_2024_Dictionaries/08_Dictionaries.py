# AUGUSTHON - Day 8: Dictionaries in Python

# Creating an empty dictionary
empty_dict = {}  # {}
# Creating a dictionary with data values
dct = {'key1': 'value1', 'key2': 'value2', 'key3': 'value3', 'key4': 'value4'}  # {'key1': 'value1', 'key2': 'value2', 'key3': 'value3', 'key4': 'value4'}

# Example of a complex dictionary
person = {
    'first_name': 'Ayesha',
    'last_name': 'Noreen',
    'age': 10,
    'country': 'Pakistan',
    'is_married': True,
    'skills': ['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
    'address': {
        'street': 'Space street',
        'zipcode': '66666'
    }
}

# Dictionary Length
print(len(person))  # 7

# Accessing Dictionary Items
print(person['first_name'])  # Ayesha
print(person['country'])      # Pakistan
print(person['skills'])       # ['JavaScript', 'React', 'Node', 'MongoDB', 'Python']
print(person['skills'][0])    # JavaScript
print(person['address']['street'])  # Space street
print(person.get('city'))     # None (no error, returns None)

# Adding Items to a Dictionary
person['job_title'] = 'Instructor'  # Adding a new key-value pair
person['skills'].append('Python')    # Adding to the skills list
print(person)  # Updated dictionary with job_title and Python in skills

# Modifying Items in a Dictionary
person['first_name'] = 'Eyob'  # Changing first_name
person['age'] = 252  # Changing age

# Checking Keys in a Dictionary
print('key2' in dct)  # True
print('key5' in dct)  # False

# Removing Key and Value Pairs from a Dictionary
person.pop('first_name')  # Removes the first_name item
person.popitem()          # Removes the last item (address)
del person['is_married']  # Removes the is_married item

# Changing Dictionary to a List of Items
print(person.items())  # dict_items([...]) (list of tuples of key-value pairs)

# Clearing a Dictionary
dct.clear()  # Clears all items in dct
print(dct)    # {}

# Deleting a Dictionary
del person  # Deletes the entire person dictionary

# Copy a Dictionary
dct = {'key1': 'value1', 'key2': 'value2', 'key3': 'value3', 'key4': 'value4'}
dct_copy = dct.copy()  # Creates a copy of dct
print(dct_copy)  # {'key1': 'value1', 'key2': 'value2', 'key3': 'value3', 'key4': 'value4'}

# Getting Dictionary Keys as a List
keys = dct.keys()
print(keys)  # dict_keys(['key1', 'key2', 'key3', 'key4'])

# Getting Dictionary Values as a List
values = dct.values()
print(values)  # dict_values(['value1', 'value2', 'value3', 'value4'])


print('''
 #Created by: Ayesha Noreen |Follow us on www.linkedin.com/in/khatoonintech | We love #AUGUSTHON 💕
      ''')