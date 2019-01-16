
# PART ONE

# Make a set
showroom = set()
# Add items to the set
showroom.update({"Sonata", "Altima", "Cherokee", "Pinto"})
print(showroom)
# find length of set
print(len(showroom))
# add a duplicate to set - theres still only one of them
showroom.add("Sonata")
print(showroom)
# add another set to the set
showroom.update({"Outback", "Bigfoot"})
print(showroom)
# remove a car from the set
showroom.discard("Outback")
print(showroom)

# PART TWO

# Make new junkyard set
junkyard = set()
# Add cars to the junkyard
junkyard.update({"Elantra", "Odyssey", "Carolina Crusher", "Sonata", "Cherokee"})
print(junkyard)
# Where do they intersect?
print(showroom.intersection(junkyard))
#Combine junkyard and showroom
print(showroom.union(junkyard))

#discard cars from junkyard
cars = junkyard.intersection(showroom)
for car in cars:
  junkyard.discard(car)
print('junkyard= ', junkyard)