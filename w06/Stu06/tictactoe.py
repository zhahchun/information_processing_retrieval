from turtle import *
import math

# creates a board, which is 3x3 array of characters
def initialize_board():
    board = [[None for _ in range(3)] for _ in range(3)]
    return board

#adds a piece to the board
def add_piece(x,y, value, board):
    board[x][y] = value
    return board

#validates a win state
def validate_win(board):
    #check horizontal
    for row in board:
        if row[0] == row[1] and row[0] == row[2] and row[1] == row[2] and (row[0] != None and row[1] != None and row[2] != None): 
           # print("horiz")
            return True
    #check vertical 
    for col in range(3):
        if board[0][col] == board[1][col] and board[0][col] == board[2][col] and board[1][col] == board[2][col] and (board[0][col] != None and board[1][col] != None and board[2][col] != None):
         #print("vert")
         return True
    #check diagonal
    if board[0][0] == board[1][1] and board[0][0] == board[2][2] and board[1][1] == board[2][2] and (board[0][0] != None and board[1][1] != None and board[2][2] != None) :
        #print("diag1")
        return True
    if board[2][0] == board[1][1] and board[2][0] == board[0][2] and board[1][1] == board[0][2] and (board[2][0] != None and board[1][1] != None and board[0][2] != None):
        #print("diag2")
        return True
    return False

speed(0)

# draw the empty board
def draw_board():
    forward_len = 0
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
    goto(0,0)


# draw the "O" or "X"
def draw(row, column, option):
    if(option == "O"):
        # draw an "O"
        draw_o(row, column)
        
    elif(option == "X"):
        # draw an "X"
        draw_x(row, column)

def draw_x(y, x):
    goto(0,0)
    x_len = (x) * 100
    y_len = (y) * 100
    penup()
    setheading(0)
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


def draw_o(y, x):
    goto(0,0)
    x_len = (x) * 100
    y_len = (y+1) * 100
    penup()
    setheading(0)
    forward(x_len)
    right(90)
    forward(y_len)
    left(90)
    forward(50)
    # draw x
    pendown()
    circle(50)
    penup()
    setheading(0)
    goto(0,0)

# for testing
draw_board()
# draw_x(1,1)
# draw_o(0,0)

def contains_piece(x, y, board):
    return board[x][y] != None

def take_turn(board, current_player):
    #prompt player
    while True:
        row_no = int(numinput("row",  current_player+ "-Enter row number that is no greater than 2: "))

        col_no = int(numinput("column", current_player+"-Enter column number that is no greater than 2:"))
        
        if row_no <= 2 and col_no <= 2 and not contains_piece(row_no, col_no, board):
            break
    if current_player == 'P1':
        add_piece(row_no,col_no,'x', board)
        draw_x(row_no,col_no)
    elif current_player == 'P2':
        add_piece(row_no,col_no,'o', board)
        draw_o(row_no,col_no)
    if (validate_win(board)):
               print(current_player, "wins!")
               return 'done'
    if current_player == 'P1':
        return 'P2'
    else:
        return 'P1'

def play_game():
    board = initialize_board()
    current_player ='P1'
    while (True):
           current_player = take_turn(board, current_player)
           if current_player == 'done':
               break
           
play_game()
done()
