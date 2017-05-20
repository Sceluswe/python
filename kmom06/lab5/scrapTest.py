"""
Scrap information from dbwebb.se.
"""
import requests
from bs4 import BeautifulSoup

# Get webpage
url = "http://www.student.bth.se/~emmd12/javascript/Kmom03/me/"
req = requests.get(url)
req = req.text
print(type(req))

# Get the webpage content as a soup
soup = BeautifulSoup(req, "html.parser")
print(type(soup.prettify()))

with open("../marvin5/webpage.txt", "r") as inputfile:
    req = inputfile.read()
    req.replace("\n", " ")

soup = BeautifulSoup(req, "html.parser")
print(soup.find("title"))
print(type(soup.findAll("title")))
print(len(soup.findAll("title")))
titles = soup.findAll("title")

my_arr = []
for title in titles:
    my_arr.append(title.text)

print(type(my_arr[0]))

for i, title in enumerate(my_arr):
    print(title)
    print("number of letters in title: " + str(len(title)))
#print(soup.prettify())




# Get all elements looking like <p class="irclog">
#ircLog = soup.findAll("p")

#print(soup.prettify())


#for node in ircLog:
#    print(''.join(node.findAll(text=True)))
