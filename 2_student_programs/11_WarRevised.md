# War Revised

|||
|---|---|
|Goal|Complete simulation of the card game War.|
|Required Reading| 0_python\00_variables.py|
||0_python\02_casting.py|
||0_python\03_comparison.py|
||0_python\04_input.py|
||0_python\05_if.py|
||0_python\06_while.py|
||0_python\08_list.py|
||0_python\10_functions.py|

## Details
In 10_WarIntro.md you started creating the card game War. In that program you had to:
- Create a full deck of cards
- Randomize those cards (random.shuffle())
- Get players names
- Deal out two decks to the players
- Compare cards
- Go to War (on a tie)

However, while there was a winner (whomever didn't run out of cards) as the cards were completely discarded.

This attempt at the game will complete the program.

### Implementation Details
- Whomever wins a card flip takes the winner cards. However, they cannot simply be added to the end of a list as that is the 'top' of the players deck. 
- War needs to be a function if it is not already. 
    - The war function has a parameter of how many flip cards there should be. In the original description of the game, only one card is placed face down in a war. Make this programmable so that you could put, for example, 3 cards face down. 
    - The war function has to deal with an edge case. That is, what is your program going to do when one of the players doesn't have enough cards to finish the war?
- You should put a max_play counter in your main loop. There are times when the randomness of the cards isn't enough and the game can go on for many many turns. Allow the programmer to limit this.
    - If the counter hits the max_play count, the game should terminate and the winner is decided based on who holds more cards at that point. 