# APPEND

planet_list = ["Mercury", "Mars"]
planet_list.append("Jupiter")
planet_list.append("Saturn")
print(planet_list)

# EXTEND

last_planets = ["Uranus", "Neptune"]
planet_list.extend(last_planets)
print(planet_list)

#INSERT

planet_list.insert(1, "Venus")
planet_list.insert(2, "Earth")
print(planet_list)

#APPEND AGAIN

planet_list.append("Pluto")
print(planet_list)

#SLICE

rocky_planets = planet_list[0:4]
print(rocky_planets)

#DEL

del planet_list[8]
print(planet_list)

#CHALLENGE - 1. Create another list containing tuples each with  a spaceship and planets visited 2. Iterate over the planets and trips and print planets with the ships that have visited them.

space_ships = [("Falcon", "Earth", "Mars"), ("Rocket_Man", "Saturn", "Neptune", "Uranus", "Earth"), ("Hal", "Mercury", "Venus")]

for planet in planet_list:
  for trip in space_ships:
    if planet in trip:
      print(f'{planet} was visited by {trip[0]}')