from random import randint

CARDS = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]
SUITS = ["♥", "♦", "♠", "♣"]

deck_of_cards = [f"{card}{suit}" for card in CARDS for suit in SUITS]
print(deck_of_cards)

def shuffle_deck(deck_of_cards):  
    length = len(deck_of_cards)

    for _ in range(length):
        random_index = randint(0, length - 1)
        card = deck_of_cards.pop(random_index)
        deck_of_cards.append(card)
    return deck_of_cards

print(deck_of_cards)
print(shuffle_deck(deck_of_cards))










#     for i in range(len(deck_of_cards)):
#         switch_index = randint(0,len(deck_of_cards)-1)
#         temp = deck_of_cards[i]
#         deck_of_cards[i] = deck_of_cards[switch_index]
#         deck_of_cards[switch_index] = temp
#     return deck_of_cards

# print(shuffle_deck(deck_of_cards))