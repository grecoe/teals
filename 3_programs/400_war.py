'''
    Building on one of the labs that doesn't take into account card suit, this 
    extension to the WAR card game is more complete. 
'''
import random

deck = []
shuffledDeck = []

cards = ["2","3","4","5","6","7","8","9","10","J","Q","K","A"]
suits = ["D", "H", "C", "S"]
weights = { "2" : 2,
            "3" : 3,
            "4" : 4,
            "5" : 5,
            "6" : 6,
            "7" : 7,
            "8" : 8,
            "9" : 9,
            "10" : 10,
            "J" : 11,
            "Q" : 12,
            "K" : 13,
            "A" : 14}

class playingCard:
    '''
        playingCard

        This class represents a single card. It's face value, suit and weight. 
    '''
    def __init__(self, cardFace, suit, weight):
        self.face = cardFace
        self.suit = suit
        self.weight = weight
    
    def wins(self, card):
        return self.weight > card.weight

    def getVisual(self):
        return "{}{}".format(self.face, self.suit)

def createDecks(shuffle_count):
    '''
        Create a deck of cards that is shuffled, then split for the two players
    '''
    global cards
    global suits
    global weights
    deck = []
    for suit in suits:
        for card in cards:
            deck.append(playingCard(card, suit, weights[card]))

    for i in range(shuffle_count):
        random.shuffle(deck)

    players = [[],[]]
    for i in range(len(deck)):
        players[i % 2].append(deck[i]) 

    return players   

def doWar(player_deck1, player_deck2, war_count):
    '''
        doWar() function happens when the two players have identical cards. 

        PARAMETERS:
        player_deck1 : List of integers representing a deck of cards for Player 1
        player_deck2 : List of integers representing a deck of cards for Player 1
        war_count    : Integer representing the number of cards that are at risk. 
                       Total cards a player can lose are war_count + 1. The war_count 
                       at risk and one more to see who wins. 

        RETURNS:
        The return of the function is a 3 part tuple that can be accessed just like 
        a list, that is, with indexes. 

        result[0] - Flip card of the first player after flipping the war_count cards
        result[1] - Flip card of the second player after flipping the war_count cards
        result[2] - All of the cards, including the flip cards, that are at risk. 

        NOTES:
        If a player loses because of a forfiet then losers cards are all added to the risk cards.
        Whomever forfiets will have no return flip card, which is a special case to look for.

        If no forfiet happens it is up to the caller to detemine the winner with the return
        results of the call.  

        RULES:
            - If either player does not have enough cards to continue, they forfiet their
              remaining cards to the other (in the risk cards) and end up with an empty deck. 
            - Cards at risk are war_count + 1 for each player. Whomever wins takes all the cards
            - If another war occurs, the function is called recursively until there is a winner
              of the war or someone runs out of cards and forfiets.
    '''
    player1_flip = None
    player2_flip = None
    risk_cards = []

    '''
        Determine if either player does not have enough cards to continue. If so
        move the losers deck onto the winners deck and select one random flip card
        from the winner. 
    '''
    if len(player_deck1) < war_count + 1:
        risk_cards.extend(player_deck1.copy())
        player_deck1.clear()
        player2_flip = player_deck2[-1]
    elif len(player_deck2) < war_count + 1:
        risk_cards.extend(player_deck2.copy())
        player_deck2.clear()
        player1_flip = player_deck1[-1]

    '''
        If there was no forfiet, collect war_count cards from each players
        deck and add them to the risk cards. 

        Next, take the last (top) card from each players deck as the flip card,
        also adding them to the risk cards. 
    '''
    if len(player_deck1) and len(player_deck2):
        '''
            Collect all the at risk cards
        '''
        for i in range(war_count):
            risk_cards.append(player_deck1.pop())
            risk_cards.append(player_deck2.pop())

        '''
            Get the final card they will flip, also added to the risk cards
        '''
        player1_flip = player_deck1.pop()
        player2_flip = player_deck2.pop()
        risk_cards.extend([player1_flip, player2_flip])

    '''
        If the result is that both players have flipped the same card value again, 
        call the function again until one either loses all their cards or there is
        a clear winner in the war. 
    '''
    while player1_flip and player2_flip and (player1_flip.weight == player2_flip.weight):
        print("Continuation War")
        player1_flip, player2_flip, risk = doWar(player_deck1, player_deck2, war_count)
        risk_cards.extend(risk)

    '''
        Return the results of the war. 
    '''
    return player1_flip, player2_flip, risk_cards

def prependCards(deck, cards):
    '''
        We don't want to just add the win cards to the top of the deck, they should be added to 
        the bottom of the deck. To do so, reverse the stack to add so they are prepended in the order
        they were recieved. 
    '''
    cards.reverse()
    for card in cards:
        deck.insert(0,card)
 
'''
    Game play.

    Add in a max turns because sometimes it just doesn't get there quickly. 
'''
# Create the player decks
players = createDecks(7)
# Track number of turns
turns = 0
# Artificial limit in case there are no winners by this number
max_turns = 4000

while len(players[0]) and len(players[1]):
    '''
        Game over when there are no cards in one of the decks OR
        if we hit the maximum amount of turns. Occassionally this 
        can run for a long long time if we don't....
    '''
    turns += 1
    if turns >= max_turns:
        break

    p1Card = players[0].pop()
    p2Card = players[1].pop()

    current_cards = [p1Card, p2Card]
    print("P1 = {}, P2 = {}".format(p1Card.getVisual(),p2Card.getVisual()))
    if p1Card.weight > p2Card.weight:
        prependCards(players[0], current_cards) 
    elif p2Card.weight > p1Card.weight:
        prependCards(players[1], current_cards) 
    else:
        print("War")
        # Cards are equal, doWar() and see who wins
        p1, p2, risk = doWar(players[0], players[1], 3)

        winner_list = None
        if not p1 or (p2 and p1.weight < p2.weight) :
            winner_list = players[1]
        elif not p2 or (p1 and p1.weight > p2.weight) : 
            winner_list = players[0]

        # Winner gets risk cards and current cards
        prependCards(winner_list, risk) 
        prependCards(winner_list, current_cards) 


'''
    Because we might stop the game before it really ends, figure out who won
'''
winner = None
if len(players[0]) and len(players[1]):
    if len(players[0]) > len(players[1]):
        winner = "Player 1"
    else: 
        winner = "Player 2"
else:
    winner = "Player 1" if len(players[0]) > 0 else "Player 2"

print("{} won the game in {} turns".format(winner, turns))
print(len(players[0]), len(players[1]))
