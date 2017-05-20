#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Code that calculates various information about an airplane.

"""

# Request input from the user.
meters = input("Enter your height above the ocean in meters:")
speed = input("Enter your speed in km/h:")
temp = input("Enter the temperature outside the plane in Celsius:")

# Convert user input to the american system.
meters = float(meters) * 3.28084
speed = float(speed) * 0.62137
temp = float(temp) * 9 / 5 + 32

# Print the converted values.
print("Height above the ocean in feet: " + str(meters))
print("Speed in miles per hour (mph): " + str(speed))
print("Temperature outside the plane in Fahrenheit: " + str(temp))
