# File Handling in Python

# Opening a file for reading
f = open('./files/reading_file_example.txt')  # Opens the file in read mode
print(f)  # Output: <_io.TextIOWrapper name='./files/reading_file_example.txt' mode='r' encoding='UTF-8'>

# Reading the entire content of the file
txt = f.read()  # Reads the entire file content
print(type(txt))  # Output: <class 'str'>
print(txt)  # Output: This is an example to show how to open a file and read.\nThis is the second line of the text.
f.close()  # Closes the file

# Reading the first 10 characters of the file
f = open('./files/reading_file_example.txt')
txt = f.read(10)  # Reads the first 10 characters
print(type(txt))  # Output: <class 'str'>
print(txt)  # Output: This is an
f.close()

# Reading the first line of the file
f = open('./files/reading_file_example.txt')
line = f.readline()  # Reads the first line
print(type(line))  # Output: <class 'str'>
print(line)  # Output: This is an example to show how to open a file and read.
f.close()

# Reading all lines of the file into a list
f = open('./files/reading_file_example.txt')
lines = f.readlines()  # Reads all lines into a list
print(type(lines))  # Output: <class 'list'>
print(lines)  # Output: ['This is an example to show how to open a file and read.\n', 'This is the second line of the text.']
f.close()

# Using splitlines to read lines
f = open('./files/reading_file_example.txt')
lines = f.read().splitlines()  # Reads the file and splits into lines
print(type(lines))  # Output: <class 'list'>
print(lines)  # Output: ['This is an example to show how to open a file and read.', 'This is the second line of the text.']
f.close()

# Using 'with' statement to open a file (automatically closes the file)
with open('./files/reading_file_example.txt') as f:
    lines = f.read().splitlines()  # Reads the file and splits into lines
    print(type(lines))  # Output: <class 'list'>
    print(lines)  # Output: ['This is an example to show how to open a file and read.', 'This is the second line of the text.']

# Appending text to a file
with open('./files/reading_file_example.txt', 'a') as f:
    f.write('This text has to be appended at the end')  # Appends text to the file

# Writing to a new file
with open('./files/writing_file_example.txt', 'w') as f:
    f.write('This text will be written in a newly created file')  # Creates and writes to a new file

# Deleting a file
import os
os.remove('./files/example.txt')  # Deletes the specified file

# Check if file exists before deleting
if os.path.exists('./files/example.txt'):
    os.remove('./files/example.txt')  # Deletes the file if it exists
else:
    print('The file does not exist')  # Output if file does not exist

# JSON handling example
import json

# Changing JSON to dictionary
person_json = '''{
    "name": "Ayesha",
    "country": "Pakistan",
    "city": "Multan",
    "skills": ["JavaScrip", "React", "Python"]
}'''
person_dct = json.loads(person_json)  # Converts JSON string to dictionary
print(type(person_dct))  # Output: <class 'dict'>
print(person_dct)  # Output: {'name': 'Ayesha', 'country': 'Pakistan', 'city': 'Multan', 'skills': ['JavaScrip', 'React', 'Python']}
print(person_dct['name'])  # Output: Ayesha

# Changing dictionary to JSON
person = {
    "name": "Ayesha",
    "country": "Pakistan",
    "city": "Multan",
    "skills": ["JavaScrip", "React", "Python"]
}
person_json = json.dumps(person, indent=4)  # Converts dictionary to JSON string with indentation
print(type(person_json))  # Output: <class 'str'>
print(person_json)  # Output: JSON formatted string

# Saving data as a JSON file
with open('./files/json_example.json', 'w', encoding='utf-8') as f:
    json.dump(person, f, ensure_ascii=False, indent=4)  # Saves dictionary as JSON file with encoding

# Reading a CSV file
import csv
with open('./files/csv_example.csv') as f:
    csv_reader = csv.reader(f, delimiter=',')  # Creates a CSV reader
    line_count = 0
    for row in csv_reader:
        if line_count == 0:
            print(f'Column names are :{", ".join(row)}')  # Output: Column names
            line_count += 1
        else:
            print(f'\t{row[0]} is a teacher. He lives in {row[1]}, {row[2]}.')  # Output: Teacher details
            line_count += 1
    print(f'Number of lines:  {line_count}')  # Output: Total number of lines

# Reading an Excel file (requires xlrd package)
'''
 before running following code ,make sure to run this in bash terminal
```bash
pip install xlrd
```
'''
import xlrd
excel_book = xlrd.open_workbook('sample.xls')  # Opens Excel file
print(excel_book.nsheets)  # Output: Number of sheets in the workbook
print(excel_book.sheet_names)  # Output: Names of the sheets

# Reading an XML file
import xml.etree.ElementTree as ET
tree = ET.parse('./files/xml_example.xml')  # Parses XML file
root = tree.getroot()  # Gets the root element
print('Root tag:', root.tag)  # Output: Root tag
print('Attribute:', root.attrib)  # Output: Attributes of the root
for child in root:
    print('field: ', child.tag)  # Output: Tags of child elements

    print('''
 #Created by: Ayesha Noreen |Follow us on www.linkedin.com/in/khatoonintech | We love #AUGUSTHON 💕
      ''')