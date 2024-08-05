# AUGUSTHON - Day 6 - Tuples in Python

# Creating an empty tuple
empty_tuple = ()  # An empty tuple
# or using the tuple constructor
empty_tuple = tuple()  # An empty tuple

# Creating a tuple with initial values
tpl = ('item1', 'item2', 'item3')  # Tuple with items
fruits = ('banana', 'orange', 'mango', 'lemon')  # Tuple of fruits

# Tuple length
tpl = ('item1', 'item2', 'item3')
length_of_tpl = len(tpl)  # Length of the tuple
# Expected Output: 3

# Accessing Tuple Items
tpl = ('item1', 'item2', 'item3')
first_item = tpl[0]  # Accessing the first item
second_item = tpl[1]  # Accessing the second item

fruits = ('banana', 'orange', 'mango', 'lemon')
first_fruit = fruits[0]  # 'banana'
second_fruit = fruits[1]  # 'orange'
last_index = len(fruits) - 1
last_fruit = fruits[last_index]  # 'lemon'

# Negative indexing
tpl = ('item1', 'item2', 'item3', 'item4')
first_item_neg = tpl[-4]  # 'item1'
second_item_neg = tpl[-3]  # 'item2'

fruits = ('banana', 'orange', 'mango', 'lemon')
first_fruit_neg = fruits[-4]  # 'banana'
second_fruit_neg = fruits[-3]  # 'orange'
last_fruit_neg = fruits[-1]  # 'lemon'

# Slicing tuples
tpl = ('item1', 'item2', 'item3', 'item4')
all_items = tpl[0:4]  # All items
middle_two_items = tpl[1:3]  # ('item2', 'item3')

fruits = ('banana', 'orange', 'mango', 'lemon')
all_fruits = fruits[0:4]  # All fruits
orange_mango = fruits[1:3]  # ('orange', 'mango')

# Changing Tuples to Lists
tpl = ('item1', 'item2', 'item3', 'item4')
lst = list(tpl)  # Convert tuple to list

fruits = ('banana', 'orange', 'mango', 'lemon')
fruits = list(fruits)  # Convert to list
fruits[0] = 'apple'  # Modify the first item
# Expected Output: ['apple', 'orange', 'mango', 'lemon']
fruits = tuple(fruits)  # Convert back to tuple
# Expected Output: ('apple', 'orange', 'mango', 'lemon')

# Checking an Item in a Tuple
tpl = ('item1', 'item2', 'item3', 'item4')
item_check = 'item2' in tpl  # True

fruits = ('banana', 'orange', 'mango', 'lemon')
orange_check = 'orange' in fruits  # True
apple_check = 'apple' in fruits  # False

# Joining Tuples
tpl1 = ('item1', 'item2', 'item3')
tpl2 = ('item4', 'item5', 'item6')
tpl3 = tpl1 + tpl2  # Joining two tuples
# Expected Output: ('item1', 'item2', 'item3', 'item4', 'item5', 'item6')

fruits = ('banana', 'orange', 'mango', 'lemon')
vegetables = ('Tomato', 'Potato', 'Cabbage', 'Onion', 'Carrot')
fruits_and_vegetables = fruits + vegetables  # Joining fruits and vegetables
# Expected Output: ('banana', 'orange', 'mango', 'lemon', 'Tomato', 'Potato', 'Cabbage', 'Onion', 'Carrot')

# Deleting Tuples
tpl1 = ('item1', 'item2', 'item3')
del tpl1  # Deleting the tuple

fruits = ('banana', 'orange', 'mango', 'lemon')
del fruits  # Deleting the fruits tuple

print('''
 #Created by: Ayesha Noreen |Follow us on www.linkedin.com/in/khatoonintech | We love #AUGUSTHON 💕
      ''')