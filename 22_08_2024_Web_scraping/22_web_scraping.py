'''
make sure to run in terminal before running this file

pip install bs4 
pip install requests

'''
# Import the necessary modules
import requests
from bs4 import BeautifulSoup   

# Declare the URL of the website to scrape
url = 'https://archive.ics.uci.edu/dataset/53/iris.php'


# Use the requests get method to fetch data from the URL
response = requests.get(url)

# Check the status of the response
status = response.status_code
print(status)  # Output: 200 (means the fetching was successful)

# Use BeautifulSoup to parse the content from the page
content = response.content  # Get all the content from the website
soup = BeautifulSoup(content, 'html.parser')  # BeautifulSoup will parse the content

# Print the title of the webpage
print(soup.title)  # Output: <title>UCI Machine Learning Repository: Data Sets</title>
print(soup.title.get_text())  # Output: UCI Machine Learning Repository: Data Sets

# Print the entire body of the webpage
print(soup.body)
print(soup.body.get_text())

# Find all the tables 
tables = soup.find('table', class_="my-4 table w-full")
print(tables.get_text())

#Getting headers of the table
th=soup.find_all('th')  # returns a list
print(th)
#To get text from headers we us loop
headers='\t\t'.join(i.get_text() for i in th)
print(headers)
# Iterate over the rows in the table and print the text in each cell
td=soup.find_all('td')

table_body='\t\t'.join(i.get_text() for i in td)
print(table_body)
print('''
#Created by: Ayesha Noreen |Follow us on www.linkedin.com/in/khatoonintech | We love #AUGUSTHON 💕
    ''')
