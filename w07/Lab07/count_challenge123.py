
words = {}       # Create a blank dictionary to hold our counts

# phrase = 'Baby, Im just gonna shake, shake, shake, shake, shake'
song = """
‘Cause the players gonna play, play, play, play, play
And the haters gonna hate, hate, hate, hate, hate
Baby, I’m just gonna shake, shake, shake, shake, shake
I shake it off, I shake it off
Heartbreakers gonna break, break, break, break, break
And the fakers gonna fake, fake, fake, fake, fake
Baby, I’m just gonna shake, shake, shake, shake, shake
I shake it off, I shake it off

I shake it off, I shake it off
I, I shake it off, I shake it off
I, I shake it off, I shake it off
I, I shake it off, I shake it off
"""
song = song.replace(',', '')
song = song.replace('‘', '')
song = song.replace('’', '')
# print(song)

# for letter in song:
# # for letter in phrase:
#     if letter != ' ':
#         # print(letter)
#         words.setdefault(letter, 0)
#         words[letter] += 1

for word in song.split():
    if word != ' ':
        if word != 'I':
            word = word.lower()
        words.setdefault(word, 0)
        words[word] += 1

del words['the']
# print(sorted(words, reverse=True))
print(words)

# for k, v in words.items():
#     print(str(k) +': '+ str(v))

for key in sorted(words, key=words.get, reverse=True):
    print('The most common word in the song is:', key)
    break
