"""
In the card game poker, a hand consists of five cards and are ranked, from lowest to highest, in the following way:

...
The file, poker.txt, contains one-thousand random hands dealt to two players. Each line of the file contains ten cards (separated by a single space): the first five are Player 1's cards and the last five are Player 2's cards. You can assume that all hands are valid (no invalid characters or repeated cards), each player's hand is in no specific order, and in each hand there is a clear winner.

How many hands does Player 1 win?
"""

cardvalues = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K', 'A']

def value(card):
    return cardvalues.index(card[0])

def values(hand):
    return [value(c) for c in hand]

def suit(card):
    return card[1]

def suits(hand):
    return [suit(card) for card in hand]

def highCard(hand):
    return max(values(hand))

def countValues(card, hand):
    return sum(1 if value(c) == value(card) else 0 for c in hand)

def fullHouse(hand):
    for card in hand:
        v = set(values(hand))
        v.remove(value(card))
        if countValues(card, hand) == 3 and len(v) == 1:
            return value(card)
    return False

def fourOfAKind(hand):
    for card in hand:
       if countValues(card, hand) == 4:
            return value(card)
    return False

def threeOfAKind(hand):
    for card in hand:
       if countValues(card, hand) == 3:
            return value(card)
    return False

def flush(hand):
    if len(set(suits(hand))) == 1:
        return hand[0][0]
    else:
        return False

def straight(hand):
    v = sorted(values(hand))
    if all(value in v for value in range(v[0], v[0] + 5)):
        return v[4]
    else:
        return False

def twoPairs(hand):
    for card in hand:
       if countValues(card, hand) == 1:
           v = set(values(hand))
           v.remove(value(card))
           hand1 = hand[:]
           hand1.remove(card)
           if len(v) == 2 and not threeOfAKind(hand1):
               return max(v)
    return False

def onePair(hand):
    for card in hand:
       if countValues(card, hand) == 2:
           return value(card)
    return False

def straightFlush(hand):
    if flush(hand) and len(set(suits(hand))) == 1:
        return(max(values(hand)))
    else:
        return False    

def royalFlush(hand):
    if straightFlush(hand) and max(values(hand)) == len(cardvalues)-1:
        return len(cardvalues)-1
    else:
        return False

tests = [royalFlush, straightFlush, fourOfAKind, fullHouse, flush, straight, threeOfAKind, twoPairs, onePair, highCard]
    
def win(cards):
    for test in tests:
        test1 = test(cards[:5])
        test2 = test(cards[5:])
        if test1 and not test2 or test1 and test1 > test2:
            return 1
        if test2:
            return 0

wins = 0
for cards in open("Problem054.txt"):
    wins += win(cards.split())
print(wins)
