import random

countries = {'Taiwan':'asia', 'the United States':'north america', 'France':'europe', 
			 'Kenya':'africa', 'Australia' : 'oceania'}

capitals = {'Taiwan':'taipei', 'the United States':'washington dc', 'France':'paris', 
		  'Kenya':'nairobi', 'Australia' : 'canberra'} 

country, continent = random.choice(list(countries.items()))

while (True):
	user_answer = input("What is the continent of {}? ".format(country))
	if(user_answer.lower() == continent):
		print("Correct answer\n")
		capital = capitals[country]
		while (True):
			user_answer = input("What is the capital of {}? ".format(country))
			if(user_answer.lower() == capital):
				print("Correct answer\n")
				break
			else:
				print("Wrong answer\n")
		break
	else:
		print("Wrong answer\n")
				
	# option = int(input("enter 0 , if you want to play again : "))
	# if (option):
	# 	break

# print("welcome to country quiz ")

