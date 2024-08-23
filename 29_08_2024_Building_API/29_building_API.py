# Importing necessary libraries
from flask import Flask, Response, request
import json
from bson.objectid import ObjectId
from bson.json_util import dumps
import pymongo
from datetime import datetime
import os

# Initializing the Flask application
app = Flask(__name__)

# MongoDB connection URI
MONGODB_URI = 'mongodb+srv://Ayesha:your_password@30daysofpython-twxkr.mongodb.net/test?retryWrites=true&w=majority'
client = pymongo.MongoClient(MONGODB_URI)
db = client['thirty_days_of_python']  # Accessing the database

# Endpoint to retrieve all students
@app.route('/api/v1.0/students', methods=['GET'])
def students():
    # Fetching student data from the database
    student_list = list(db.students.find())
    return Response(dumps(student_list), mimetype='application/json')

# Endpoint to retrieve a single student by ID
@app.route('/api/v1.0/students/<id>', methods=['GET'])
def single_student(id):
    # Fetching a single student document using the provided ID
    student = db.students.find_one({'_id': ObjectId(id)})
    return Response(dumps(student), mimetype='application/json')

# Endpoint to create a new student
@app.route('/api/v1.0/students', methods=['POST'])
def create_student():
    # Extracting student data from the request
    name = request.form['name']
    country = request.form['country']
    city = request.form['city']
    skills = request.form['skills'].split(', ')
    bio = request.form['bio']
    birthyear = request.form['birthyear']
    created_at = datetime.now()

    # Creating a student dictionary
    student = {
        'name': name,
        'country': country,
        'city': city,
        'birthyear': birthyear,
        'skills': skills,
        'bio': bio,
        'created_at': created_at
    }
    
    # Inserting the new student into the database
    db.students.insert_one(student)
    return Response(dumps({"result": "Student created successfully"}), mimetype='application/json')

# Endpoint to update an existing student
@app.route('/api/v1.0/students/<id>', methods=['PUT'])
def update_student(id):
    # Query to find the student by ID
    query = {"_id": ObjectId(id)}
    
    # Extracting updated data from the request
    name = request.form['name']
    country = request.form['country']
    city = request.form['city']
    skills = request.form['skills'].split(', ')
    bio = request.form['bio']
    birthyear = request.form['birthyear']
    created_at = datetime.now()

    # Creating an updated student dictionary
    student = {
        'name': name,
        'country': country,
        'city': city,
        'birthyear': birthyear,
        'skills': skills,
        'bio': bio,
        'created_at': created_at
    }
    
    # Updating the student in the database
    db.students.update_one(query, {"$set": student})
    return Response(dumps({"result": "Student updated successfully"}), mimetype='application/json')

# Endpoint to delete a student
@app.route('/api/v1.0/students/<id>', methods=['DELETE'])
def delete_student(id):
    # Deleting the student document by ID
    db.students.delete_one({"_id": ObjectId(id)})
    return Response(dumps({"result": "Student deleted successfully"}), mimetype='application/json')

# Running the Flask application
if __name__ == '__main__':
    # Setting the port for deployment
    port = int(os.environ.get("PORT", 5000))
    app.run(debug=True, host='0.0.0.0', port=port)

# Expected Outputs:
# 1. GET /api/v1.0/students -> Returns a list of all students in JSON format.
# 2. GET /api/v1.0/students/<id> -> Returns the student with the specified ID in JSON format.
# 3. POST /api/v1.0/students -> Creates a new student and returns a success message.
# 4. PUT /api/v1.0/students/<id> -> Updates the student with the specified ID and returns a success message.
# 5. DELETE /api/v1.0/students/<id> -> Deletes the student with the specified ID and returns a success message.



print('''
#Created by: Ayesha Noreen |Follow us on www.linkedin.com/in/khatoonintech | We love #AUGUSTHON 💕
    ''')
