import read_cards
import fc_helper
count_right = 0
# cards = {'Arkansas': "little rock", 'Montana': 'helena', 'North Dakota': 'bismarck', 'Wyoming': 'cheyenne'}
# cards = read_cards.read_cards('capitals.txt')
# cards = read_cards.read_cards('capitals-all.txt')
cards = read_cards.read_cards('nba_players.txt')

# flashcard("What is the capital of Arkansas? ", "little rock" )
# flashcard("What is the capital of Montana? ", 'helena')
# flashcard("What is the capital of North Dakota? ", 'bismarck')
# flashcard("What is the capital of Wyoming? ", 'cheyenne')
# cards['Wisconsin'] = 'Madison'
# print(cards.keys())

for prompt, answer in cards.items():
    fc_helper.flashcard(prompt, answer)