
# Variables in Python

first_name = 'Ayesha'
last_name = 'Noreen'
country = 'Pakistan'
city = 'Multan'
age = 350
is_married = False
skills = ['C', 'C++', 'ML', 'DL', 'Python']
person_info = {
    'firstname':'Ayesha', 
    'lastname':'Noreen', 
    'country':'Pakistan',
    'city':'Multan'
    }

# Printing the values stored in the variables

print('First name:', first_name)
print('First name length:', len(first_name))
print('Last name: ', last_name)
print('Last name length: ', len(last_name))
print('Country: ', country)
print('City: ', city)
print('Age: ', age)
print('Married: ', is_married)
print('Skills: ', skills)
print('Person information: ', person_info)

# Declaring multiple variables in one line

first_name, last_name, country, age, is_married = 'Ayesha', 'Noreen', 'Helsink', 350, False

print(first_name, last_name, country, age, is_married)
print('First name:', first_name)
print('Last name: ', last_name)
print('Country: ', country)
print('Age: ', age)
print('Married: ', is_married)