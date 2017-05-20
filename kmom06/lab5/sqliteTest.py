"""
Creates a SQLite table and inserts a row, then prints columns from that row.
"""
import sqlite3
import requests

with sqlite3.connect("sqliteTest1.sqlite") as db:
    # Create a connection and a cursor
    #db = sqlite3.connect("sqliteTest1.sqlite")
    dbc = db.cursor()

    # Perform SQL queries
    dbc.execute("CREATE TABLE IF NOT EXISTS Pings (url TEXT, time TEXT, response INTEGER)")

    # Make requests and get the values for our database.
    url = "http://dbwebb.se/humans.txt"
    req = requests.head(url)
    code = req.status_code
    rTime = req.headers['Date']

    aTuple = (url, rTime, code)
    dbc.execute("INSERT INTO main.Pings (url, time, response) VALUES (?, ?, ?)", aTuple)
    dbc.execute("SELECT url, time, response FROM Pings")

    # Loop through a resultset from a SELECT query
    for row in dbc:
        print(type(row))
        print(row)
