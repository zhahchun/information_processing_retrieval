import flag
from turtle import *

speed(0)
for i in range(6):
    flag.colored_rectangle('red')
    flag.move_next()
    flag.colored_rectangle('white')
    flag.move_next()

flag.colored_rectangle('red') 
flag.move_next()

penup()
goto(0, -60)
pendown()
flag.colored_rectangle('blue', 100, 70)

done()
