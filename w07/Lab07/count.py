
words = {}       # Create a blank dictionary to hold our counts

# Initialize the dictionary to 0 for all of the words
# words.setdefault('duck',0)
# words.setdefault('goose',0)

# phrase = "duck duck goose"
phrase = 'Baby, Im just gonna shake, shake, shake, shake, shake'

# words['duck'] += 1
# words['duck'] += 1
# words['goose'] += 1
new_phrase = phrase.split(',')
part = new_phrase[1].split(' ')
new_phrase.pop(1)
new_phrase = new_phrase + part

for w in new_phrase:
    w = w.strip()
    if w != '':
        words.setdefault(w, 0)
        words[w] += 1

print(words)

# print(new_phrase)

# print(words)
