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

bar("black")
right(90); forward(50); left(90)
bar("red")
right(90); forward(50); left(90)
bar("yellow")
# left(90); forward(50); right(90)

done()

    
