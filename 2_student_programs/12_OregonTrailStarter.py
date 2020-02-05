'''
    OREGON TRAIL STARTER KIT

    First read 12_OregonTrail.md then come back to this file. 

    We will start by collecting the information we 
    need from the instructions to be succesful. 

    We will then start creating functions and testing
    them along the way. An important hint here is the 
    built in python funciton quit() makes your program
    exit. 
'''

'''
    What do we need to store? 
    What do we know from the instructions?

    DATA NEEDED:
    1. Trip starts on 03/01
    2. Distance to travel = 2000 miles
    3. Player starts with 500lbs of food
    4. Player starts with 5 health
    5. Must be at end of trip on 12/31
    6. The list of months that have 31 days 
       is given in the implmementation details:
       MONTHS_WITH_31_DAYS = [1, 3, 5, 7, 8, 10, 12]
'''


'''
    What actions do we ned to take? 
    What do we know from the instructions?

    ACTIONS NEEDED: 
    1. Collect the users name.
    2. Get user input for a command:
        travel : moves you randomly between 30-60 miles and 
                 takes 3-7 days (random).
        rest   : increases health 1 level (up to 5 maximum) and 
                 takes 2-5 days (random).
        hunt   : adds 100 lbs of food and takes 2-5 days (random).
        status : lists food, health, distance traveled, and day.
        help   : lists all the commands.
        quit   : will end the game.
    
    Implementation details tell us
        - Create functions for all options a player can take
        - Create a function add_day which updates the day
        - Every day that passes, there should be a 5% chance 
          that the player loses 1 health.
        - Every day that passes, the player eats 5lbs of food
'''

'''
    Write functions here:
'''

'''
    Provided Function(s)
'''
def addDay():
    '''
        Move the day forward by 1
    '''
    pass

def isHealthDecreased():
    '''
        The game rules state that:

        Every day that passes, there should be a 5% chance that the player loses 1 health, so get a random number between 1-100 and see if it's
        less than or equal to 5.

        Return true if health should decrease.
    '''
    return random.randint(1,100) <= 5


'''
    Now write the program here.....
'''