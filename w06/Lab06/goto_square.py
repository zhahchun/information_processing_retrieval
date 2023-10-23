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
