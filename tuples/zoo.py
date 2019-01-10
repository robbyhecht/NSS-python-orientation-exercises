# make tuple
zoo = ("dog", "giraffe", "aracari", "bearded dragon lizard")

# find index of an animal
aracari = zoo.index("aracari")
print(aracari)

# use value to determine if an animal is included

print(zoo.index("bearded dragon lizard"))

# create variables from animals
(dog, giraffe, aracari, dragon) = zoo
print(dragon)

# convert tuple to a list
zoo_list = list(zoo)
print(zoo_list)

# add animals to list
new_animals = ["gorilla", "monkey", "bear"]
zoo_list.extend(new_animals)
print(zoo_list)

# convert back to tuple
zoo = tuple(zoo_list)
print(zoo)