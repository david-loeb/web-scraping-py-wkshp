# 0) Import necessary libraries
from bs4 import BeautifulSoup
import requests

# 1) Define variable that has the URL
website = 'https://subslikescript.com/movie/Titanic-120338'

# 2) Use requests.get(url) to get the HTML from the site, 
# and save as a Response object
result = requests.get(website)

# 3) Extract text out of the HTML, using Response.text method
content = result.text

# 4) Use the parser to get the result
soup = BeautifulSoup(content,'lxml')

# Print the result of this process, just so you see what the HTML is like
# prettify() is just a method to make ur HTML look nicer
print(soup.prettify())

# 5) Locate elements u want in the HTML with .find() or .find_all()
box = soup.find('article', class_='main-article')

# 6) Use the .get_text() method after you've located elements with .find() 
# to extract contents from the elements
title = soup.find('title').get_text()

# Print the extracted text content (just to see what it's like)
print(title)
print(box.get_text())

# 7) Save the extracted data in a file
with open('title.txt', 'w') as file:
    file.write(title)
# open() creates a text file named 'title.txt'
# 'w' opens the file in "write" mode which is how you add things to files
# file.write(title) saves the content of the 'title' object to the txt file

