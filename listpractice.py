import numpy as np
empty_list = []
cities = ["Oakland", "New York City", "Seattle", "Memphis", "Miami", "Boston", "Los Angeles", "Denver", "New Orleans"]
print(cities)
US_cities = cities[0:6]
print(US_cities)
cities[0] = "San Fransisco"
cities[1] = "Brooklyn"
cities[6] = "Hollywood"
cities[5] = "Tampa"
print(US_cities)
print(cities)
cities.sort()
print(cities)
cities.sort(key=len)
print(cities)

favorite_food = ["pizza", "chicken sandwich", "blueberries", "watermelon", "cherries", "coffee", "milkshake", "popcorn", "bagel", "ginger ale"]
print(favorite_food)
threefaves = favorite_food[0:3]
print(threefaves)


listnumbers = []
size = 5
for i in range(size):
    listnumbers.append(10*np.random.random())
print(listnumbers)
listnumbers.sort() 
print(listnumbers)      
i=1

#pop, remove, clear
#append, extend, insert

