
# Single line comment
letter = 'A'                # A string could be a single character or a bunch of texts
print(letter)               # A
print(len(letter))          # 1 -length of the variable "letter" is 1
greeting = 'I stand by AUGUSTHON!'  # String could be  a single or double quote,"I stand by AUGUSTHON!"
print(greeting)             # I stand by AUGUSTHON!
print(len(greeting))        # 21
sentence = "I hope you are enjoying 30 days of python challenge"
print(sentence)
print('-'*50)      #printing the section breaker

# Multiline String
multiline_string = '''I am a teacher and enjoy teaching.
I didn't find anything as rewarding as empowering people.
That is why I created 30 days of python.'''
print(multiline_string)
print('-'*50)      #printing the section breaker

# Another way of doing the same thing
multiline_string = """I am a teacher and enjoy teaching.
I didn't find anything as rewarding as empowering people.
That is why I created 30 days of python."""
print(multiline_string)
print('-'*50)      #printing the section breaker

# String Concatenation
first_name = 'Ayesha'
last_name = 'Noreen'
space = ' '
full_name = first_name  +  space + last_name
print(full_name) # Ayesha Noreen
print('-'*50)      #printing the section breaker

# Checking length of a string using len() builtin function
print(len(first_name))  # 6
print(len(last_name))   # 6
print(len(first_name) > len(last_name)) # False
print(len(full_name)) # 12
print('-'*50)      #printing the section breaker

#### Unpacking characters 
language = 'Python'
a,b,c,d,e,f = language # unpacking sequence characters into variables
print(a) # P
print(b) # y
print(c) # t 
print(d) # h
print(e) # o
print(f) # n

# Accessing characters in strings by index
language = 'Python'
first_letter = language[0]
print(first_letter) # P
second_letter = language[1]
print(second_letter) # y
last_index = len(language) - 1
last_letter = language[last_index]
print(last_letter) # n
print('-'*50)      #printing the section breaker

# If we want to start from right end we can use negative indexing. -1 is the last index
language = 'Python'
last_letter = language[-1]
print(last_letter) # n
second_last = language[-2]
print(second_last) # o
print('-'*50)      #printing the section breaker

# Slicing

language = 'Python'
first_three = language[0:3] # starts at zero index and up to 3 but not include 3
last_three = language[3:6]
print(last_three) # hon
# Another way
last_three = language[-3:]
print(last_three)   # hon
last_three = language[3:]
print(last_three)   # hon
print('-'*50)      #printing the section breaker

# Skipping character while splitting Python strings
language = 'Python'
pto = language[0:6:2] # 
print(pto) # pto
print('-'*50)      #printing the section breaker

# Escape sequence
print('I hope every one enjoying the python challenge.\nDo you ?') # line break
print('Days\tTopics\tExercises')
print('Day 1\t3\t5')
print('Day 2\t3\t5')
print('Day 3\t3\t5')
print('Day 4\t3\t5')
print('This is a back slash  symbol (\\)') # To write a back slash use double backslash
print('In every programming language it starts with \"Hello, World!\"')  #to print inverted commas ,use backslash with inverted commas
print('-'*50)      #printing the section breaker

## String Methods
# capitalize(): Converts the first character the string to Capital Letter

challenge = 'thirty days of python'
print(challenge.capitalize()) # 'Thirty days of python'
print('-'*50)      #printing the section breaker

# count(): returns occurrences of substring in string, count(substring, start=.., end=..)

challenge = 'thirty days of python'
print(challenge.count('y')) # 3
print(challenge.count('y', 7, 14)) # 1
print(challenge.count('th')) # 2`
print('-'*50)      #printing the section breaker

# endswith(): Checks if a string ends with a specified ending

challenge = 'thirty days of python'
print(challenge.endswith('on'))   # True
print(challenge.endswith('tion')) # False
print('-'*50)      #printing the section breaker

# expandtabs(): Replaces tab character with spaces, default tab size is 8. It takes tab size argument

challenge = 'thirty\tdays\tof\tpython'
print(challenge.expandtabs())   # 'thirty  days    of      python'
print(challenge.expandtabs(13)) # 'thirty    days      of        python'
print('-'*50)      #printing the section breaker

# find(): Returns the index of first occurrence of substring

challenge = 'thirty days of python'
print(challenge.find('y'))  # 5
print(challenge.find('th')) # 0
print('-'*50)      #printing the section breaker

