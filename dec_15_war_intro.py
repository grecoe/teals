import random

# Face value of cards
card_values = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
# Clubs, Spades, Diamonds, Hearts
card_suit = ['\u2663', '\u2660', '\u2666', '\u2665']

# Indexes to player list
PLAYER_1 = 0
PLAYER_2 = 1

# Indexes to card list
CARD_WEIGHT = 0
CARD_FACE = 1
CARD_SUIT = 2


def build_deck(shuffle_count=7):
    """
        Build a deck of 52 cards and shuffle them
        for a game.

        Parameters:
        shuffle_count:
            int - Number of times to shuffle

        Returns:
            List of cards where a card is a list of
                [weight, face, suit]
    """
    # Build the deck by adding in each value with each suit
    deck = []
    for suit in range(len(card_suit)):
        for value in range(len(card_values)):
            card = [value, card_values[value], card_suit[suit]]
            deck.append(card)

    # Now loop through the number of shuffles to mix them up
    for unused_var in range(shuffle_count):
        random.shuffle(deck)

    # Return the deck
    return deck


def deal_cards(deck):
    """
        Provide a full deck (52 cards), and divvy them
        up into two player decks.

        Parameters:
            deck - List of cards

        Returns:
            A list of lists (one for each player)
    """
    # List of lists to hold player cards
    players = [[], []]

    # Split all the cards in the deck between each player
    for card_num in range(len(deck)):
        players[card_num % 2].append(deck[card_num])

    # Return the players decks
    return players


# Create a deck (shuffled)
playing_deck = build_deck()
# Deal the cards out
player_decks = deal_cards(playing_deck)

print("****DECK DETAILS*****")
print("Full Deck Card Count : {}".format(len(playing_deck)))
print("Player Decks:")
print("\tDeck Count: {}".format(len(player_decks)))
print("\tPlayer One Card Count: {}".format(len(player_decks[PLAYER_1])))
print("\tPlayer Two Card Count: {}".format(len(player_decks[PLAYER_2])))
print("****DECK DETAILS*****")


# Play 5 cards from each....and see who won, does not account
# for a tie (War) scenario
for card_idx in range(len(player_decks[PLAYER_1])):
    p1_card = player_decks[PLAYER_1][card_idx]
    p2_card = player_decks[PLAYER_2][card_idx]

    winning_card = p2_card
    if p1_card[CARD_WEIGHT] > p2_card[CARD_WEIGHT]:
        winning_card = p1_card

    print("(P1) {}{} vs. (P2) {}{} == Winner {}{}".format(
        p1_card[CARD_FACE], p1_card[CARD_SUIT],
        p2_card[CARD_FACE], p2_card[CARD_SUIT],
        winning_card[CARD_FACE], winning_card[CARD_SUIT],
    ))
