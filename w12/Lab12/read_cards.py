
def read_cards(filename):
    cards = {}
    with open(filename, "r") as f:
        for line in f:
            line = line.strip()
            if line == "":
                break
            parts = line.split(",")
            cards[parts[1]] = parts[0]
    return cards
