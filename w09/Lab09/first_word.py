
# Function that grabs the first word from a sentence

def first_word(sentence):
    words = sentence.split()
    return words[0]


# Code to test

def test_first_word():
    word = first_word('This is a test')
    assert word == 'This'
