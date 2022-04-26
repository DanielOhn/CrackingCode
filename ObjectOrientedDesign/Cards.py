class Cards():
    def __init__(self, suit, value):
        self.suit = suit
        self.value = value

def setCards():
    # Cards have 4 Types
    # Cards go from 2-10, J, Q, K, A 
    suit = ["Club", "Spade", "Heart", "Diamond"]
    value = [2, 3, 4, 5, 6, 7, 8, 9, 10, "Jack", "Queen", "King", "Ace"]
    cards = []
    for i in range(4):
        for j in range(13):
            cards.append(Cards(suit[i], value[j]))

    return cards 

getCards = setCards()

for i in getCards:
    print(i.suit, i.value)