# format()	formats string into nicer output    
first_name = 'Ayesha'
last_name = 'Noreen'
job = 'LinkedIn Influencer'
country = 'Pakistan'
sentence = 'I am {} {}. I am a {}. I live in {}.'.format(first_name, last_name, job, country)
print(sentence) # I am Ayesha Noreen. I am a LinkedIn Influencer. I live in Pakistan.
print('-'*50)      #printing the section breaker

radius = 10
pi = 3.14
area = pi # radius ## 2
result = 'The area of circle with {} is {}'.format(str(radius), str(area))
print(result) # The area of circle with 10 is 314.0
print('-'*50)      #printing the section breaker

# index(): Returns the index of substring
challenge = 'thirty days of python'
print(challenge.index('y'))  # 5
print(challenge.index('th')) # 0
print('-'*50)      #printing the section breaker

# isalnum(): Checks alphanumeric character

challenge = 'ThirtyDaysPython'
print(challenge.isalnum()) # True

challenge = '30DaysPython'
print(challenge.isalnum()) # True

challenge = 'thirty days of python'
print(challenge.isalnum()) # False --because there are spaces

challenge = 'thirty days of python 2019'
print(challenge.isalnum()) # False --beacuse there are spaces
print('-'*50)      #printing the section breaker

# isalpha(): Checks if all characters are alphabets

challenge = 'thirty days of python'
print(challenge.isalpha()) # True
num = '123'
print(num.isalpha())      # False
print('-'*50)      #printing the section breaker

# isdigit(): Checks Digit Characters

challenge = 'Thirty'
print(challenge.isdigit()) # False
challenge = '30'
print(challenge.isdigit())   # True
print('-'*50)      #printing the section breaker

# isdecimal():Checks decimal characters

num = '10'
print(num.isdecimal()) # True
num = '10.5'
print(num.isdecimal()) # False
print('-'*50)      #printing the section breaker


# isidentifier():Checks for valid identifier, means it check if a string is a valid variable name

challenge = '30DaysOfPython'
print(challenge.isidentifier()) # False, because it starts with a number
challenge = 'thirty_days_of_python'
print(challenge.isidentifier()) # True
print('-'*50)      #printing the section breaker


# islower():Checks if all alphabets in a string are lowercase

challenge = 'thirty days of python'
print(challenge.islower()) # True
challenge = 'Thirty days of python'
print(challenge.islower()) # False
print('-'*50)      #printing the section breaker

# isupper(): returns if all characters are uppercase characters

challenge = 'thirty days of python'
print(challenge.isupper()) #  False
challenge = 'THIRTY DAYS OF PYTHON'
print(challenge.isupper()) # True
print('-'*50)      #printing the section breaker

# isnumeric():Checks numeric characters

num = '10'
print(num.isnumeric())      # True
print('ten'.isnumeric())    # False
print('-'*50)      #printing the section breaker

# join(): Returns a concatenated string

web_tech = ['HTML', 'CSS', 'JavaScript', 'React']
result = ', #'.join(web_tech)
print(result) # 'HTML, #CSS, #JavaScript, #React'
print('-'*50)      #printing the section breaker

# strip(): Removes both leading and trailing characters

challenge = 'python'
print(challenge.strip('thon')) # py
print('-'*50)      #printing the section breaker

# replace(): Replaces substring inside

challenge = 'thirty days of python'
print(challenge.replace('python', 'coding')) # 'thirty days of coding'
print('-'*50)      #printing the section breaker

# split():Splits String from Left

challenge = 'thirty days of python'
print(challenge.split()) # ['thirty', 'days', 'of', 'python']
print('-'*50)      #printing the section breaker

# title(): Returns a Title Cased String

challenge = 'thirty days of python'
print(challenge.title()) # Thirty Days Of Python
print('-'*50)      #printing the section breaker

# swapcase(): Convert uppercase into lowercase and vice versa
  
challenge = 'thirty days of python'
print(challenge.swapcase())   # THIRTY DAYS OF PYTHON
challenge = 'Thirty Days Of Python'
print(challenge.swapcase())  # tHIRTY dAYS oF pYTHON
print('-'*50)      #printing the section breaker

# startswith(): Checks if String Starts with the Specified String

challenge = 'thirty days of python'
print(challenge.startswith('thirty')) # True
challenge = '30 days of python'
print(challenge.startswith('thirty')) # False
print('-'*50)      #printing the section breaker

print('''
 #Created by: Ayesha Noreen |Follow us on www.linkedin.com/in/khatoonintech | We love #AUGUSTHON 💕
      ''')