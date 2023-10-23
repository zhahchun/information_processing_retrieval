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
        return 'black'
    elif current_color == 'black':
        return 'red'

# For Exercise 5, Only modify this function
# This function draws a row of squares.  `number` is the number of squares across it should draw. Each square is of size sq_size.
# The colors start with sq_color, and then should be chosen by next_color()
def row(number, sq_size, sq_color):
    for i in range(number):
        square(sq_size, sq_color)
        # draw_piece(sq_size/2)
        forward(sq_size)
        sq_color = next_color(sq_color)


def draw_piece(radius):
    penup()
    forward(radius)
    right(90)
    forward(2 * radius)
    left(90)
    pendown()
    color('green')
    # fillcolor('green')
    begin_fill()
    circle(radius)
    end_fill()
    penup()
    left(90)
    forward(radius * 2)
    right(90)
    backward(radius)

def goto_square(x,y):
    x = int(x)
    y = int(y)
    pencolor("red")
    board_size = 400
    squares_across = 8

    board_x = -200 + (x-1) * (board_size / squares_across)
    board_y = 200 - (y-1) * (board_size / squares_across)
    penup()
    goto(board_x, board_y)
    pendown()

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
# goto(-200, 200)
while True:
    x = textinput('X Axis', 'Enter x cooridinate (empty to stop it)): ')
    if x == '':
        break
    y = textinput('Y Axis', 'Enter y cooridinate (empty to stop it): ')
    if y == '':
        break
    goto_square(x, y)
    pendown()
    draw_piece(400/8/2)


done()
