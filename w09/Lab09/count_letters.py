
# Main code that counts letters in a string

def count_letters(input_string):
    letters = {}
    for letter in input_string:
        letters.setdefault(letter, 0)
        letters[letter] += 1
    return letters
        

# Code to test the count_letters function
def test_count_letters01():
    result = []
    letters = count_letters('HI')
    for k, v in letters.items():
        result.append(v)
    
    assert result == [1, 1]

def test_count_letters02():
    result = []
    letters = count_letters('akshay')
    for k, v in letters.items():
        result.append(v)
    
    assert result == [2, 1, 1, 1, 1]

def test_count_letters03():
    result = []
    letters = count_letters('')
    for k, v in letters.items():
        result.append(v)
    
    # assert result == [0]
    assert result == []

def test_count_letters03():
    letters = count_letters('akshay')
    check = {'a': 2, 'k': 1, 's': 1, 'h':1, 'y': 1, 'z': 1}
    for k, v in check.items():
        assert k in letters



