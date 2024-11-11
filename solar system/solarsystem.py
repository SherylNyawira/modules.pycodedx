# solar_system.py

from math import pi
from random import choice as ch

# List of planets
planets = [
    'Mercury',
    'Venus',
    'Earth',
    'Mars',
    'Saturn'
]

# Select a random planet
random_planet = ch(planets)

# Assign radius based on the planet
if random_planet == 'Mercury':
    r = 2440
elif random_planet == 'Venus':
    r = 6052
elif random_planet == 'Earth':
    r = 6371
elif random_planet == 'Mars':
    r = 3390
elif random_planet == 'Saturn':
    r = 58232
else:
    print("Oops! An error occurred.")
    r = None

# Calculate and print the surface area if the radius was set
if r is not None:
    area = 4 * pi * r**2
    # Print the name of the planet and its surface area, rounded to two decimal places
    print(f"The surface area of {random_planet} is {round(area, 2)} square kilometers.")
