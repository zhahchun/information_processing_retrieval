from turtle import *
import ttt_backend
import ttt_frontend

def take_turn(board, current_player):
    #prompt player
    while True:
        while True:
            row_no = int(numinput("row",  current_player+ "-Enter row number that is no greater than 2: "))
            if row_no <= 2:
                break
        while True:
            col_no = int(numinput("column", current_player+"-Enter column number that is no greater than 2:"))
            if col_no <= 2:
                break
        if not ttt_backend.contains_piece(row_no, col_no, board):
            break
    #X player goes
    if current_player == 'P1':
        ttt_backend.add_piece(row_no,col_no,'x', board)
        ttt_frontend.draw(row_no,col_no,'X')
    #O player goes
    elif current_player == 'P2':
        ttt_backend.add_piece(row_no,col_no,'o', board)
        ttt_frontend.draw(row_no,col_no,'O')
    #check win condition every turn
    if (ttt_backend.validate_win(board)):
               print(current_player, "wins!")
               return 'done'
    #switch player
    if current_player == 'P1':
        return 'P2'
    else:
        return 'P1'

#driver code for the game
def play_game():
    #create a board object
    board = ttt_backend.initialize_board()
    speed(0)  
    #draw board in turtle
    ttt_frontend.draw_board()
    #start with player 1 
    current_player ='P1'
    while (True):
           #take turns until tie or player wins2
           current_player = take_turn(board, current_player)
           if current_player == 'done':
               break
        
#main
play_game()
done()
