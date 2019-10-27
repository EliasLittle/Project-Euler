# Card Methods
def suit(card):
    return card[1]


def value(card):
    altVals = {
        'T': 10,
        'J': 11,
        'Q': 12,
        'K': 13,
        'A': 14
    }
    if card[0] in altVals:
        return altVals[card[0]]
    return int(card[0])


def symbol(value):
    altSymbols = {
        10: 'T',
        11: 'J',
        12: 'Q',
        13: 'K',
        14: 'A'
    }
    if value in range(2, 10):
        return str(value)
    return altSymbols[value]


# Outcome class


class Outcome:

    def __init__(self, name='', has=False, rank=0, value=0):
        self.name = name
        self.has = has
        self.rank = rank
        self.value = value


# Hand Rankings
def highValue(hand):
    ordered = sorted(list(map(value, hand)))
    outcome = Outcome('highValue', True, 1, ordered[len(ordered)-1])
    return outcome


def hasnOfAKind(hand, n):
    valHand = list(map(value, hand))
    for val in valHand:
        newHand = [x for x in valHand if x != val]
        if len(newHand) <= len(hand)-n:
            return Outcome('', True, 0, val)
    return Outcome('', False, 0, 0)


def hasPair(hand):
    pair = hasnOfAKind(hand, 2)
    return Outcome('hasPair', pair.has, 2, pair.value)


def hasTwoPair(hand):
    results = hasPair(hand)
    valHand = list(map(value, hand))
    if results.has:
        newHand = [symbol(x) for x in valHand if x != results.value]
        newResults = hasPair(newHand)
        if newResults.has:
            #print("Value 1: ", results.value)
            #print("Value 2: ", newResults.value)
            if newResults.value > results.value:
                greater = newResults.value
            else:
                greater = results.value
            return Outcome('hasTwoPair', True, 3, greater)
    return Outcome('hasTwoPair', False, 0, 0)


def hasThreeOfAKind(hand):
    tri = hasnOfAKind(hand, 3)
    return Outcome('hasThreeOfAKind', tri.has, 4, tri.value)


def hasStraight(hand):
    ordered = sorted(list(map(value, hand)))
    if ordered == list(range(ordered[0], ordered[0]+5)):
        return Outcome('hasStraight', True, 5, ordered[4])
    return Outcome('hasStraight', False, 0, 0)


def hasFlush(hand):
    for card in hand:
        if suit(card) != suit(hand[0]):
            return Outcome('hasFlush', False, 0, 0)
    return Outcome('hasFlush', True, 6, highValue(hand).value)


def hasFullHouse(hand):
    results = hasThreeOfAKind(hand)
    valHand = list(map(value, hand))
    if results.has:
        newResults = hasPair([str(x) for x in valHand if x != results.value])
        if newResults.has:
            return Outcome('hasFullHouse', True, 7, newResults.value)
    return Outcome('hasFullHouse', False, 0, 0)


def hasFourOfAKind(hand):
    quad = hasnOfAKind(hand, 4)
    return Outcome('hasFourOfAKind', quad.has, 8, quad.value)


def hasStraightFlush(hand):
    if hasFlush(hand).has and hasStraight(hand).has:
        return Outcome('hasStraightFlush', True, 9, highValue(hand).value)
    return Outcome('hasStraightFlush', False, 0, 0)


def hasRoyalFlush(hand):
    royalVals = range(10, 15)
    flush = hasFlush(hand)
    if flush.has:
        if list(map(value, hand)) == royalVals:
            outcome = Outcome('hasRoyalFlush', True, 10, 14)
            return outcome
    outcome = Outcome('hasRoyalFlush', False, 0, 0)
    return outcome


file = open(r'/Users/EliasL/Documents/Code/Project Euler/Euler54/Euler54.txt')
games = [line.split(' ') for line in file]
for game in games:
    game[9] = game[9][:2]


funcList = [
    hasRoyalFlush,
    hasStraightFlush,
    hasFourOfAKind,
    hasFullHouse,
    hasFlush,
    hasStraight,
    hasThreeOfAKind,
    hasTwoPair,
    hasPair,
    highValue
]


def test(hand):
    result = []
    for func in funcList:
        outcome = func(hand)
        result.append(outcome)
    return result


player1Wins = 0
player2Wins = 0
totgames = 0


def winner(p1, p2):
    global player1Wins, player2Wins, totgames
    if p1 > p2:
        player1Wins += 1
        totgames += 1
        print("Player 1 wins this round")
        return True
    elif p2 > p1:
        player2Wins += 1
        totgames += 1
        print("Player 2 wins this round")
        return True
    return False


print("BEGIN!")
for game in games:
    print(" ")
    print("Game #: ", str(totgames+1))
    p1hand = []
    p2hand = []

    p1Rank = 0
    p1Value = 0
    p2Rank = 0
    p2Value = 0

    for result in test(game[:5]):
        if result.has:
            p1hand.append(result.name)
            if result.rank > p1Rank:
                p1Rank = result.rank
                p1Value = result.value

    for result in test(game[5:]):
        if result.has:
            p2hand.append(result.name)
            if result.rank > p2Rank:
                p2Rank = result.rank
                p2Value = result.value

    print("P1's Hand: ", p1hand, " : ", p1Value)
    print("P2's Hand: ", p2hand, " : ", p2Value)

    if winner(p1Rank, p2Rank):
        continue
    elif p1Rank == p2Rank and p1Rank != 0:
        #print("Same Rank!")
        if winner(p1Value, p2Value):
            continue
        else:
            #print("Doble Tie!")
            isWinner = False
            p1hand, p2hand = list(map(value, game[:5])), list(
                map(value, game[5:]))
            p1hand.sort()
            p2hand.sort()
            print("p1hand: ", p1hand)
            print("p2hand: ", p2hand)
            i = 4
            while not isWinner and i >= 0:
                if winner(p1hand[i], p2hand[i]):
                    isWinner = True
                else:
                    i -= 1
            if i == 0:
                print("More work?")
    print(" ")

print("Total Games: ", totgames)
print("Player 1 Wins ", player1Wins, " times.")
