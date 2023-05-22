from enum import Enum
import urllib.request

class Card:
    value_mapping = {str(i): i for i in range(2, 10)}
    value_mapping.update({'T': 10, 'J': 11, 'Q': 12, 'K': 13, 'A': 14})

    def __init__(self, card):
        self.value = self.value_mapping[card[0]]
        self.suit = card[1]

class Hand:
    def __init__(self, cards):
        self.cards = sorted(cards, key=lambda x: x.value, reverse=True)
        self.rank = self.get_rank()

    def get_rank(self):
        values = [card.value for card in self.cards]
        suits = [card.suit for card in self.cards]
        is_flush = len(set(suits)) == 1
        is_straight = len(set(values)) == 5 and max(values) - min(values) == 4
        counts = {value: values.count(value) for value in values}

        if is_straight and is_flush and max(values) == 14:
            return (9, max(values))
        if is_straight and is_flush:
            return (8, max(values))
        if 4 in counts.values():
            return (7, self.get_key(counts, 4))
        if 3 in counts.values() and 2 in counts.values():
            return (6, self.get_key(counts, 3), self.get_key(counts, 2))
        if is_flush:
            return (5,) + tuple(values)
        if is_straight:
            return (4, max(values))
        if 3 in counts.values():
            return (3, self.get_key(counts, 3)) + tuple(sorted((k for k, v in counts.items() if v!=3), reverse=True))
        if list(counts.values()).count(2) == 2:
            return (2, sorted((k for k, v in counts.items() if v==2), reverse=True)[0]) + tuple(sorted((k for k, v in counts.items() if v!=2), reverse=True))
        if 2 in counts.values():
            return (1, self.get_key(counts, 2)) + tuple(sorted((k for k, v in counts.items() if v!=2), reverse=True))
        return (0,) + tuple(values)

    def get_key(self, dict, value):
        return next((k for k, v in dict.items() if v==value), None)

def solve_poker_problem(file_url):
    with urllib.request.urlopen(file_url) as f:
        hands = f.read().decode().split('\n')
    player1_wins = 0
    for hand in hands:
        if hand == '':
            continue
        cards = hand.split(' ')
        player1 = Hand([Card(card) for card in cards[:5]])
        player2 = Hand([Card(card) for card in cards[5:]])
        if player1.rank > player2.rank:
            player1_wins += 1
    return player1_wins

# Use the function with the URL of the file
# e.g., solve_poker_problem('https://projecteuler.net/project/resources/p054_poker.txt')
wins = solve_poker_problem('https://projecteuler.net/project/resources/p054_poker.txt')
print(wins)