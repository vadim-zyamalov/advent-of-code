class Hand:
    def __init__(self, hand: str, bid: int, order=list("AKQJT98765432")):
        self.bid = bid
        self.hand = hand
        self.order = order

        self.strength, self.count = self.type()

    def type(self):
        strength = 0
        cards = {}

        for card in self.hand:
            if card not in cards:
                cards[card] = 0
            cards[card] += 1

        match len(cards):
            case 1:
                strength = 7
            case 2:
                strength = 6 if 4 in cards.values() else 5
            case 3:
                strength = 4 if 3 in cards.values() else 3
            case 4:
                strength = 2
            case _:
                strength = 1

        return strength, cards

    def __gt__(self, other):
        if self.strength > other.strength:
            return True
        if self.strength < other.strength:
            return False
        for i in range(5):
            si = self.order.index(self.hand[i])
            oi = self.order.index(other.hand[i])
            if si < oi:
                return True
            if si > oi:
                return False
        return False

    def __lt__(self, other):
        if self.strength < other.strength:
            return True
        if self.strength > other.strength:
            return False
        for i in range(5):
            si = self.order.index(self.hand[i])
            oi = self.order.index(other.hand[i])
            print(si, oi)
            if si > oi:
                return True
            if si < oi:
                return False
        return False

    def __eq__(self, other):
        return self.hand == other.hand

    def __ge__(self, other):
        return (self == other) or (self > other)

    def __le__(self, other):
        return (self == other) or (self < other)

    def __ne__(self, other):
        return not (self == other)

    def __str__(self):
        return f"{self.hand}/{self.bid}/{self.strength}"

    def __repr__(self):
        return self.__str__()


if __name__ == "__main__":
    cards = []
    with open("_inputs/2023/day-07/input.txt", "r", encoding="utf8") as f:
        for line in f:
            line = line.strip()
            if line == "":
                break

            hand, bid = line.split()

            cards.append(Hand(hand.strip(), int(bid.strip())))

    res = 0
    i = 1
    prev = None
    for hand in sorted(cards):
        res += i * hand.bid
        if (prev is None) or (prev != hand):
            i += 1
        prev = hand

    print(sorted(cards))
    print(f"Part 1: {res}")
