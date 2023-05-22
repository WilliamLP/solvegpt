import random

class Monopoly:
    def __init__(self, sides=4):
        self.sides = sides
        self.position = 0
        self.doubles = 0
        self.cc_cards = list(range(16))
        self.ch_cards = list(range(16))
        random.shuffle(self.cc_cards)
        random.shuffle(self.ch_cards)
        self.counts = [0]*40

    def roll(self):
        return random.randint(1, self.sides), random.randint(1, self.sides)

    def advance(self, num):
        self.position = (self.position + num) % 40
        if self.position in [2, 17, 33]:  # CC
            self.community_chest()
        elif self.position in [7, 22, 36]:  # CH
            self.chance()
        elif self.position == 30:  # G2J
            self.go_to_jail()

    def go_to_jail(self):
        self.position = 10
        self.doubles = 0

    def community_chest(self):
        card = self.cc_cards.pop(0)
        self.cc_cards.append(card)
        if card == 0:
            self.position = 0
        elif card == 1:
            self.go_to_jail()

    def chance(self):
        card = self.ch_cards.pop(0)
        self.ch_cards.append(card)
        if card == 0:
            self.position = 0
        elif card == 1:
            self.go_to_jail()
        elif card == 2:
            self.position = 11
        elif card == 3:
            self.position = 24
        elif card == 4:
            self.position = 39
        elif card == 5:
            self.position = 5
        elif card == 6 or card == 7:
            while self.position not in [5, 15, 25, 35]:
                self.advance(1)
        elif card == 8:
            while self.position not in [12, 28]:
                self.advance(1)
        elif card == 9:
            self.advance(-3)

    def play(self, rounds=500000):
        for _ in range(rounds):
            die1, die2 = self.roll()
            if die1 == die2:
                self.doubles += 1
                if self.doubles == 3:
                    self.go_to_jail()
                    self.counts[self.position] += 1
                    continue
            else:
                self.doubles = 0
            self.advance(die1 + die2)
            self.counts[self.position] += 1

        results = list(enumerate(self.counts))
        results.sort(key=lambda x: x[1], reverse=True)

        return ''.join(str(x).zfill(2) for x, _ in results[:3])

game = Monopoly()
print(game.play())
