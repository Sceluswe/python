#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Underlying functions used to create the viking game.
"""

import os
import json

GRAPHICS = [":------:\n|     T|\n|      /\n|     B|\n:------:\n",
            ":------:\n|  K   |\n/  <>  /\n|      |\n:------:\n",
            ":------:\n|      |\n/   L  /\n|      |\n:------:\n",
            ":------:\n| F    |\n/   B  /\n|      |\n:------:\n",
            ":------:\n|      |\n/   O  /\n|      |\n:------:\n",
            ":------:\n|      |\n/      /\n|      |\n:------:\n"]

POSSIBLEROOMS = ["room0", "room1", "room2", "room3", "room4", "room5", "room6", "room7"]
ROOMS = {}
ITEMS = {}
ACTIVEROOM = "room1"
PREVROOM = "room0"
COMMANDS = """
Marvin tittar uppmärksamt på dig innan han ler och säger: "Dessa order lyder jag":
quit            Avslutar programmet.
i, info         Skriver ut beskrivningen av rummet.
h, hjälp        Skriver ut denna lista.
fr, fram        Gå framåt till nästa rum, om det är upplåst.
ba, bak         Gå bakåt till föregående rum.
se              Titta dig runt omkring.
l, ledtråd      Ger dig en ledtråd för hur man löser rummet.

För att manipulera föremål:
o, objekt                       Skriver ut vilka objekt som finns i rummet.
t [objekt], titta [objekt]      Skriver ut beskrivningen av det nämnda objektet.
ö [objekt], öppna [objekt]      Öppna objektet om det går.
s [objekt], sparka [objekt]     Sparka sönder ett objekt om det går.
f [objekt], flytta [objekt]     Flytta objekt om det går.

Marvins väska:
inv, inventarier            Skriver ut vad som finns i väskan.
ta [objekt]                 Försöker lägga ett objekt i väskan.
sl [objekt], släpp [objekt] Släpper ett objekt.
a [objekt], använd [objekt] Använd ett objekt.

save [fil]        Skriv in filnamn (ingen filtyp) och spara ditt spel.
load [fil]        Skriv in filnamn (ingen filtyp) och ladda ditt spel.
"""

def commandMenu(choice):
    """
    All the possible commands in the game.
    """
    if choice == "i" or "info" in choice:
        print("\n" + getRoomDescription() + "\n")

    elif choice == "h" or "hjälp" in choice:
        print("\n" + COMMANDS + "\n")

    elif choice == "fr" or "fram" in choice:
        print("\n" + walkForward() + "\n")
        print("\n" + getRoomDescription() + "\n")

    elif choice == "ba" or "bak" in choice:
        if ACTIVEROOM != "room6":
            print("\n" + walkBackward() + "\n")
            print("\n" + getRoomDescription() + "\n")
        else:
            print("Dörren är låst.")

    elif "se" in choice:
        print("\n" + getRoomInspection() + "\n")

    elif choice == "l" or "ledtråd" in choice:
        print("\n" + getRoomClue() + "\n")

    elif choice == "o" or "objekt" in choice:
        print("\n" + getRoomObjects() + "\n")

    elif "t " in choice[:2] or "titta" in choice:
        strip = choice[2:] if "t " in choice else choice[6:]
        print("\n" + inspectObject(strip) + "\n")

    elif "ö " in choice[:2] or "öppna" in choice:
        strip = choice[2:] if "ö " in choice else choice[6:]
        print("\n" + openObject(strip) + "\n")

    elif "s " in choice[:2] or "sparka" in choice:
        strip = choice[2:] if "s " in choice else choice[7:]
        print("\n" + kickObject(strip) + "\n")

    elif "f " in choice[:2] or "flytta" in choice:
        strip = choice[2:] if "f " in choice else choice[7:]
        print("\n" + moveObject(strip) + "\n")

    # -------- Inventory --------
    # Använd klo.
    elif "inv" in choice[:3] or "inventarier" in choice:
        print("\n" + getInventory() + "\n")

    elif "ta " in choice[:3]:
        print("\n" + pickItem(choice[3:]) + "\n")

    elif "sl " in choice[:3] or "släpp" in choice[:6]:
        strip = choice[3:] if "inv" in choice else choice[6:]
        print("\n" + dropItem(strip) + "\n")

        if ACTIVEROOM == "room5" and strip == "nyckel":
            # Drop the silver key.
            ROOMS[ACTIVEROOM]["objects"]["dörr"]["locked"] = False
            # Delete it so "it falls down the well".
            del ROOMS[ACTIVEROOM]["objects"]["nyckel"]
            # Print flavor.
            print("Ett högt mekaniskt \"klick\" ekar igenom rummet och Marvin skinner upp.")

    elif "a " in choice[:2] or "använd" in choice:
        strip = choice[2:] if "a " in choice else choice[7:]
        print("\n" + useInventoryObject(strip) + "\n")

    # -------- Save and load game --------
    elif "save " in choice[:5]:
        print("\n" + saveGame(choice[5:]) + "\n")

    elif "load " in choice[:5]:
        print("\n" + loadSavedGame(choice[5:]) + "\n")

    else:
        print("\n" + "\"Vad vill du att jag ska göra?\" frågar Marvin. \"Du kan alltid be om hjälp.\"" + "\n")



def useInventoryObject(item):
    """
    Checks if the specified object can be used.
    """
    result = "\"Ingenting hände.\", Marvin ser fundersam ut.\"Har jag plockat upp den?\""
    # Make sure the item exists in the players inventory first.
    if item in ITEMS["inventory"]:
        if item == "nyckel" and ACTIVEROOM == "room1":
            result = unlockObject(item, "dörr")

        elif item == "klo" and ACTIVEROOM == "room2":
            # If the two objects have the same status name:
            if ITEMS["inventory"]["klo"]["status"] == ROOMS[ACTIVEROOM]["objects"]["stenblock"]["status"]:
                result = unlockObject(item, "dörr")

        elif item == "yxa" and ACTIVEROOM == "room3":
            ROOMS[ACTIVEROOM]["objects"]["dörr"]["destructable"] = True
            result = kickObject("dörr")

        elif item == "fågelben" and ACTIVEROOM == "room4":
            result = "Marvin placerar fågelbenen på rätt plats. " + unlockObject(item, "dörr")

        elif item == "yxa" and ACTIVEROOM == "room6":
            result = "Marvin går gråtande av sorg och lycka till det sista rummet."
            result += "Gå nu igenom labyrinten till din frihet, Marvin."
            nextRoom()
            # Launch Game

    elif item == "marvin" and ACTIVEROOM == "room6":
        result = "Du lämnar resterna av din trogne tjänare bakom dig och går in i det sista testet."
        result += "\nGå nu igenom labyrinten till din frihet."
        nextRoom()
        # Launch game.


    return result



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
    Take a sequence and save it as JSON, return bool.
    """
    result = False
    # Try to create the file, if it exists just move on.
    try:
        open(filename, "x")
    except FileExistsError:
        pass
    # Save the sequence to the file.
    with open(filename, "w") as JSONfile:
        json.dump(JSONobject, JSONfile, indent=4)
        result = True

    return result



