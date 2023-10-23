from turtle import *


def title():
    # set up title words
    write("WELCOME TO DYLAN's CONCERT! ROCK & ROLL!",font=('Arial', 20, 'normal'))
    speed(0)
    penup()
    right(90)
    forward(5)
    left(90)
    pendown()
    # draw underline
    pensize(5)
    forward(650)
    # move to the next line
    penup()
    left(180)
    forward(650)
    left(90)
    forward(25)
    left(90)
    pensize(1)
    pendown()

def header():
    # write down each header
    write("Name",font=('Arial', 15, 'normal'))
    penup()
    forward(120)
    pendown()
    write("Pronunciation",font=('Arial', 15, 'normal'))
    penup()
    forward(120)
    pendown()
    write("Title",font=('Arial', 15, 'normal'))
    penup()
    forward(120)
    pendown()
    write("Message",font=('Arial', 15, 'normal'))
    penup()
    # move to the next line
    backward(360)
    right(90)
    forward(25)
    left(90)

# move forward and write name
def writeName(guest):
    # name
    pencolor('black')
    write(guest['Name'],font=('Arial', 15, 'normal'))
    penup()
    forward(120)

    #Pronunciation
    write(guest['Pronunciation'],font=('Arial', 15, 'normal'))
    penup()
    forward(120)

    #Title
    write(guest['Title'],font=('Arial', 15, 'normal'))
    penup()
    forward(120)

    # Message
    write(guest['Message'],font=('Arial', 15, 'normal'))
    penup()

    #draw a line
    backward(360)
    pencolor('Red')
    pendown()
    forward(650)
    penup()
    left(180)
    forward(650)
    # move to the next line
    left(90)
    forward(25)
    left(90)
    
penup()
setpos(-300,300)
pendown()
title()
header()
    
def enter_guest():
    guest = {}
   
    guest['Name'] = textinput("Name", "Enter your name: ")
    if guest['Name'].lower() == 'done':
        return guest['Name'].lower()
    guest['Pronunciation'] = textinput("Pronunciation", "Enter your name's pronunciation: ")
    if guest['Pronunciation'].lower() == 'done':
        return guest['Pronunciation'].lower()
    guest['Title'] = textinput("Title", "Enter your title (Mr, Mrs. Dr. etc): ")
    if guest['Title'].lower() == 'done':
        return guest['Title'].lower()
    guest['Message'] = textinput("Name", "Enter a message: ")
    if guest['Message'].lower() == 'done':
        return guest['Message'].lower()
    
    return guest

#run program
while True:
    # if (writeName("Please enter your name. Enter \'Done\' to exit: ").lower() == 'done'):
    #     break
    guest = enter_guest()
    if(guest == 'done'):
        done()
    else:
        writeName(guest)

done()
