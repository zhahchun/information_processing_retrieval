from turtle import *

# Square

def square(size, sq_color):
    fillcolor(sq_color)
    begin_fill()
    for i in range(4):
        forward(size)
        right(90)
    end_fill()

def row(number, sq_size, sq_color):
    for i in range(number):
        square(sq_size, sq_color)
        forward(sq_size)
    # pass
    

### Do not modify anything below this line
# Draw board

penup()
goto(-200, 200)
pendown()
square(400, "black")
row(4, 400/4, "red")

done()
