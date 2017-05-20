"""
Pings a webpage, prints it's status code.
"""
import requests

url = "http://dbwebb.se/humans.txt"
req = requests.head(url)

print("Request to ", url)
print("Recieved status code: ", req.status_code)
