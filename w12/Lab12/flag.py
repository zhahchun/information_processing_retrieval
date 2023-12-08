from turtle import *

speed(9)
def colored_rectangle(stripe_color, width = 300, height = 10):
    color(stripe_color)
    begin_fill()
    forward(width)
    left(90)
    forward(height)
    left(90)
    forward(width)
    left(90)
    forward(height)
    left(90)
    end_fill()

def move_next():
    penup()
    right(90)
    forward(10)
    left(90)
    pendown()