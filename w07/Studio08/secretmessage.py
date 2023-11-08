message = """ 
hnronxttfao fi x lrnt rl knbxvfdb bphnbiifra. 
hnronxttfao fi x vrrz, tske zfqb xa xnvfiv unsie rn x vd kxtbnx. 
fv kraivnxfai gexv yrs kxa cr knbxvfdbzy, 
usv xzir knbxvbi txay abg rhhrnvsafvfbi lrn favbnxkvfdb bphnbiifra.
"""

def replaceLetter(messsage):
    message_current = message
    message_list = []
    letter_list = []
    while True:
        print("""Commands: 'undo' to undo the last letter entered, 'reset' to reset the message, 'done' to quit""")
        print("Current message:",message_current)
        print("Letters replaced: ", letter_list)
        oldLetter = input("What letter do you want to replace? ")
        if oldLetter.lower() == 'undo':
            print("Undoing last move")
            print()
            try:
                message_current = message_list.pop()
                letter_list.pop()
            except:
                print("Error: no moves to undo. ")
                print()
                continue
            continue
        if oldLetter.lower() == 'done':
            print("Goodbye")
            print()
            break
        if oldLetter.lower() =='reset':
            message_current = message
            message_list = []
            letter_list = []
            print("Resetting")
            print()
            continue
        if oldLetter not in message_current:
            print("That letter is not in the message. ")
            print()
            continue
        newLetter = input("What letter do you want to replace it with? ")
        if newLetter.lower() == 'undo':
            print("Undoing last move")
            print()
            try:
                message_current = message_list.pop()
                letter_list.pop()
            except:
                print("Error: no moves to undo. ")
                print()
            continue
        if newLetter.lower() == 'done':
            print("Goodbye")
            print()
            break
        if newLetter.lower() =='reset':
            message_current = message
            message_list = []
            letter_list = []
            print("Resetting")
            print()
            continue
        print("Replacing",oldLetter,"with",newLetter)
        print()
        message_list.append(message_current)
        letter_list.append(oldLetter)

        message_current = message_current.replace(oldLetter, newLetter.upper())
        count_letters(message_current)
        
        
def count_letters(msg):
    letter_frequency = {}
    for letter in msg:
        if(letter not in letter_frequency):
            letter_frequency[letter] = 1
        else:
            letter_frequency[letter] += 1
    
    # print(sorted(letter_frequency, key=letter_frequency.get, reverse= True))
    print('[Letter Frequency]', end=' ')
    for item in sorted(letter_frequency, key=letter_frequency.get, reverse= True):
        print(repr(item),":",letter_frequency[item], end=', ')
    print()

#run code
replaceLetter(message)