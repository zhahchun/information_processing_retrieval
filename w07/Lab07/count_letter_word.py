
words = {}       # Create a blank dictionary to hold our counts
letters = {}
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


for letter in song:
# for letter in phrase:
    if letter != ' ':
        # print(letter)
        words.setdefault(letter, 0)
        words[letter] += 1

for word in song.split():
    if word != ' ':
        words.setdefault(word, 0)
        words[word] += 1

# print(words)

for k, v in words.items():
    print(str(k) +': '+ str(v))