def loadDefaultGame(roomsFile, itemsFile):
    """
    Loads all the DEFAULT game rooms into memory.
    """
    global ROOMS, ITEMS, ACTIVEROOM
    ACTIVEROOM = "room1"
    ROOMS = loadJSON(roomsFile)
    ITEMS = loadJSON(itemsFile)



def saveGame(saveFile):
    """
    Saves the game state for a player.
    """
    result = "Save was not successful. Did you specify a name?"
    # Make sure saveFile is not an empty string.
    if saveFile:
        ROOMS["activeroom"] = ACTIVEROOM
        check1 = saveJSON("rooms" + saveFile + ".txt", ROOMS)
        check2 = saveJSON("inv" + saveFile + ".txt", ITEMS)

        if check1 and check2:
            result = "Save successful."

    return result



def loadSavedGame(saveFile):
    """
    Loads a save file, returns message with status of failure/success.
    """
    global ROOMS, ITEMS, ACTIVEROOM
    result = saveFile + "File does not exist."

    if not saveFile:
        result = "You must enter the name of the file."

    elif os.path.isfile("inv" + saveFile + ".txt") and os.path.isfile("rooms" + saveFile + ".txt"):
        ROOMS = loadJSON("rooms" + saveFile + ".txt")
        ITEMS = loadJSON("inv" + saveFile + ".txt")
        ACTIVEROOM = ROOMS["activeroom"]
        result = "Save loaded successfully."

    return result



def getRoomDescription():
    """
    Gets the description from the specified room.
    """
    result = ROOMS[ACTIVEROOM]["description"]

    if ACTIVEROOM != "room7":
        index = [i for i, r in enumerate(POSSIBLEROOMS) if r == ACTIVEROOM][0] - 1
        result += "\n" + GRAPHICS[index] + "\n"
    # Return description
    return result



def getRoomClue():
    """
    Returns a clue that helps the player solve the room.
    """
    return ROOMS[ACTIVEROOM]["clue"]



def getRoomInspection():
    """
    Points out the most important object in the room.
    """
    return ROOMS[ACTIVEROOM]["inspect"]



def getRoomObjects():
    """
    Returns the description of ALL VISIBLE objects in the room.
    """
    result = ""
    for key in ROOMS[ACTIVEROOM]["objects"]:
        if ROOMS[ACTIVEROOM]["objects"][key]["visible"]:
            result += getObjectDescription(key) + " "

    return result



