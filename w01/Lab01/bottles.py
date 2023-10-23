beverage = "orange juice"
count = 99

for i in range(100):
    print(count, "bottles of", beverage, "on the wall")
    print(count, "bottles of", beverage)
    if(i == 94):
        print("If one of those bottles should happen to fall")
        print(count-1, "bottles of", beverage, "on the wall...")
        print("")
    elif(i != 100):
        print("Take one down, pass it around")
        count = count - 1
        print(count, "bottles of", beverage, "on the wall")
        print("")

    # print(count, "bottles of", beverage, "on the wall")
    # print(count, "bottles of", beverage)
    # print("Take four down, pass it around")
    # count = count - 4
    # print(count, " bottles of", beverage, "on the wall")
    # print("")
    # count = 5    

print("No more bottles of beer on the wall, no more bottles of beer.") 
print("We've taken them down and passed them around; now we're drunk and passed out!")

