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

# change color
def next_color(current_color):
    if current_color == 'red':
        return 'black'
    elif current_color == 'black':
        return 'red'

# This function draws a row of squares.  `number` is the number of squares across it should draw. Each square is of size sq_size.
# The colors start with sq_color, and then should be chosen by next_color()
def row(number, sq_size, sq_color):
    for i in range(number):
        square(sq_size, sq_color)
        # draw_piece(sq_size/2)
        forward(sq_size)
        sq_color = next_color(sq_color)

# circle
def draw_piece(radius):
    penup()
    forward(radius)
    right(90)
    forward(2 * radius -1)
    left(90)
    pendown()
    color('green')
    begin_fill()
    circle(radius-1)
    end_fill()
    penup()
    left(90)
    forward(radius * 2 -1)
    right(90)
    backward(radius)

# go to certain position on board
def goto_square(x,y, board_size, squares_across):
    x = int(x)
    y = int(y)
    pencolor("red")

    board_x = -200 + (x-1) * (board_size / squares_across)
    board_y = 200 - (y-1) * (board_size / squares_across)
    penup()
    goto(board_x, board_y)
    pendown()

# board
def checkboard(board_size, squares_across, first_color):
    for i in range(squares_across):
        row(squares_across, board_size/squares_across, first_color)
        first_color = next_color(first_color)                                                       

        penup()
        back(board_size)
        right(90)
        forward(board_size/squares_across)
        left(90)
        pendown()

def remove_piece(x, y, board_size, squares_across, first_color):
    goto_square(x, y, board_size, squares_across)
    x = int(x)
    y = int(y)
    if (x+y) % 2 == 0:
        square_color = first_color
    else:
        square_color = next_color(first_color)
    square(board_size/squares_across, square_color)
    
speed(0)
penup()
goto(-200, 200)
pendown()
# square(400, "black")
first_color = "red"
board_size = 400
squares_across = 10
checkboard(board_size, squares_across, first_color)

penup()
x_list = []
y_list = []
while True:
    
    x = textinput('X Axis', 'Enter x cooridinate (empty to stop)): ')
    if x == '':
        break
    y = textinput('Y Axis', 'Enter y cooridinate (empty to stop): ')
    if y == '':
        break
    if x in x_list and y in y_list:
        print('A piece has existed in the position.')
        continue   
    x_list.append(x)
    y_list.append(y)
    penup()
    goto_square(x, y,board_size,squares_across)
    pendown()
    draw_piece(board_size/squares_across/2)
    x = textinput('Remove', 'Which piece do you want to remove? (enter x coordinate): ')
    y = textinput('Remove', 'Which piece do you want to remove? (enter y coordinate): ')
    if x not in x_list and y not in y_list:
        print('No piece is in the position.')
        continue
    x_list.remove(x)
    y_list.remove(y)
    remove_piece(x, y, board_size, squares_across, first_color)
    

done()
