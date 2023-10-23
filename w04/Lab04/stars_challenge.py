from turtle import *

### Functions
# Modify code in this section

def star(size):
    for i in range(5):
        forward(size)
        right(144)


### The main code that gets run
# Do not modify anything after this line


for i in range(13):
    star(8 + i*2)
    penup()
    right(360/13)
    forward(50)
    pendown()

done()
