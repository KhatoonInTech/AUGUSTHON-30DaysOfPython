# AUGUSTHON -#30DaysOfPython: Day 7 - Sets in Python

# Creating a Set
# Creating an empty set
st = set()  # st is now an empty set: set()

# Creating a set with initial items
st = {'item1', 'item2', 'item3', 'item4'}  # st = {'item1', 'item2', 'item3', 'item4'}

# Example of creating a set of fruits
fruits = {'banana', 'orange', 'mango', 'lemon'}  # fruits = {'banana', 'orange', 'mango', 'lemon'}

# Getting Set's Length
# Finding the length of a set
len_fruits = len(fruits)  # len_fruits = 4

# Accessing Items in a Set
# Accessing items is done through loops (not shown here)

# Checking an Item
# Check if an item exists in the set
contains_item3 = 'item3' in st  # contains_item3 = True
print("Does set st contain item3? ", contains_item3)  # Output: Does set st contain item3? True

# Example check
mango_exists = 'mango' in fruits  # mango_exists = True
print('mango' in fruits)  # Output: True

# Adding Items to a Set
# Add one item using add()
st.add('item5')  # st = {'item1', 'item2', 'item3', 'item4', 'item5'}

# Example of adding to fruits
fruits.add('lime')  # fruits = {'banana', 'orange', 'mango', 'lemon', 'lime'}

# Add multiple items using update()
st.update(['item6', 'item7'])  # st = {'item1', 'item2', 'item3', 'item4', 'item5', 'item6', 'item7'}

# Example of updating fruits with vegetables
vegetables = ('tomato', 'potato', 'cabbage', 'onion', 'carrot')
fruits.update(vegetables)  # fruits now contains vegetables

# Removing Items from a Set
# Remove an item using remove()
st.remove('item2')  # st = {'item1', 'item3', 'item4', 'item5', 'item6', 'item7'}

# Example of popping a random item
removed_item = fruits.pop()  # removed_item is a random item from fruits

# Clearing Items in a Set
st.clear()  # st is now an empty set: set()
print(fruits)  # Output: set() after clearing

# Deleting a Set
del st  # st is deleted

# Converting List to Set
lst = ['item1', 'item2', 'item3', 'item4', 'item1']
st_from_list = set(lst)  # st_from_list = {'item2', 'item4', 'item1', 'item3'}

# Example of converting fruits list to set
fruits_list = ['banana', 'orange', 'mango', 'lemon', 'orange', 'banana']
fruits_set = set(fruits_list)  # fruits_set = {'mango', 'lemon', 'banana', 'orange'}

# Joining Sets
st1 = {'item1', 'item2', 'item3', 'item4'}
st2 = {'item5', 'item6', 'item7', 'item8'}
st3 = st1.union(st2)  # st3 = {'item1', 'item2', 'item3', 'item4', 'item5', 'item6', 'item7', 'item8'}

# Example of union of fruits and vegetables
combined = fruits.union(vegetables)  # combined = {'banana', 'orange', 'mango', 'lemon', 'lime', 'tomato', 'potato', 'cabbage', 'onion', 'carrot'}

# Finding Intersection Items
intersection_items = st1.intersection(st2)  # intersection_items = set()

# Example of intersection
whole_numbers = {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
even_numbers = {0, 2, 4, 6, 8, 10}
common_even = whole_numbers.intersection(even_numbers)  # common_even = {0, 2, 4, 6, 8, 10}

# Checking Subset and Super Set
is_subset = st2.issubset(st1)  # is_subset = False
is_superset = st1.issuperset(st2)  # is_superset = True

# Checking the Difference Between Two Sets
difference_st1_st2 = st1.difference(st2)  # difference_st1_st2 = {'item1', 'item4'}

# Finding Symmetric Difference Between Two Sets
symmetric_difference = st1.symmetric_difference(st2)  # symmetric_difference = {'item1', 'item4', 'item5', 'item6', 'item7', 'item8'}

# Joining Sets (Disjoint Check)
are_disjoint = st1.isdisjoint(st2)  # are_disjoint = False

print('''
 #Created by: Ayesha Noreen |Follow us on www.linkedin.com/in/khatoonintech | We love #AUGUSTHON 💕
      ''')