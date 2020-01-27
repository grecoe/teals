# War Card Game Introduction

|||
|---|---|
|Goal|Simulate the card game War.|
|Required Reading| 0_python\00_variables.py|
||0_python\02_casting.py|
||0_python\03_comparison.py|
||0_python\04_input.py|
||0_python\05_if.py|
||0_python\06_while.py|
||0_python\08_list.py|
||0_python\10_functions.py|


## Details
Create a program that lets a user play a simplified version of the card game 'War'. In this version, the users will share a single deck of cards and cards will not be added back to the deck after they have been played.

Your game should:
- Start with a given shuffled deck variable (shuffle function comes from python's random library, more details below)
- Ask for player1 and player2's names.
- Have a function player_turn, with the contract shown below:
```
# name: player_turn
# purpose: takes in a player name and draws/removes a card from the deck, prints "user drew card x", and returns the value
# input: player_name as string, deck as list
# returns: integer
```
- Have a function compare_scores that takes in the two integers representing the cards drawn and compares the card values. Make sure to write the contract for compare_scores!
- For simplicity Jacks will be represented as 11, Queens will be represented as 12, Kings will be represented as 13, and Aces will be represented as 14
For simplicity the suit does not matter
- Include a while loop that keeps the game running until there are no cards in the deck.
- If there is a tie, there is "war". Take the next two cards an whoever wins that gets all four cards (including the previous tied cards). If there is another tie, continue taking the next two cards until there a winner. The winner takes all the "war" cards.
- Keep track of the score.
- Player who won the most number of cards wins.
- Declare the name of the winner and final score at the end of the game.


# Deck Shuffling
While seemingly simple-- shuffling a deck is a somewhat complicated problem. Luckily, Python's random library has a built in shuffle algorithm. Feel free to read the documentation, but we have provided a simple wrapper function that will return to you a shuffled deck of cards.

```python
import random

def shuffled_deck():
    card_face = [2,3,4,5,6,7,8,9,10,11,12,13,14]
    number_of_suits = 4
    deck = []
    for i in range(number_of_suits):
        for card in card_face:
            deck.append(card)

    random.shuffle(deck)
    return deck
```

## Sample Output
```
Player 1's name: Pat
Player 2's name: Sam
Pat drew card 8
Sam drew card 9
Sam has high card
Pat: 0
Sam: 2
Pat drew card 9
Sam drew card 8
Pat has high card
Pat: 2
Sam: 2
Pat drew card 7
Sam drew card 7
War
Pat: 2
Sam: 2
Pat drew card 5
Sam drew card 6
Sam has high card
Sam wins war of 4 cards
Pat: 2
Sam: 6
Pat drew card 13
Sam drew card 14
Sam has high card
Winner: Sam
```
