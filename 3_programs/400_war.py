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


'''
    playingCard

    This class represents a single card. It's face value, suit and weight. 
'''
class playingCard:
    def __init__(self, cardFace, suit, weight):
        self.face = cardFace
        self.suit = suit
        self.weight = weight
    
    def wins(self, card):
        return self.weight > card.weight

    def getVisual(self):
        return "{}{}".format(self.face, self.suit)

'''
    playingCardDeck

    This class represents a full deck (52) of playing cards. 
'''
class playingCardDeck:
    def __init__(self):
        self.deck = []
        self.shuffledDeck = []
        self._buildDeck()

    def _buildDeck(self):
        for suit in suits:
            for card in cards:
                self.deck.append(playingCard(card, suit, weights[card]))

    def shuffleDeck(self):
        options = list(range(1,53,1))
        shuffle = random.shuffle(options)
        for opt in options:
            self.shuffledDeck.append(self.deck[opt - 1])

    def splitDeck(self):
        sets = []
        sets.append([])
        sets.append([])
        currentSet = 0
        for card in self.shuffledDeck:
            sets[currentSet%2].append(card)
            currentSet += 1

        return sets[0], sets[1]

'''
    warPlayer

    This class is a game player that has a name and a set of cards
    they are playing with. 
'''
class warPlayer:
    def __init__(self, name, cards):
        self.name = name
        self.personalDeck = cards

    def cardCount(self):
        return len(self.personalDeck)

    def getTopCard(self):
        return self.personalDeck.pop(0)

    def addCards(self, cardCollection):
        for card in cardCollection:
            self.personalDeck.append(card)

'''
    playTie:

    In war if there the cards are of equal weight, then the players go to war.

    In this case, they remove 'cardsAtRisk' number of cards from the deck and then compare 
    the next one. If it's a tie, they redo this step. If one wins, the winner takes all the cards
    from the war. 

    If a user doens't have enough cards to play the war, then they forfiet all their cards to the opponent
    and lose the game (eventually).
'''
def playTie(player1, player2, cardsAtRisk):
    riskCards = []
    winningPlayer = None

    while True:
        if player1.cardCount() < cardsAtRisk + 1:
            print(player1.name, " doesn't have enough cards, it's a forfiet.") 
            winningPlayer = player2
            while player1.cardCount() > 0:
                riskCards.append(player1.getTopCard())
            break
        elif player2.cardCount() < cardsAtRisk + 1:
            print(player2.name, " doesn't have enough cards, it's a forfiet.") 
            winningPlayer = player1
            while player2.cardCount() > 0:
                riskCards.append(player2.getTopCard())
            break

        for c in range(1,cardsAtRisk + 1, 1):
            riskCards.append(player1.getTopCard())
            riskCards.append(player2.getTopCard())

        p1Card = player1.getTopCard()
        p2Card = player2.getTopCard()
        riskCards.append(p1Card)
        riskCards.append(p2Card)

        if p1Card.wins(p2Card):
            winningPlayer = player1
            print(player1.name, " wins the war with ", p1Card.getVisual(), " and ", player2.name, " lost with card ", p2Card.getVisual()) 
            break
        elif p2Card.wins(p1Card):
            winningPlayer = player2
            print(player2.name, " wins the war with ", p2Card.getVisual(), " and ", player1.name, " lost with card ", p1Card.getVisual()) 
            break
        else:
            print("Its another tie! {} - {}, {} - {}".format(player1.name, p1Card.getVisual(), player2.name, p2Card.getVisual()) )

    if  not winningPlayer is None:
        print(winningPlayer.name, " wins the WAR!")
        winningPlayer.addCards(riskCards)
        settled = True

    return winningPlayer
        
'''
    Actual game play
'''
# Build the deck to play with
cardDeck = playingCardDeck()

player1 = input("Who is the first player?: ")
player2 = input("Who is the second player?: ")

# Shuffle the deck
print("Shuffling the deck....")
cardDeck.shuffleDeck()

# Split the deck into 2
print("Dealing cards")
player1Cards, player2Cards = cardDeck.splitDeck()

# Generate the users with a name and a set of cards. 
print("Generate user objects")
warPlayer1 = warPlayer(player1, player1Cards)
warPlayer2 = warPlayer(player2, player2Cards)

# Start actually playing 
print("Start game")

# If the game goes on too long, lets create a flag that will let us
# simply end the game. 
turnMaximumBeforeTheyGetBored = 100

## Stats to track
turns = 0
wars = 0
turnsWon = {}
turnsWon[warPlayer1.name] = 0
turnsWon[warPlayer2.name] = 0
warWins = {}
warWins[warPlayer1.name] = 0
warWins[warPlayer2.name] = 0
## Stats to track

# Continuously loop until someone has no cards (or they get bored!)
while warPlayer1.cardCount() > 0 and warPlayer2.cardCount() > 0:
    turns += 1

    # Sometimes you just have to quit because you're bored :)
    if turns > turnMaximumBeforeTheyGetBored:
        print("{} and {} got bored and quit. ".format(warPlayer1.name, warPlayer2.name))
        break

    p1Card = warPlayer1.getTopCard()
    p2Card = warPlayer2.getTopCard()

    print(warPlayer1.name, " plays ", p1Card.getVisual(), "and ", warPlayer2.name, " plays card ", p2Card.getVisual()) 

    winningPlayer = None
    if p1Card.wins(p2Card):
        winningPlayer = warPlayer1
    elif p2Card.wins(p1Card):
        winningPlayer = warPlayer2
    else:
        winningPlayer = playTie(warPlayer1, warPlayer2, 3)
        wars += 1
        warWins[winningPlayer.name] += 1


    turnsWon[winningPlayer.name] += 1
    print(winningPlayer.name, " wins the match!\n")
    winningPlayer.addCards([p1Card, p2Card])


# Print out information about the game that was just played. 
print("Game over in {} turns! ".format(turns))
print("Game maximum turns = ", turnMaximumBeforeTheyGetBored)
for key in turnsWon.keys():
    print(key, " won ", turnsWon[key], " times. ")
print("Total Wars Fought  : ", wars)
for key in warWins.keys():
    print(key, " won ", warWins[key], " wars. ")

print("Card count at the end:")
print("{} : {} - {} : {}".format(warPlayer1.name, warPlayer1.cardCount(), warPlayer2.name, warPlayer2.cardCount()))
