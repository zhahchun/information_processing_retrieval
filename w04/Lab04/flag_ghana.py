from turtle import *

### Functions for drawing
# Modify the code in this function

def bar(bar_color):
    color(bar_color)
    begin_fill()
    forward(300)
    left(90)
    forward(50)
    left(90)
    forward(300)
    left(90)
    forward(50)
    left(90)
    end_fill()

### Main code that gets run, to draw the german flag
# Do not modify code below this line for Exercise 7.  It is OK to add code below this for Exercise 8
def star(bar_color):
    color(bar_color)
    begin_fill()
    for i in range(5):
        forward(50/3.077 * 3.2361)
        right(144)
    end_fill()

bar("red")
right(90); forward(50); left(90)
bar("yellow")
right(90); forward(50); left(90)
bar("green")
penup()
left(90); forward(100); right(90); forward(150); right(72)
pendown()
star('black')

done()

    
