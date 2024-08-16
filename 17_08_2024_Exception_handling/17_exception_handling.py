# Exception Handling in Python

# Example 1: Basic try-except block
try:
    print(10 + '5')  # Attempting to add an integer and a string
except:
    print('Something went wrong')  # This will execute if an exception occurs
# Expected Output: Something went wrong

# Example 2: Handling specific exceptions
try:
    name = input('Enter your name:')  # User input for name
    year_born = input('Year you were born:')  # User input for year of birth
    age = 2019 - year_born  # Calculate age
    print(f'You are {name}. And your age is {age}.')  # Output the name and age
except TypeError:
    print('Type error occurred')  # Handle TypeError
except ValueError:
    print('Value error occurred')  # Handle ValueError
except ZeroDivisionError:
    print('Zero division error occurred')  # Handle ZeroDivisionError
# Expected Output: Type error occurred (if input is invalid)

# Example 3: Using else and finally
try:
    name = input('Enter your name:')  # User input for name
    year_born = input('Year you were born:')  # User input for year of birth
    age = 2019 - int(year_born)  # Calculate age
    print(f'You are {name}. And your age is {age}.')  # Output the name and age
except TypeError:
    print('Type error occurred')  # Handle TypeError
except ValueError:
    print('Value error occurred')  # Handle ValueError
except ZeroDivisionError:
    print('Zero division error occurred')  # Handle ZeroDivisionError
else:
    print('I usually run with the try block')  # Executes if no exceptions occur
finally:
    print('I always run.')  # Executes regardless of exceptions
# Expected Output: You are Ayesha. And your age is 99. (if inputs are valid)

# Example 4: Unpacking Lists
def sum_of_five_nums(a, b, c, d, e):
    return a + b + c + d + e  # Return the sum of five numbers

lst = [1, 2, 3, 4, 5]
print(sum_of_five_nums(*lst))  # Unpacking the list into function arguments
# Expected Output: 15

# Example 5: Packing Arguments
def sum_all(*args):
    s = 0
    for i in args:
        s += i  # Sum all arguments
    return s

print(sum_all(1, 2, 3))  # Pass multiple arguments
# Expected Output: 6
print(sum_all(1, 2, 3, 4, 5, 6, 7))  # Pass more arguments
# Expected Output: 28

# Example 6: Unpacking Dictionaries
def unpacking_person_info(name, country, city, age):
    return f'{name} lives in {country}, {city}. She is {age} years old.'  # Return formatted string

dct = {'name': 'Ayesha', 'country': 'Pakistan', 'city': 'Multan', 'age': 250}
print(unpacking_person_info(**dct))  # Unpacking dictionary into function arguments
# Expected Output: Ayesha lives in Pakistan, Multan. She is 250 years old.

# Example 7: Using zip to combine lists
fruits = ['banana', 'orange', 'mango', 'lemon', 'lime']
vegetables = ['Tomato', 'Potato', 'Cabbage', 'Onion', 'Carrot']
fruits_and_veges = []
for f, v in zip(fruits, vegetables):
    fruits_and_veges.append({'fruit': f, 'veg': v})  # Combine fruit and vegetable into a dictionary

print(fruits_and_veges)  # Output the combined list
# Expected Output: [{'fruit': 'banana', 'veg': 'Tomato'}, {'fruit': 'orange', 'veg': 'Potato'}, ...]


print('''
 #Created by: Ayesha Noreen |Follow us on www.linkedin.com/in/khatoonintech | We love #AUGUSTHON 💕
      ''')