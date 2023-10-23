from turtle import *

def blank_face():
    color('wheat')
    begin_fill()
    circle(radius=50)
    end_fill()
    penup()

def next():
    penup()
    forward(150)
    pendown()

def eyes(shape):
    x, y = pos()
    left(90)
    forward(55)
    left(90)
    forward(30)
    pendown()
    color('black')
    if shape == 'extreme':      
        write('>', font=15)
        penup()
        right(180)
        forward(50)
        pendown()
        write('<', font=15)    

    elif shape == 'bored':
        write('=', font=15)
        penup()
        right(180)
        forward(50)
        pendown()
        write('=', font=15) 

    elif shape == 'rich':
        write('$', font=15)
        penup()
        right(180)
        forward(50)
        pendown()
        write('$', font=15) 

    elif shape == 'confused':
        write('@', font=15)
        penup()
        right(180)
        forward(50)
        pendown()
        write('@', font=15) 
    else: # normal
        write('.', font=15)
        penup()
        right(180)
        forward(50)
        pendown()
        write('.', font=15)  

    penup()
    setx(x)
    sety(y)
    setheading(0)

def mouth(shape):
    x, y = pos()
    left(90)
    forward(25)
    left(90)
    forward(5)
    pendown()
    color('black')
    if shape == 'average':      
        write('_', font=15)

    elif shape == 'sad':
        write('∩', font=20)

    else: # happy
        write('U', font=15)

    penup()
    setx(x)
    sety(y)
    setheading(0)


penup()        
setx(-300)
pendown()
while True:
    input = textinput('Game', 'Do you want to draw your face(yes or no)?  ').lower()
    if input == 'no':
        break
    eyes_user = textinput('Eye', 'What do your eyes look like(normal, extreme, bored, rich, or confused)?  ').lower()
    mouth_user = textinput('Mouth', 'What does your mouth look like(happy, sad, or average)? ').lower()
    blank_face()
    eyes(eyes_user)
    mouth(mouth_user)
    next()

done()