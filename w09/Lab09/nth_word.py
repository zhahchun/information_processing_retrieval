
# Function that grabs the first word from a sentence

def nth_word(sentence, n):
    words = sentence.split()
    return words[n]


# Code to test
# Level 0 tests
def test_nth_word00():
    word = nth_word('This is a test', 2)
    assert word == 'a'

# Level 1 tests
def test_nth_word01():
    word = nth_word('This is a test', 0)
    assert word == 'This'

def test_nth_word02():
    word = nth_word('This is a test', -1)
    assert word == 'test'

