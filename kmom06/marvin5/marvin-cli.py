#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Example to show how command-line options can be handled by a script.
"""



import sys
import os
import json
import random
from datetime import datetime
import getopt
import sqlite3
import requests
from bs4 import BeautifulSoup




#
# Add some stuff about this script
#
PROGRAM = os.path.basename(sys.argv[0])
AUTHOR = "Emil Mattsson"
EMAIL = "emilcbm@gmail.com"
VERSION = "0.0.1"
USAGE = """{program} - Print my name. By {author} ({email}), version {version}.
Usage:
  {program} [options] command [arguments-to-the-command]
Options:
  -h --help                      Display this help message.
  -v --version                   Print version and exit.
  -s --silent                    Do not display any details or statistics about the execution.
  --verbose                      Display details about the execution.
  --output=<file> get <url>      Gets a webpage and saves to <file>.
  --input=<file> quote           Get a quote from a JSON file.
  --input=<file> title           Get title from a web page saved to file.
  -- json seo <url>              SEO test the <url> and save to json.
  -- json --input=<file> seo     SEO test a web page from a file.
  -- json --input=<file> seo     SEO test a web page from a file and save to json.

Commands:
  ping <url>                     Ping a webpage and save some info.
  ping-history                   Display history of all pings made.
  get <url>                      Get a webpage and print it.
  quote                          Get a quote from dbwebb.se Marvin.
  title <url>                    Get a title from a webpage.
  seo <url>                      SEO analyze a webpage.