def getObjectDescription(obj):
    """
    Returns the description of ONE object.
    """
    result = "\"Inte ens jag kan beskriva det där\", säger Marvin."
    # If the object is in the room:
    if obj in ROOMS[ACTIVEROOM]["objects"]:
        if "status" in ROOMS[ACTIVEROOM]["objects"][obj]:
            status = ROOMS[ACTIVEROOM]["objects"][obj]["status"]
            # Add object status and item description to description.
            result = ROOMS[ACTIVEROOM]["objects"][obj]["description"].format(status=status)
        else:
            result = ROOMS[ACTIVEROOM]["objects"][obj]["description"]
    # else if the object is in the player inventory.
    elif obj in ITEMS["inventory"]:
        if "status" in ITEMS["inventory"][obj]:
            status = ITEMS["inventory"][obj]["status"]
            # Add object status and item description to description.
            result = ITEMS["inventory"][obj]["description"].format(status=status)
        else:
            result = ITEMS["inventory"][obj]["description"]
    else:
        assert False, "obj: " + obj + " does NOT exist."

    return result



def inspectObject(obj):
    """
    Return the inspection text of an object.
    """
    result = "\"Det finns inget sådant objekt.\" svarar Marvin."

    if obj in ROOMS[ACTIVEROOM]["objects"]:
        result = getObjectDescription(obj) + " "
        result += ROOMS[ACTIVEROOM]["objects"][obj]["inspect"]

    elif obj in ITEMS["inventory"]:
        result = getObjectDescription(obj) + " "
        result += ITEMS["inventory"][obj]["inspect"]

    return result



def openObject(obj):
    """
    Attempts to open the object.
    """
    result = "\"Det funkar inte.\", säger Marvin."

    if obj in ROOMS[ACTIVEROOM]["objects"]:
        if ROOMS[ACTIVEROOM]["objects"][obj]["openable"] and ROOMS[ACTIVEROOM]["objects"][obj]["contains"]:
            item = ROOMS[ACTIVEROOM]["objects"][obj]["contains"]
            result = "Ni hittade en " + item
            ROOMS[ACTIVEROOM]["objects"][item]["visible"] = True

    return result



def kickObject(obj):
    """
    Kick an object to pieces.
    """
    result = "\"Det funkar inte.\", säger Marvin."

    if obj in ROOMS[ACTIVEROOM]["objects"]:
        if ROOMS[ACTIVEROOM]["objects"][obj]["destructable"] and ROOMS[ACTIVEROOM]["objects"][obj]["visible"]:
            result = "Marvin går lös på objektet: " + obj + " under glada tjut och tjim."

            if ROOMS[ACTIVEROOM]["objects"][obj]["contains"]:
                item = ROOMS[ACTIVEROOM]["objects"][obj]["contains"]
                status = ROOMS[ACTIVEROOM]["objects"][item]["status"]

                ROOMS[ACTIVEROOM]["objects"][item]["visible"] = True

                result += " Ni upptäcker ett nytt objekt bland spillrorna:"
                result += " " +  ROOMS[ACTIVEROOM]["objects"][item]["description"].format(status=status)

            del ROOMS[ACTIVEROOM]["objects"][obj]

        elif ROOMS[ACTIVEROOM]["objects"][obj]["visible"]:
            result = "Marvin skriker till av smärta när han sparkar objektet."
            result += " \"Det kommer inte att gå sönder!\", tjuter han."

    return result



def moveObject(obj):
    """
    Move an object to another location.
    """
    result = "\"Det funkar inte.\" svarar Marvin."

    if obj in ROOMS[ACTIVEROOM]["objects"] and ROOMS[ACTIVEROOM]["objects"][obj]["visible"]:
        if ROOMS[ACTIVEROOM]["objects"][obj]["moveable"]:
            result = ROOMS[ACTIVEROOM]["objects"][obj]["moveDesc"]

            ROOMS[ACTIVEROOM]["objects"][obj]["status"] = circleStatusOpt(obj)

            # If the move object contained something, make it visible.
            contains = ROOMS[ACTIVEROOM]["objects"][obj]["contains"]
            if contains:
                ROOMS[ACTIVEROOM]["objects"][contains]["visible"] = True
        else:
            if "moveDesc" in ROOMS[ACTIVEROOM]["objects"][obj]:
                result = ROOMS[ACTIVEROOM]["objects"][obj]["moveDesc"]

    return result



def circleStatusOpt(obj):
    """
    Takes a list and returns the next index as if it were a
    circular list.
    """
    if "statusopt" in ROOMS[ACTIVEROOM]["objects"][obj]:
        status = ROOMS[ACTIVEROOM]["objects"][obj]["status"]
        statusopt = ROOMS[ACTIVEROOM]["objects"][obj]["statusopt"]
        index = [i for i, x in enumerate(statusopt) if x == status][0]

        if index == (len(statusopt) - 1):
            index = 0
        else:
            index = index + 1
    else:
        assert False, "statusopt does not exist in object: " + obj

    return statusopt[index]



