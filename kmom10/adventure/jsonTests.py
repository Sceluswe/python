#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Load and save functions.
"""

import json

def loadJSON(filename):
    """
    Load a JSON file.
    Return JSON object.
    """
    returnObj = None
    # Load the JSON file.
    with open(filename, "r") as JSONfile:
        returnObj = json.load(JSONfile)

    return returnObj

def saveJSON(filename, JSONobject):
    """
    Take a sequence and save it as JSON.
    """
    # Try to create the file, if it exists just move on.
    try:
        open(filename, "x")
    except FileExistsError:
        pass
    # Save the sequence to the file.
    with open(filename, "w") as JSONfile:
        json.dump(JSONobject, JSONfile, indent=4)

jsonObj = loadJSON("json.txt")
print(jsonObj)

saveJSON("json1.txt", {"marvin": {"axe": 1}})
saveJSON("json2.txt", [("lel", 1), ("lel", 2), ("lel", 3)])
saveJSON("json3.txt", "Stringmystringstring")

jsonObj = loadJSON("json1.txt")
print("\n")
print(jsonObj)

jsonObj = loadJSON("json2.txt")
print("\n")
print(jsonObj)

jsonObj = loadJSON("json3.txt")
print("\n")
print(jsonObj)

room1 = {"room1": {}}
room1["room1"]["box"] = {"description": "En {status} trälåda.", "status": "stor fyrkantig", "pickable": False}
room1["room1"]["axe"] = {"description": "En yxa", "status": ", nyvässad men med sprucket handtag.", "pickable": True}
room1["room1"]["door"] = {"description": "En trädörr.", "status": "låst", "pickable": False}

saveJSON("room1.txt", room1)

my_dict = loadJSON("room1.txt")

print(my_dict["room1"]["box"])
