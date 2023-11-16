
# Main code that prints out a verse of the song


def bottles(n):
    print(n, "bottles of beer on the wall. ", end="")
    print(n, "bottles of beer. ", end="")
    if (n < 10):
        print("If one of those bottles should happen to fall. ", end="")
    else:
        print("Take one down, pass it around. ", end="")
    print(n-1, "bottles of beer on the wall.", end="")

# bottles(10) 
# bottles(8) 

# Code to test the bottles function
def test_bottles01(capsys):
    bottles(10)
    captured = capsys.readouterr()
    assert captured.out == '10 bottles of beer on the wall. 10 bottles of beer. Take one down, pass it around. 9 bottles of beer on the wall.'

def test_bottles02(capsys):
    bottles(8)
    captured = capsys.readouterr()
    assert captured.out == '8 bottles of beer on the wall. 8 bottles of beer. If one of those bottles should happen to fall. 7 bottles of beer on the wall.'





