from turtle import *

### Function that draws stars of different sizes

def star(size, star_color):
    fillcolor(star_color)
    begin_fill()
    for i in range(5):
        forward(size)
        right(144)
    end_fill()


### Main code area


done()

