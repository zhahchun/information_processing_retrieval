import sys
import random
from turtle import *
from random import randrange
input_filename = sys.argv[1]

def count_words_in_file(filename,stoplist):
    word_count = {}
    with open(filename, "r", encoding='utf-8') as f:
        for line in f:
            words = line.split()
            for word in words:
                if word.lower() in stoplist:
                    continue
                elif word.lower() in word_count:
                    word_count[word.lower()] += 1
                else:
                    word_count[word.lower()] = 1
    return word_count

def create_stoplist(stoplist_filepath):
    stoplist = []
    with open(stoplist_filepath, encoding = 'utf-8') as s:
        for line in s:
            stoplist.append(line.strip()) 
        return stoplist

def count_top_50(input_filename, stoplist):
    words = count_words_in_file(input_filename, stoplist)
    top50 = {}
    count = 0
    for key in sorted(words, key = words.get, reverse= True):
        top50[key] = words[key]
        count += 1
        if count == 50:
            return top50

def randomizeDict(my_dict):
    keys = list(my_dict.keys())
    random_keys = random.sample(keys, len(keys))
    random_dict = {}
    for key in random_keys:
        random_dict[key] = my_dict[key]
    return random_dict
    


speed(9)
# dict_freq = {'part': 30, 'cat': 20, 'kokoa': 60, 'giving': 40, 'holiday': 10, 'happy': 200}
def draw_word(dict_freq):
    # change color setting into (r,g,b)
    colormode(255) 

    max_font = max(dict_freq.values()) * 0.5
    penup()
    goto(-600, 200)
    pendown()
    for k in dict_freq:
        # up()
        penup()

        #randomize the color
        color(randrange(255),randrange(255),randrange(255))
        write(k, font=("Arial", int(dict_freq[k] * 0.5) , "normal"), move=True)
        
        # if dict_freq[k] <= 100:
        #     forward(dict_freq[k] * 2.5)
        # elif dict_freq[k] <= 200:
        #     forward(dict_freq[k] * 1.5)
        # else:
        #     forward(dict_freq[k])
        # pendown()
        x, y = pos()
        if x >= 600.0:
            goto(-600, y-max_font)

#main
stoplist = create_stoplist("stoplist.txt")
words = randomizeDict(count_top_50(input_filename, stoplist))

# print(words)
draw_word(words)

done()
