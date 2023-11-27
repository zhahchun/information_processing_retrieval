
words = {}       # Create a blank dictionary to hold our counts

# Initialize the dictionary to 0 for all of the words
words.setdefault('duck',0)
words.setdefault('goose',0)

phrase = "duck duck goose"

words['duck'] += 1
words['duck'] += 1
words['goose'] += 1

print(words)
