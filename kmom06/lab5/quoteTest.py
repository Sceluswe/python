"""
Request a json object from the website and print a quote.
"""
import requests

url = "http://dbwebb.se/javascript/lekplats/get-marvin-quotes-using-ajax/quote.php"

req = requests.get(url)

print("\nThe response status code is:\n", req.status_code)

print("\nThe response body is:\n", req.text)

json = req.json()
print("\nQuote of today is:\n\"{quote}\"\n".format(quote=json["quote"]))
