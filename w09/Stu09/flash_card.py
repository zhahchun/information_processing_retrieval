import random

universities = {'UW Madison': 'Bucky Badger', 'Ohio State University' : 'Brutus Buckeye', 'UCLA': 'Joe Bruin', 'Appalachian State University': 'Yosef', 
				'University of Nebraska-Lincoln': 'Herbie Husker', 'Michigan State University': 'Sparty the Spartan', 
                'University of Iowa' : 'Herky the Hawk', 'University of Maryland': 'Testudo', 'Pennsylvania State University': 'Nittany the Lion',
				'Northwestern University' : 'Willie the Wildcat'}

print("Welcome to Mascot Quiz!")
while (True):
	universitiy = random.choice(list(universities.keys()))
	user_answer = input("What is the mascot of {}? ".format(universitiy))

	if(user_answer.lower() == universities[universitiy].lower()):
		print("Correct answer!\n")
	else:
		print("Wrong answer! The answer is " +  universities[universitiy] + ".\n")
		
	del universities[universitiy]
	if len(universities) == 0:
		break
