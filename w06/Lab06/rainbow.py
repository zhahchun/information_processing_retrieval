from turtle import *

def next_color(current_color):
    if current_color == 'red':
        return 'orange'
    elif current_color == 'orange':
        return 'yellow'
    elif current_color == 'yellow':
        return 'green'
    elif current_color == 'green':
        return 'cyan'
    elif current_color == 'cyan':
        return 'blue'
    elif current_color == 'blue':
        return 'violet'
    elif current_color == 'violet':
        return 'red'

speed(0)
### Do not modify anything below this line

def bar(bar_color):
    color(bar_color)
    begin_fill()
    forward(200)
    right(90)
    forward(30)
    right(90)
    forward(200)
    right(90)
    forward(30)
    right(90)
    end_fill()

### Main code that draws a rainbow

rainbow_color = "red"
for i in range(7):
    bar(rainbow_color)
    right(90); forward(30); left(90)
    rainbow_color = next_color(rainbow_color)

done()
    
