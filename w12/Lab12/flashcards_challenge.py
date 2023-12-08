import read_cards
import fc_helper_challenge
import random

cards = read_cards.read_cards('nba_players.txt')

# Challenge 2: Randomize the order of the flashcards
d_keys = list(cards.keys())
random.shuffle(d_keys)
count_right = 0

for prompt in d_keys:
    # Challenge 3: Refactoring – Handling the count correctly
    count_right += fc_helper_challenge.flashcard(prompt, cards[prompt])

print()
print('You provided correct answers for ' + str(count_right) + ' out of the ' + str(len(cards)) + ' quesions.')