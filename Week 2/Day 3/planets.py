# Saturn is missing from the planet_list
# Insert it into the correct position

planet_list = ["Mercury", "Venus", "Earth", "Mars", "Jupiter", "Uranus", "Neptune"]
# planet_list = planet_list[:5] + ["Saturn"] + planet_list[5:]

planet_list.insert(5, "Saturn")

print(planet_list)