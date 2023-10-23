user_name = input("Hey, What's your name:? ")
print("Hi", user_name, "Welcome to Hogwards School of Witchcraft and Wizardry") 
print("The Sorting Ceremony will take place in a few minutes in front of the rest of the school.\n")

while True:
    character_name =input("Which character you want to sort in respective houses: Harry Potter, Luna Lovegood, Draco Malfoy, Cedric Diggory? ")
    print("")
    if (character_name == "Harry Potter" or character_name == "harry potter"):
        print("Sorting Cap: Hmm. Difficult. Very difficult. Plenty of courage, I see. Not a bad mind either. There's talent, my goodness, yes — and a nice thirst to prove yourself, now that's interesting... So where shall I put you? Not Slytherin, eh? Are you sure? You could be great, you know, it's all here in your head, and Slytherin will help you on the way to greatness, no doubt about that — no? Well, if you're sure — better be GRYFFINDOR!\n")
    elif (character_name == "Luna Lovegood" or character_name == "luna lovegood"):
        print("Sorting Cap: This one seems an easy one. Open-minded with a dreamy disposition and a distinct flair for fashion. Transmits an aura of distinct dottiness. Honest and loyal. Very brave , and not scared to risk her own safety and even life to help her friends. I choose Ravenclaw!\n")
    elif (character_name == "Draco Malfoy" or character_name == "draco malfoy"):
        print("Sorting Cap: 'I know exactly where to put you'")
        print("Draco Malfoy: 'I hate Gryffindor, I want Slytherin!'")
        print("Sorting Cap: 'Slyytherinnnnn'\n")
    elif (character_name == "Cedric Diggory" or character_name == "cedric diggory"):
        print("Sorting Cap: I think I wil put you in HUFFLEPUFF!!\n")
    else:
        print("The charater name is not correct\n")
        continue

#     question1 = input("Do you want to proceed ahead with the next event?")
    question1 = input("Do you want to change the character? ")
    if question1 == 'No' or question1 == 'no':
        print("")
        break

question2 = input("\nDo you want to proceed ahead with the next event? ")   
if(question2 == "Yes" or question2 == "yes"):
    print("\nHere we go with the second event")

else:
    print("\nGreat, Goodbye, Have a good day.")