from turtle import *

# Square

def square(size, sq_color):
    color(sq_color)
    begin_fill()
    for i in range(4):
        forward(size)
        right(90)
    end_fill()
    # pass

def next_color(current_color):
    if current_color == 'red':
        return 'orange'
    elif current_color == 'orange':
        return 'yellow'
    elif current_color == 'yellow':
        return 'green'
    elif current_color == 'green':
        return 'cyan'
    elif current_color == 'cyan':
        return 'blue'
    elif current_color == 'blue':
        return 'violet'
    elif current_color == 'violet':
        return 'red'
    

# For Exercise 5, Only modify this function
# This function draws a row of squares.  `number` is the number of squares across it should draw. Each square is of size sq_size.
# The colors start with sq_color, and then should be chosen by next_color()
def row(number, sq_size, sq_color):
    for i in range(number):
        square(sq_size, sq_color)
        forward(sq_size)
        sq_color = next_color(sq_color)
    
speed(0)
#### Do not modify anything below this line before Exercise 8
# Draw board

penup()
goto(-200, 200)
pendown()
square(400, "black")
first_color = "red"
for i in range(8):
    row(8, 400/8, first_color)
    first_color = next_color(first_color)

    penup()
    back(400)
    right(90)
    forward(400/8)
    left(90)
    pendown()

penup()
goto(-200, 200)
pendown()






done()
