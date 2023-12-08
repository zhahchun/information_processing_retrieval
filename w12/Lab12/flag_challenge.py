from turtle import *

def stripe(stripe_color, width = 300, height = 10): # Challenge 1: More Refactoring of the flag
    colored_rectangle(stripe_color, width , height)
    move_next()

def colored_rectangle(stripe_color, width = 300, height = 10):
    color(stripe_color)
    begin_fill()
    for i in range(2):
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