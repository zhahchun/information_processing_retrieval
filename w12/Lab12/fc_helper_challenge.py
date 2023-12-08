def flashcard(prompt, expected_answer):
    # answer = input('What is the capital of ' + prompt + '? ')
    answer = input('What is the nba team of' + prompt + '? ')

    if answer.lower() == expected_answer.lower():
        print("Correct!")
        return 1
    else:
        print("Sorry, that is wrong....")
        return 0