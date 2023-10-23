from turtle import *
colors = ['red', 'orange', 'yellow', 'green', 'blue']

for j in range(5):
    color(colors[j])
    begin_fill()
    pendown()
    for i in range(5):
        forward(100)
        right(144)
    penup()
    forward(125)
    end_fill()

done()