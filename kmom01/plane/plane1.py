#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Code that calculates various information about an airplane.

"""

# Convert values to the american system.
meters = 1100 * 3.28084
speed = 1000 * 0.62137
temp = -50 * 9 / 5 + 32

# Print the converted values.
print("Height above the ocean in feet: " + str(meters))
print("Speed in miles per hour (mph): " + str(speed))
print("Temperature outside the plane in Fahrenheit: " + str(temp))
