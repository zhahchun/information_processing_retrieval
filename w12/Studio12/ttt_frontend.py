from turtle import *
import math

# draw the empty board
def draw_board():
    forward_len = 0
    # draw 3 x 3 table
    for j in range(3):
        for i in range(3):
            forward(100)
            right(90)
            forward(100)
            right(90)
            forward(100)
            right(90)
            forward(100)
            right(90)
            forward(100)
        penup()
        goto(0,0)
        right(90)
        forward_len += 100
        pendown()
        forward(forward_len)
        left(90)
    # go back to initinal position
    goto(0,0)


# draw the "O" or "X"
def draw(y, x, option):
    goto(0,0)

    # draw a "O" inside the column
    if(option == "O"):
        # set right position
        x_len = (x) * 100
        y_len = (y+1) * 100 
        penup()
        setheading(0)
        # go to right position
        forward(x_len)
        right(90)
        forward(y_len)
        left(90)
        forward(50)
        # draw O
        pendown()
        circle(50)

    # draw a "X" inside the column 
    elif(option == "X"): 
        # set right position
        x_len = (x) * 100
        y_len = (y) * 100
        penup()
        setheading(0)
        # go to right position
        forward(x_len)
        right(90)
        forward(y_len)
        # draw x
        left(45)
        pendown()
        forward(math.sqrt(100**2 + 100**2))
        penup()
        left(135)
        forward(100)
        left(135)
        pendown()
        forward(math.sqrt(100**2 + 100**2))
        
    penup()
    setheading(0)
    goto(0,0)
