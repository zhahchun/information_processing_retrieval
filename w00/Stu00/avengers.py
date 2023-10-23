# The Avengers -- an Adventure program

print("Thor, Iron Man, Black Widow, and Captain America are all sitting around a room.  The other Avengers are also somewhere nearby.")
print("As they are talking, Iron Man says 'Thor, I bet I can lift your hammer!'")
print("'I'd like to see you try!' Thor responds")
print("Captain America looks skeptical.  'Its not a good idea to mess with Thor's hammer' he says")
print("")
person = input("Who will first try to pick up Thor's hammer? ")

if (person == "Thor") or (person == "thor"):
  print("Thor walks over to the hammer and reaches down to pick it up.")
  print("'Of course, it is as light as paper for me' he brags.  'I am righteous; I can always pick it up'")
  print("")
  pickup = input("Does Thor pick up the hammer? ")
  
  if (pickup == "Yes") or (pickup == "yes"):
    print("Thor picks up the hammer and throws it at Iron Man.  Iron man is stuck under the weight of it")
    print("'Get this thing off of me!' he says.")
    print("Once Thor picks it up, Iron Man blasts him.  Which, of course, causes Thor to drop the hammer right back on top of Iron Man.")
  else:
    print("'I am a God.  I don't need to prove anything' says Thor.")
    print("Iron man looks down at him. 'You can't lift it.  I knew it!' he says.")
    print("Captain America walks over to the hammer, picks it up, and throws it to Thor.")
    print("'Yup, really is light as a feather' he says.")
    
elif (person == "Iron Man") or (person == "iron man") or (person == "tony"):
  print("Iron man walks over the hammer and grabs the handle.  He pulls, and nothing happens.")
  print("He pulls harder. Nothing happens.  He uses the blaster to give him more leverage.  Still nothing.")
  print("'This is old version of my suit.  The next version will be able to lift it.'")
  print("Captain America just rolls his eyes.")

elif (person == "Captain America") or (person == "captain america") or (person == "cap"):
  print("Of course I can, I am the Captain!")

elif (person == "Black Widow"):
  print("Yeah let me lift it. It probably weighs nothing.")
  print("I knew this would be easy!")

else:
  print("That's not a person!")
