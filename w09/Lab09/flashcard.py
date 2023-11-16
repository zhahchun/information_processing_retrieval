
# Main code that prints out a flashcard and asks for input

def hobbit_flashcard():
    print("What has roots nobody sees, Is taller than trees, Up, up it goes, And yet never grows?")
    ans = input("Answer? ")
    ans = ans.lower()
    if (ans == "mountain"):
        return "Correct"
    else:
        return "Incorrect"

        
# Code to test the flashcard function

def test_hobbit_flashcard01(monkeypatch):
    monkeypatch.setattr('builtins.input', lambda x: 'mountain')
    result = hobbit_flashcard()
    assert result == 'Correct'

def test_hobbit_flashcard02(monkeypatch):
    monkeypatch.setattr('builtins.input', lambda x: 'flower')
    result = hobbit_flashcard()
    assert result == 'Incorrect'
