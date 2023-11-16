from turtle import * 
import random


guess_history = [] # list of previously guessed words
NUM_GUESSES = 6 #how many guesses until you lose

def draw_answer(answer):
    penup()
    goto(-130, 150) 
    pendown()
    write("Answer: " + answer, font=("Verdana",50, "normal"))


def draw_result(result):
    penup()
    goto(-130, 200) 
    pendown()
    write(result, font=("Verdana",50, "normal"))

def draw_noose():
    penup()
    goto(-300, 0)
    pendown()
    forward(200)
    backward(100)
    left(90)
    forward(200)
    right(90)
    forward(70)
    right(90)
    forward(30)
    setheading(0)

def draw_man(guess_chance):
    penup()
    if guess_chance == 0:
        goto(-130, 170)
        right(180)
        pendown()
        circle(20)   
    elif guess_chance == 1:
        goto(-130, 130) 
        right(90)
        pendown()
        forward(70)
    elif guess_chance == 2:
        goto(-130, 130) 
        right(135)
        pendown()
        forward(30)
    elif guess_chance == 3:
        goto(-130, 130) 
        right(45)
        pendown()
        forward(30)
    elif guess_chance == 4:
        goto(-130, 60) 
        right(135)
        pendown()
        forward(30)
    elif guess_chance == 5:
        goto(-130, 60) 
        right(45)
        pendown()
        forward(30)
        
    # guess_chance += 1
    setheading(0)
    # return guess_chance

def user_guess_popup():
    guess = textinput('Hangman', 'Please guess a letter to complete the word: ')
    return guess



letter_position = {}
# drawing the frame of word and length is depends on user input
def draw_frame_word(word):
    penup()
    goto(-300,-50) #start position
    
    for item in range(len(word)): # drawing the line
        pendown()
        letter_position[item] = pos()
        forward(40)
        penup()
        forward(10)

# writing the correct letter in the correct place
def write_letter(index, letter):
    penup()
    goto(letter_position[index])
    forward(15) # put the letter in the middle of line
    pendown()
    write(letter, font=("Verdana",30, "normal"))


def isComplete(solution, inProgress):
    word = ""
    for letter in inProgress:
        word += letter
    return word == solution
    
def makeGuesses(word):
    solution = word
    numLetters = len(solution)
    inProgress = list('_'*numLetters)
    incorrect_guesses = 0

    while True:
        # print("word: " + str(inProgress))
        if isComplete(solution, inProgress): # win condition
                draw_result("You Win!")
                # print("you win!")
                break     
        if incorrect_guesses >= NUM_GUESSES: # lose condition
                draw_result("You Lose!")
                draw_answer(word)
                # print("you lose!")
                break
        if len(guess_history) != 0:
            print('You already guess: ' + str(guess_history))
        guess = user_guess_popup()
        if len(guess) != 1:
             print("Error: Input must be a single character")
             continue
        if guess in guess_history:
            print('You already guess: ' + str(guess_history))
            continue
        else: 
            guess_history.append(guess)
        if guess in solution:
            for i in range(numLetters):
                if solution[i] == guess:
                    inProgress[i] = guess
                    write_letter(i, guess)     
        else:
            draw_man(incorrect_guesses)
            incorrect_guesses += 1
            # print("not in word.",(NUM_GUESSES-incorrect_guesses)," guesses remaining")
            
        
def playGame():
    draw_noose()
    
    with open('wordlist.txt', 'r') as words:
        lines = words.readlines()
        word = random.choice(lines).strip()
        # print(word)
        draw_frame_word(word)
        makeGuesses(word)
    done()

playGame()