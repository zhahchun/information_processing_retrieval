import random
restaurants = []
number = input('How many places are you thinking about for lunch? ')

for i in range(int(number)):
    place = input("Enter the name of restuarant " + str(i+1) + ": ")
    restaurants.append(place)

print('You should go to ', random.choice(restaurants), '.')
