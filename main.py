from random import randint

CARDS = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]
SUITS = ["♥", "♦", "♠", "♣"]

deck_of_cards = [f"{card}{suit}" for card in CARDS for suit in SUITS]

# Implement a solution for shuffling a deck of cards
# Use only randint() and no other imports
def shuffle_deck(deck):
    for i in range(len(deck_of_cards)):
        switch_index = randint(0,len(deck_of_cards)-1)
        temp = deck_of_cards[i]
        deck_of_cards[i] = deck_of_cards[switch_index]
        deck_of_cards[switch_index] = temp
    return deck_of_cards

print(shuffle_deck(deck_of_cards))