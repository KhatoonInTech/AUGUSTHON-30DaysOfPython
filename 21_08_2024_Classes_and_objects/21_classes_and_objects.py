# Creating a Class
class Person:
    pass

print(Person)  # Output: <class '__main__.Person'>

# Creating an Object
p = Person()
print(p)  # Output: <__main__.Person object at 0x10804e510>

# Class Constructor
class Person:
    def __init__(self, name):
        self.name = name

p = Person('Ayesha')
print(p.name)  # Output: Ayesha
print(p)  # Output: <__main__.Person object at 0x2abf46907e80>

# Adding more parameters to the constructor function
class Person:
    def __init__(self, firstname, lastname, age, country, city):
        self.firstname = firstname
        self.lastname = lastname
        self.age = age
        self.country = country
        self.city = city

p = Person('Ayesha', 'Noreen', 250, 'Pakistan', 'Multan')
print(p.firstname)  # Output: Ayesha
print(p.lastname)  # Output: Noreen
print(p.age)  # Output: 250
print(p.country)  # Output: Pakistan
print(p.city)  # Output: Multan

# Object Methods
class Person:
    def __init__(self, firstname, lastname, age, country, city):
        self.firstname = firstname
        self.lastname = lastname
        self.age = age
        self.country = country
        self.city = city

    def person_info(self):
        return f'{self.firstname} {self.lastname} is {self.age} years old. She lives in {self.city}, {self.country}'

p = Person('Ayesha', 'Noreen', 250, 'Pakistan', 'Multan')
print(p.person_info())  # Output: Ayesha Noreen is 250 years old. She lives in Multan, Pakistan

# Object Default Methods
class Person:
    def __init__(self, firstname='Ayesha', lastname='Noreen', age=250, country='Pakistan', city='Multan'):
        self.firstname = firstname
        self.lastname = lastname
        self.age = age
        self.country = country
        self.city = city

    def person_info(self):
        return f'{self.firstname} {self.lastname} is {self.age} years old. She lives in {self.city}, {self.country}.'

p1 = Person()
print(p1.person_info())  # Output: Ayesha Noreen is 250 years old. She lives in Multan, Pakistan.

p2 = Person('John', 'Doe', 30, 'Nomanland', 'Noman city')
print(p2.person_info())  # Output: John Doe is 30 years old. She lives in Noman city, Nomanland.

# Method to Modify Class Default Values
class Person:
    def __init__(self, firstname='Ayesha', lastname='Noreen', age=250, country='Pakistan', city='Multan'):
        self.firstname = firstname
        self.lastname = lastname
        self.age = age
        self.country = country
        self.city = city
        self.skills = []

    def person_info(self):
        return f'{self.firstname} {self.lastname} is {self.age} years old. She lives in {self.city}, {self.country}.'

    def add_skill(self, skill):
        self.skills.append(skill)

p1 = Person()
print(p1.person_info())  # Output: Ayesha Noreen is 250 years old. She lives in Multan, Pakistan.

p1.add_skill('HTML')
p1.add_skill('CSS')
p1.add_skill('JavaScript')

p2 = Person('John', 'Doe', 30, 'Nomanland', 'Noman city')
print(p2.person_info())  # Output: John Doe is 30 years old. She lives in Noman city, Nomanland.

print(p1.skills)  # Output: ['HTML', 'CSS', 'JavaScript']
print(p2.skills)  # Output: []

# Inheritance
class Student(Person):
    pass

s1 = Student('Eyob', 'Noreen', 30, 'Pakistan', 'Multan')
s2 = Student('Lidiya', 'Teklemariam', 28, 'Pakistan', 'Espoo')

print(s1.person_info())  # Output: Eyob Noreen is 30 years old. She lives in Multan, Pakistan.

s1.add_skill('JavaScript')
s1.add_skill('React')
s1.add_skill('Python')
print(s1.skills)  # Output: ['JavaScript', 'React', 'Python']

print(s2.person_info())  # Output: Lidiya Teklemariam is 28 years old. She lives in Sahiwal, Pakistan.

s2.add_skill('Organizing')
s2.add_skill('Marketing')
s2.add_skill('Digital Marketing')
print(s2.skills)  # Output: ['Organizing', 'Marketing', 'Digital Marketing']

# Overriding parent method
class Student(Person):
    def __init__(self, firstname='Ayesha', lastname='Noreen', age=250, country='Pakistan', city='Multan', gender='female'):
        self.gender = gender
        super().__init__(firstname, lastname, age, country, city)

    def person_info(self):
        gender = 'He' if self.gender == 'male' else 'She'
        return f'{self.firstname} {self.lastname} is {self.age} years old. {gender} lives in {self.city}, {self.country}.'

s1 = Student('Eyob', 'Noreen', 30, 'Pakistan', 'Multan', 'male')
s2 = Student('Lidiya', 'Teklemariam', 28, 'Pakistan', 'Sahiwal', 'female')

print(s1.person_info())  # Output: Eyob Noreen is 30 years old. He lives in Multan, Pakistan.

s1.add_skill('JavaScript')
s1.add_skill('React')
s1.add_skill('Python')
print(s1.skills)  # Output: ['JavaScript', 'React', 'Python']

print(s2.person_info())  # Output: Lidiya Teklemariam is 28 years old. She lives in Sahiwal, Pakistan.

s2.add_skill('Organizing')
s2.add_skill('Marketing')
s2.add_skill('Digital Marketing')
print(s2.skills)  # Output: ['Organizing', 'Marketing', 'Digital Marketing']



print('''
 #Created by: Ayesha Noreen |Follow us on www.linkedin.com/in/khatoonintech | We love #AUGUSTHON 💕
      ''')
