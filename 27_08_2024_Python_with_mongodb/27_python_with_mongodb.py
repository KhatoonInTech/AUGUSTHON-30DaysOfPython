# Import necessary modules
from flask import Flask, render_template
import os
import pymongo
from bson.objectid import ObjectId

# Set the MongoDB connection URI
MONGODB_URI = 'mongodb+srv://ayesha:your_password_goes_here@30daysofpython-twxkr.mongodb.net/test?retryWrites=true&w=majority'

# Connect to MongoDB
client = pymongo.MongoClient(MONGODB_URI)

# Print the list of databases
print(client.list_database_names())
# Output: ['admin', 'local']

# Create a database and collection
db = client['thirty_days_of_python']
db.students.insert_one({'name': 'Ayesha', 'country': 'Pakistan', 'city': 'Multan', 'age': 250})
print(client.list_database_names())
# Output: ['thirty_days_of_python', 'admin', 'local']

# Insert multiple documents
students = [
    {'name':'David','country':'UK','city':'London','age':34},
    {'name':'John','country':'Sweden','city':'Stockholm','age':28},
    {'name':'Sami','country':'Pakistan','city':'Multan','age':25},
]
for student in students:
    db.students.insert_one(student)

# Find a document
student = db.students.find_one()
print(student)
# Output: {'_id': ObjectId('5df68a21f106fe2d315bbc8b'), 'name': 'Ayesha', 'country': 'Pakistan', 'city': 'Multan', 'age': 250}

# Find a document by ID
student = db.students.find_one({'_id':ObjectId('5df68a23f106fe2d315bbc8c')})
print(student)
# Output: {'_id': ObjectId('5df68a23f106fe2d315bbc8c'), 'name': 'David', 'country': 'UK', 'city': 'London', 'age': 34}

# Find all documents
students = db.students.find()
for student in students:
    print(student)
# Output: All documents in the collection

# Find documents with specific fields
students = db.students.find({}, {"_id":0, "name": 1, "country":1})
for student in students:
    print(student)
# Output: {'name': 'Ayesha', 'country': 'Pakistan'}, {'name': 'David', 'country': 'UK'}, ...

# Find with query
query = {"country":"Pakistan"}
students = db.students.find(query)
for student in students:
    print(student)
# Output: Documents where country is 'Pakistan'

# Find with query modifiers
query = {"age":{"$gt":30}}
students = db.students.find(query)
for student in students:
    print(student)
# Output: Documents where age is greater than 30

# Limit documents
db.students.find().limit(3)

# Sort documents
students = db.students.find().sort('name')
for student in students:
    print(student)
# Output: Documents sorted by name in ascending order

# Update a document
query = {'age':250}
new_value = {'$set':{'age':38}}
db.students.update_one(query, new_value)
for student in db.students.find():
    print(student)
# Output: Documents with Ayesha's age updated to 38

# Delete a document
query = {'name':'John'}
db.students.delete_one(query)
for student in db.students.find():
    print(student)
# Output: Documents with John removed

# Drop a collection
db.students.drop()

print('''
#Created by: Ayesha Noreen |Follow us on www.linkedin.com/in/khatoonintech | We love #AUGUSTHON 💕
    ''')
