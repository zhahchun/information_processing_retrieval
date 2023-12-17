# creates a board, which is 3x3 array of characters
def initialize_board():
    board = [[None for _ in range(3)] for _ in range(3)]
    return board

#adds a piece to the board
def add_piece(x,y, value, board):
    board[x][y] = value
    return board

#check if the spot contains a piece
def contains_piece(row_no, col_no, board):
    return board[row_no][col_no] != None

#validates a win state
def validate_win(board):
    #check horizontal
    for row in board:
        if ((row[0] == row[1] and row[0] == row[2] and 
            row[1] == row[2] and (row[0] != None and row[1] != None and row[2] != None))): 
            return True
    #check vertical 
    for col in range(3):
        if board[0][col] == board[1][col] and board[0][col] == board[2][col] and board[1][col] == board[2][col] and (board[0][col] != None and board[1][col] != None and board[2][col] != None):
         return True
    #check diagonals
    if board[0][0] == board[1][1] and board[0][0] == board[2][2] and board[1][1] == board[2][2] and (board[0][0] != None and board[1][1] != None and board[2][2] != None) :
        return True
    if board[2][0] == board[1][1] and board[2][0] == board[0][2] and board[1][1] == board[0][2] and (board[2][0] != None and board[1][1] != None and board[0][2] != None):
        return True
    return False