""".format(program=PROGRAM, author=AUTHOR, email=EMAIL, version=VERSION)

MSG_VERSION = "{program} version {version}.".format(program=PROGRAM, version=VERSION)
MSG_USAGE = "Use {program} --help to get usage.\n".format(program=PROGRAM)




#
# Global default settings affecting behaviour of script in several places
#
SILENT = False
VERBOSE = True
SAVEFILE = False
INPUTFILE = False
USEJSON = False

# Exit status 0
EXIT_SUCCESS = 0
EXIT_USAGE = 1
EXIT_FAILED = 2

# -------- database wrapper functions --------
def dbInPingHistory(response, url, rDate):
    """
    Establish a connection to the db and insert ping history.
    """
    if VERBOSE:
        print("Saving ping history...")

    try:
        if not os.path.isfile("ping-history.sqlite"):
            assert False, "FAILED: Database does not exist."
        # Create a connection and a cursor
        with sqlite3.connect("ping-history.sqlite") as db:
            dbc = db.cursor()
            # Insert history.
            aTuple = (response, url, rDate)
            dbc.execute("INSERT INTO ping_history (response, url, rDate) VALUES (?, ?, ?)", aTuple)

    except Exception as err:
        print(err)
        print("FAILED: Connection to database could not be establised.")
        sys.exit(EXIT_FAILED)

    if VERBOSE:
        print("Ping history saved.")



def dbOutPingHistory():
    """
    Get ping history from the database. Return Array of tuples.
    """
    if VERBOSE:
        print("Loading ping history...")

    result = []

    try:
        if not os.path.isfile("ping-history.sqlite"):
            assert False, "FAILED: Database does not exist."

        # Connect to db and get the info.
        with sqlite3.connect("ping-history.sqlite") as db:
            dbc = db.cursor()
            dbc.execute("SELECT id, response, url, rDate FROM ping_history")

            for row in dbc:
                result.append(row)

    except Exception as err:
        print(err)
        print("FAILED: Connection to database could not be establised.")
        sys.exit(EXIT_FAILED)

    if VERBOSE:
        print("Ping history loaded.")

    return result



# -------- package functions --------
def printUsage():
    """
    Print usage information about the script and exit.
    """
    print(USAGE)
    sys.exit(EXIT_SUCCESS)



def printVersion():
    """
    Print version information and exit.
    """
    print(MSG_VERSION)
    sys.exit(EXIT_SUCCESS)



def pingSite(url):
    """
    Ping a website using the global URL.
    """
    try:
        req = requests.head(url)

        # Check if the ping worked or not.
        if req is None:
            assert False, "Cannot ping: " + url

        if VERBOSE:
            print("Ping request sent to: ", url)
            print("Response received: " + req.headers["Date"])

        print("Recieved status code: ", req.status_code)

        # Save ping history.
        dbInPingHistory(req.status_code, url, req.headers["Date"])

    except Exception as err:
        print(err)
        print("Ping was unsuccessful.")
        sys.exit(EXIT_FAILED)



def printPingHistory():
    """
    Print the ping history.
    """
    if VERBOSE:
        print("Printing history...")

    try:
        # Get ping history in a list of tuples.
        tuples_list = dbOutPingHistory()

        for i, response, url, rDate in tuples_list:
            print("{i}. ({response}, {url}, {rDate})".format(i=i, response=response, url=url, rDate=rDate))

    except Exception as err:
        print(err)
        sys.exit(EXIT_FAILED)




def downloadWebpage(url, savefile=False):
    """
    Download an entire webpage and print it.
    """
    if VERBOSE:
        print("Downloading web page...")
    try:
        # Get webpage
        req = requests.get(url)

        if req is None:
            assert False, "Cannot find: " + url

        # Get the webpage content as a soup.
        soup = BeautifulSoup(req.text, "html.parser")

        # Save webpage if savefile=True, else print it.
        if savefile:
            if VERBOSE:
                print("Saving web page to: " + savefile)

            if not os.path.isfile(savefile):
                open(savefile, "x")

            with open(savefile, "w") as theFile:
                theFile.write(str(soup))


            print("Web page saved.")
        else:
            print(soup.prettify())
    except Exception as err:
        print(err)
        print("File could not be saved.")
        sys.exit(EXIT_FAILED)



def getdbwebbQuote():
    """
    Get a quote from Marvin, from dbwebb.se
    """
    if VERBOSE:
        print("Getting json quote from dbwebb.se")

    try:
        url = "http://dbwebb.se/javascript/lekplats/get-marvin-quotes-using-ajax/quote.php"

        # Get site.
        req = requests.get(url)

        if req is None:
            assert False, "Cannot find: " + url

        # Handle json object.
        jsonObj = req.json()
        # Get quote from json object.
        print("\nQuote of today is:\n\"{quote}\"\n".format(quote=jsonObj["quote"]))

    except Exception as err:
        print(err)
        sys.exit(EXIT_FAILED)



def getjsonQuote(jsonfile):
    """
    Get a Quote from a json file.
    """
    if VERBOSE:
        print("Getting quote from json file.")
    # Try reading the object from file and print a random quote.
    try:
        with open(jsonfile, "r") as jsonFile:
            jsonObj = json.load(jsonFile)

            # Randomize a number.
            print(random.choice(jsonObj["quotes"]))

    except Exception as err:
        print(err)
        sys.exit(EXIT_FAILED)



def getWebpageTitle(url=False, afile=False):
    """
    Get the <title> from a webpage or file.
    """
    if VERBOSE:
        print("Getting title from webpage...")

    try:
        req = ""
        # Get webpage
        if url and not afile:
            req = requests.get(url)
            req = req.text

        elif afile and not url:
            with open(afile, "r") as inputfile:
                req = inputfile.read()
        else:
            assert False, "getWebpageTitle: both arguments cannot be true."

        if req is None:
            assert False, "Cannot find: " + url

        # Get the webpage content as a soup
        soup = BeautifulSoup(req, "html.parser")

        titleContent = ''.join(soup.find("title"))

        print(titleContent)
    except Exception as err:
        print(err)
        sys.exit(EXIT_FAILED)



def seoAnalyze(url=False, afile=False):
    """
    Analyze a webpage through the perspective of seo.
    """
    if VERBOSE:
        print("Performing SEO analysis...")

    try:
        req = ""
        # Get webpage
        if url and not afile:
            req = requests.get(url)
            req = req.text

        elif afile and not url:
            with open(afile, "r") as inputfile:
                req = inputfile.read()
        else:
            assert False, "seoAnalyze: both arguments cannot be true."

        if req is None:
            assert False, "Cannot find: " + url

        # Get the webpage content as a soup
        soup = BeautifulSoup(req, "html.parser")

        # Get the number of title tags.
        titles = soup.findAll("title")
        print("\nNumber of titles: " + str(len(titles)))

        for i, title in enumerate(titles):
            print("Chars in title" + str(i+1) + ": " +  str(len(title.text)))

        h1tags = soup.findAll("h1")
        print("\nNumber of <h1> elements: " + str(len(h1tags)))

        h2tags = soup.findAll("h2")
        print("Number of <h2> elements: " + str(len(h2tags)))

        atags = soup.findAll("a")
        print("Number of <a> elements: " + str(len(atags)))

        if USEJSON:
            # Create a dictionary
            seo_tuplelist = [("h1tags", str(len(h1tags))), ("h2tags", str(len(h2tags))), ("atags", str(len(atags)))]
            seo_tuplelist.append(("nrOfTitles", str(len(titles))))
            # Put all titles in json.
            for i, title in enumerate(titles):
                seo_tuplelist.append(("Chars in title" + str(i+1), str(len(title.text))))
            # Save dictionary in a dict called seo
            jsonObj = {"seo": seo_tuplelist}
            # Dump json to file.
            with open("dbwebbSeo.txt", "w") as jsonFile:
                json.dump(jsonObj, jsonFile, indent=4)

    except Exception as err:
        print(err)
        sys.exit(EXIT_FAILED)



def parseOptions():
    """
    Merge default options with incoming options and arguments and return them as a dictionary.
    """

    # Switch through all options
    try:
        global VERBOSE, SAVEFILE, INPUTFILE, USEJSON

        # Get the arguments from the command-line.
        # arg1 is the argument list to be parsed.
        # arg2 is the short name for the options ":" indicates the option
        # needs an argument.
        # arg3 is the long name version of each option.
        longopts_arr = ["help", "version", "verbose", "silent", "output=", "input=", "json"]
        opts, args = getopt.getopt(sys.argv[1:], "d:hr:svp:", longopts_arr)

        # Check which one of the options has been selected.
        for opt, arg in opts:
            # Print the help options and exit with status code 0.
            # -------- Standard options --------
            if opt in ("-h", "--help"):
                printUsage()

            elif opt in ("-v", "--version"):
                printVersion()

            elif opt in ("-s", "--silent"):
                VERBOSE = False

            elif opt in ("--verbose"):
                VERBOSE = True

            elif opt in ("--output"):
                SAVEFILE = arg

                if VERBOSE:
                    print("Setting SAVEFILE to: " + arg)

            elif opt in ("--input"):
                if not arg or not os.path.isfile(arg):
                    assert False, "input: FILE argument or file missing, input=<file>"

                INPUTFILE = arg

                if VERBOSE:
                    print("Setting INPUTFILE to: " + arg)

            elif opt in ("--json"):
                USEJSON = True
            else:
                assert False, "Unhandled option"

        # -------- Handle Commands: --------
        if args[0] == "ping":
            if not args[1]:
                assert False, "-p ping: URL argument missing."
            url = args[1]

            if VERBOSE:
                print("Setting URL to: " + url)

            pingSite(url)

        elif args[0] == "ping-history":
            printPingHistory()

        elif args[0] == "get":
            if not args[1]:
                assert False, "get: URL argument missing."

            url = args[1]

            if VERBOSE:
                print("Setting URL to: " + url)

            downloadWebpage(url, SAVEFILE)

        elif args[0] == "quote":
            if not INPUTFILE:
                getdbwebbQuote()
            else:
                getjsonQuote(INPUTFILE)

        elif args[0] == "title":
            if not INPUTFILE:
                if not args[1]:
                    assert False, "get: URL argument missing."

                url = args[1]

                if VERBOSE:
                    print("Setting URL to: " + url)

                getWebpageTitle(url=url)

            else:
                getWebpageTitle(afile=INPUTFILE)

        elif args[0] == "seo":
            if not args[1]:
                assert False, "seo: URL argument missing."

            url = args[1]

            if VERBOSE:
                print("Setting URL to: " + url)

            seoAnalyze(url)

    except Exception as err:
        print(err)
        print(MSG_USAGE)
        # Prints the callstack, good for debugging, comment out for production
        #traceback.print_exception(Exception, err, None)
        sys.exit(EXIT_USAGE)



def main():
    """
    Main function to carry out the work.
    """
    # Get the startTime of the program.
    startTime = datetime.now()

    # Handle the arguments.
    parseOptions()

    # Calculate when the program finished.
    timediff = datetime.now() - startTime
    if VERBOSE:
        sys.stderr.write("Script executed in {}.{} seconds\n".format(timediff.seconds, timediff.microseconds))

    sys.exit(EXIT_SUCCESS)



if __name__ == "__main__":
    main()
