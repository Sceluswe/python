"""
Save json to json file.
"""
import json

def saveJSONInventory(newItems=None):
    """
    Take a list and save it to a JSON file if it has less then 4 elements.
    Return boolean.
    """
    returnBool = False
    with open("json.txt", "w") as JSONfile:
        JSONobject = {"marvinArray": []}
        for eachitem in newItems:
            JSONobject["marvinArray"].append({"item": eachitem})
        json.dump(JSONobject, JSONfile, indent=4)
        returnBool = True

    return returnBool
# Create a dictionary
my_dict = {"lel": "test", "nej": "test1"}
# Save dictionary in a dict called seo
jsonObj = {"seo": my_dict}
# make it a json object and dump it to a file.

with open("dbwebbSeo.txt", "w") as jsonFile:
    json.dump(jsonObj, jsonFile, indent=4)
