planets = ["Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune"]

print("The first planet is", planets[0])
print("The second planet is", planets[1])
print("The third planet is", planets[2])

# Output
# The first planet is Mercury
# The second planet is Venus
# The third planet is Earth

planets[3] = "Red Planet"
print("Mars is also known as", planets[3])

# Output
# Mars is also known as Red Planet

number_of_planets = len(planets)
print(f"The number of planets is {number_of_planets}")
 
# ADD VALUES TO LISTS
planets.append("Pluto")
number_of_planets = len(planets)
print("There are actually", number_of_planets, "planets in the solar system.")

# Remove last value from lists
last_planet=planets.pop()
print(last_planet)


# Find Value in lists
find = planets.index("Jupiter")
print(find)

# Max and Min in Lists
gravity_on_planets = [0.378, 0.907, 1, 0.377, 2.36, 0.916, 0.889, 1.12]
bus_weight = 12650 # in kilograms, on Earth

print("On Earth, a double-decker bus weighs", bus_weight, "kg")
print("The lightest a bus would be in the solar system is", bus_weight * min(gravity_on_planets), "kg")
print("The heaviest a bus would be in the solar system is", bus_weight * max(gravity_on_planets), "kg")

# Output
# On Earth, a double-decker bus weighs 12650 kg
# The lightest a bus would be in the solar system is 4769.05 kg
# The heaviest a bus would be in the solar system is 29854 kg

# Slicing in Python
planets_before_earth = planets[0:2]
print(planets_before_earth)
#  A slice creates a new list.

# Join Lists
amalthea_group = ["Metis", "Adrastea", "Amalthea", "Thebe"]
galilean_moons = ["Io", "Europa", "Ganymede", "Callisto"]

regular_satellite_moons = amalthea_group + galilean_moons
print("The regular satellite moons of Jupiter are", regular_satellite_moons)

# Output
# The regular satellite moons of Jupiter are ['Metis', 'Adrastea', 'Amalthea', 'Thebe', 'Io', 'Europa', 'Ganymede', 'Callisto']