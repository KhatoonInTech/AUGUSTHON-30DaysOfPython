import re

# Example 1: Using re.match()
txt = 'I love to teach python and javaScript'
# It returns an object with span, and match
match = re.match('I love to teach', txt, re.I)
print(match)  # Expected output: <re.Match object; span=(0, 15), match='I love to teach'>
span = match.span()
print(span)  # Expected output: (0, 15)
start, end = span
substring = txt[start:end]
print(substring)  # Expected output: I love to teach

# Example 2: Using re.search()
txt = '''Python is the most beautiful language that a human being has ever created.
I recommend python for a first programming language'''
match = re.search('first', txt, re.I)
print(match)  # Expected output: <re.Match object; span=(100, 105), match='first'>
span = match.span()
print(span)  # Expected output: (100, 105)
start, end = span
substring = txt[start:end]
print(substring)  # Expected output: first

# Example 3: Using re.findall()
matches = re.findall('language', txt, re.I)
print(matches)  # Expected output: ['language', 'language']

# Example 4: Replacing a substring
match_replaced = re.sub('Python|python', 'JavaScript', txt, re.I)
print(match_replaced)  # Expected output: JavaScript is the most beautiful language that a human being has ever created.

# Example 5: Splitting text using re.split()
txt = '''I am teacher and  I love teaching.
There is nothing as rewarding as educating and empowering people.'''
print(re.split('\n', txt))  # Expected output: ['I am teacher and  I love teaching.', 'There is nothing as rewarding as educating and empowering people.']

# Example 6: Writing RegEx patterns
regex_pattern = r'apple'
txt = 'Apple and banana are fruits.'
matches = re.findall(regex_pattern, txt)
print(matches)  # Expected output: ['apple']

# Example 7: Using square brackets in regex
regex_pattern = r'[Aa]pple'
matches = re.findall(regex_pattern, txt)
print(matches)  # Expected output: ['Apple', 'apple']

# Example 8: Using escape character in regex
regex_pattern = r'\d+'
txt = 'This regular expression example was made on December 6, 2019.'
matches = re.findall(regex_pattern, txt)
print(matches)  # Expected output: ['6', '2019']

# Example 9: Using quantifiers in regex
regex_pattern = r'\d{4}'
matches = re.findall(regex_pattern, txt)
print(matches)  # Expected output: ['2019']

# Example 10: Clean text and count frequent words
sentence = '''%I $am@% a %tea@cher%, &and& I lo%#ve %tea@ching%;.'''
cleaned_text = re.sub(r'[%$@&#]', '', sentence)
print(cleaned_text)  # Expected output: I am a teacher and I love teaching.



print('''
 #Created by: Ayesha Noreen |Follow us on www.linkedin.com/in/khatoonintech | We love #AUGUSTHON 💕
      ''')