def unlockObject(keyobj, unlockobj):
    """
    Takes an object used as key and the object to unlock.
    """
    result = "\"Jag kan inte låsa upp: " + unlockobj + " med " + keyobj + "\""

    # Make sure both objects exist.
    if unlockobj in ROOMS[ACTIVEROOM]["objects"] and keyobj in ITEMS["inventory"]:
        # Get the name of the item that unlocks the doorobj.
        key = ROOMS[ACTIVEROOM]["objects"][unlockobj]["locked"]

        if key == keyobj:
            ROOMS[ACTIVEROOM]["objects"][unlockobj]["locked"] = False
            result = "Marvin låste upp:" + unlockobj + "."

        elif not ROOMS[ACTIVEROOM]["objects"][unlockobj]["locked"]:
            result = "\"Den är redan upplåst!\" utbrister Marvin glatt."

        else:
            result = "Marvin provar men det funkar inte. \"Detta kanske inte är rätt nyckel?\" undrar Marvin."

    return result



def walkForward():
    """
    Attempt to open the door to the next room.
    """
    result = "Marvin provar att öppna dörren.\"Dörren är låst.\", proklamerar han."

    if "dörr" in ROOMS[ACTIVEROOM]["objects"]:
        if not ROOMS[ACTIVEROOM]["objects"]["dörr"]["locked"]:
            result = "Marvin öppnar dörren och ni går in i nästa rum."
            nextRoom()

    else:
        result = "Dörren är sönderslagen, vägen är fri. Ni går in i nästa rum."
        nextRoom()

    return result



def nextRoom():
    """
    Set the current active room to the next room.
    """
    global PREVROOM, ACTIVEROOM
    # Make previous room the now active room.
    PREVROOM = ACTIVEROOM
    # Calculate index for the next room.
    index = [i for i, x in enumerate(POSSIBLEROOMS) if x == ACTIVEROOM][0] + 1
    # If we're at the last room. Make index smaller.
    if(index == 8):
        index = index - 1
    # Make active room the next room
    ACTIVEROOM = POSSIBLEROOMS[index]



def walkBackward():
    """
    Attempt to walk backwards.
    """
    result = "Dörren är låst."
    if PREVROOM == "room0":
        result = "Bakom dig syns ett svagt ljus ifrån ett hål i taket. Det är omöjligt att klättra upp."

    elif ROOMS[PREVROOM]["objects"]["dörr"]:
        if not ROOMS[PREVROOM]["objects"]["dörr"]["locked"]:
            result = "Ni retirerar bakåt in i föregående rum."
            prevRoom()
    else:
        result = "Ni retirerar bakåt in i föregående rum."
        prevRoom()

    return result



def prevRoom():
    """
    Set the current room to the previous room.
    """
    global ACTIVEROOM

    # Calculate index for previous room.
    index = [i for i, x in enumerate(POSSIBLEROOMS) if x == PREVROOM][0]
    ACTIVEROOM = POSSIBLEROOMS[index]



def getInventory():
    """
    Display the items in the inventory.
    """
    result = "\"Min väska är tom för tillfället\" svarar Marvin."
    if len(ITEMS) > 0:
        result = "Dessa ting har jag i min väska:\n"
        for item in ITEMS["inventory"]:
            result += item + "\n"

    return result



def pickItem(item):
    """
    Add the item argument to our inventory.
    """
    # Set default value for result.
    result = "\"Det funkar inte.\", svarar Marvin."
    if item in ROOMS[ACTIVEROOM]["objects"] and ROOMS[ACTIVEROOM]["objects"][item]["visible"]:
        if ROOMS[ACTIVEROOM]["objects"][item]["pickable"]:
            # Save item in ITEMS.
            ITEMS["inventory"][item] = ROOMS[ACTIVEROOM]["objects"][item]

            # Remove the object from ROOMS.
            del ROOMS[ACTIVEROOM]["objects"][item]

            # Check if saving went well.
            result = "Marvin plockar upp: " + item

    return result



def dropItem(item):
    """
    Drop the provided item in the inventory.
    """
    # Set default value for result and define our list.
    result = "\"Det finns ingen " + item + "\"  säger Marvin."

    if item in ITEMS["inventory"]:
        # Drop the item into the active room.
        ROOMS[ACTIVEROOM]["objects"][item] = ITEMS["inventory"][item]
        result = "Marvin släpper entusiastiskt: " + item
        # Delete the item from our inventory.
        del ITEMS["inventory"][item]
        # Update the saved inventory.

    return result
