from turtle import *

### Functions
# Modify code in this section

def star():
    for i in range(5):
        forward(20)
        right(144)


### The main code that gets run
# Do not modify anything after this line

for i in range(13):
    star()
    penup()
    right(360/13)
    forward(50)
    pendown()

done()
