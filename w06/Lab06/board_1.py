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
    
### Do not edit below this line
# Draw board

penup()
goto(-200, 200)
pendown()
square(400, "red")

done()
