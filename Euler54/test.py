class Outcome:

    def __init__(self, name='', has=False, rank=0, value=0):
        self.name = name
        self.has = has
        self.rank = rank
        self.value = value


def useless(name, has, rank, value):
    return Outcome(name, has, rank, value)


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


def hasStraight(hand):
    ordered = sorted(list(map(value, hand)))
    if ordered == list(range(ordered[0], ordered[0]+5)):
        return Outcome('hasStraight', True, 5, ordered[4])
    return Outcome('hasStraight', False, 0, 0)


print(hasStraight(['6H', '4H', '5C', '3H', '2H']).has)
