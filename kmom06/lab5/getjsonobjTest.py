"""
Get json object from dbwebb.se and save it to file.
"""
import random
import json
import requests

url = "https://dbwebb.se/repo/javascript/example/lekplats/get-marvin-quotes-using-ajax/quote.php?all"

req = requests.get(url)

print("\nThe response status code is:\n", req.status_code)

print("\nThe response body is:\n", req.text)

jsonObj = req.json()
#print("\nQuote of today is:\n\"{quote}\"\n".format(quote=json["quote"]))
with open("json.txt", "w") as jsonFile:
    json.dump(jsonObj, jsonFile, indent=4)

# Try reading the object from file and print a random quote.
with open("json.txt", "r") as jsonFile:
    jsonObj = json.load(jsonFile)

    # Randomize a number.
    print(random.choice(jsonObj["quotes"]))
