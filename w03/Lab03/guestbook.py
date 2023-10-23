from turtle import *

number = textinput("Number", "How many student in the class?")
for i in range(int(number)):
    name = textinput("Name", "Please enter your name")

    write(name)

    penup()
    right(90)
    forward(50)
    left(90)
    pendown()



done()
