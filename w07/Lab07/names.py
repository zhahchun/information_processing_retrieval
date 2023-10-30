
# Create an empty dictionary
names = {}


names['Wash'] = 'Rick'
names['Chen'] = 'Mickey'
names['Liu'] = 'Xu'
names['Chen'] = 'Yichun'


while True:
    last_name_user = input("Enter the last name of a student: ")
    first_name_user = input('Enter the first name of that same student: ')
    names[last_name_user] = first_name_user
    
    last_name = input("Enter a student's last name: ")
    # if last_name == "":
    #     # If the user hits enter without entering a name, stop the loop
    #     break
    if last_name in names:
        print("Their first name is", names[last_name])
    else:
        print("I don't know that name")

