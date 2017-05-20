#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Code that calculates various information about an airplane. 
And prints it to a webbpage using cgi.

"""

# To write pagecontent to sys.stdout as bytes instead of string
import sys
import codecs

#Enable debugging of cgi-.scripts
import cgitb
cgitb.enable()

# Send the HTTP header
#print("Content-Type: text/plain;charset=utf-8")
print("Content-Type: text/html;charset=utf-8")
print("")

content = """<p>Height above the ocean in feet: <b>{feet}</b></p>
<p>Speed in miles per hour (mph): <b>{miles}</b></p>
<p>Temperature outside the plane in Fahrenheit: <b>{fahrenheit}</b></p>
 """ 

# Convert values to the american system.
meters = 1100 * 3.28084
speed = 1000 * 0.62137
temp = -50 * 9 / 5 + 32


# Write page content
sys.stdout = codecs.getwriter("utf-8")(sys.stdout.detach())
sys.stdout.write(content.format(feet=meters, miles=speed, fahrenheit=temp))
