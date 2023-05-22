import collections

# define card values and types of hands
VALUES = {'2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, 'T': 10, 'J': 11, 'Q': 12, 'K': 13, 'A': 14}
HANDS = {'High Card':1, 'One Pair':2, 'Two Pairs':3, 'Three of a Kind':4, 'Straight':5, 'Flush':6, 'Full House':7, 'Four of a Kind':8, 'Straight Flush':9, 'Royal Flush':10}

def poker_hand_ranking(hand):
    values = [VALUES[card[0]] for card in hand]
    values.sort(reverse=True)
    suits = [card[1] for card in hand]

    same_suit = len(set(suits)) == 1
    sequence = values == list(range(max(values), max(values) - 5, -1))
    card_counts = collections.Counter(values).most_common()

    if same_suit and sequence and max(values) == 14:
        return HANDS['Royal Flush'], values
    elif same_suit and sequence:
        return HANDS['Straight Flush'], values
    elif card_counts[0][1] == 4:
        return HANDS['Four of a Kind'], [card_counts[0][0]] + sorted([v for v in values if v != card_counts[0][0]], reverse=True)
    elif card_counts[0][1] == 3 and card_counts[1][1] == 2:
        return HANDS['Full House'], [card_counts[0][0]]*3 + [card_counts[1][0]]*2
    elif same_suit:
        return HANDS['Flush'], values
    elif sequence:
        return HANDS['Straight'], values
    elif card_counts[0][1] == 3:
        return HANDS['Three of a Kind'], [card_counts[0][0]]*3 + sorted([v for v in values if v != card_counts[0][0]], reverse=True)
    elif card_counts[0][1] == 2 and card_counts[1][1] == 2:
        pair1 = max(card_counts[0][0], card_counts[1][0])
        pair2 = min(card_counts[0][0], card_counts[1][0])
        kicker = [v for v in values if v not in [pair1, pair2]][0]
        return HANDS['Two Pairs'], [pair1]*2 + [pair2]*2 + [kicker]
    elif card_counts[0][1] == 2:
        return HANDS['One Pair'], [card_counts[0][0]]*2 + sorted([v for v in values if v != card_counts[0][0]], reverse=True)
    else:
        return HANDS['High Card'], values

def compare_hands(hand1, hand2):
    rank1, values1 = poker_hand_ranking(hand1)
    rank2, values2 = poker_hand_ranking(hand2)
    # print(hand1, rank1, hand2, rank2)

    if rank1 > rank2:
        return 1
    elif rank1 < rank2:
        return 2
    else:
        for v1, v2 in zip(values1, values2):
            if v1 > v2:
                return 1
            elif v1 < v2:
                return 2
        return 0

with open('poker.txt', 'r') as file:
    lines = file.readlines()

player1_wins = 0
for line in lines:
    cards = line.strip().split(' ')
    hand1 = cards[:5]
    hand2 = cards[5:]
    # print(compare_hands(hand1, hand2))
    if compare_hands(hand1, hand2) == 1:
        player1_wins += 1

print(player1_wins)
