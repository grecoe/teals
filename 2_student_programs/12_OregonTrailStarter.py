'''
    OREGON TRAIL STARTER KIT

    We will start by collecting the information we 
    need from the instructions to be succesful. 

    We will then start creating functions and testing
    them along the way. 

    Pull the repo
        If you have changes that GIT complains about, change the git pull
        call slightly to force an overwrite:
            git reset --hard origin/master
            git pull
'''


'''
    What do we need to store? 
    What do we know from the instructions?

    DATA NEEDED:
    1. Trip starts on 03/01
    2. Distance to travel = 2000 miles
    3. Player starts with 500lbs of food
    4. Player starts with 5 health
    5. How far has the player moved
    6. Must be at end of trip on 12/31
    7. The list of months that have 31 days 
       is given in the implmementation details:
       MONTHS_WITH_31_DAYS = [1, 3, 5, 7, 8, 10, 12]
'''
import random

# Months with 31 days
MONTHS_WITH_31_DAYS = [1, 3, 5, 7, 8, 10, 12]
# How far is the total trip
total_trip_distance = 2000
# Current month/day
current_day = 1
current_month = 3
# Player information
player_name = ""
player_distance = 0
player_health = 5
player_food = 500


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
def dailyUpdate(days):
    '''
        Daily tasks that must be completed:
        1. Move clock (month/day) ahead by 1
        2. Reduce food by 5lbs
        3. Check for a decrease in health
    '''
    global player_food
    global player_health

    for day in range(days):
        # Move clock
        addDay()
        # Consume 5lbs of food
        player_food -= 5
        # 5% chance of drop in health
        if isHealthDecreased():
            player_health -= 1

def addDay():
    '''
        Move the day forward by 1
    '''
    global current_day
    global current_month
    global MONTHS_WITH_31_DAYS

    # 1 Find out how many days are in the month
    days_in_month = 30
    if current_month in MONTHS_WITH_31_DAYS:
        days_in_month = 31

    # Increase the day
    current_day += 1

    # Is it greater than the number of days in the month?
    #   Yes : Increase month by 1 and set day to 1
    #   No  : Still in same month, it's all good
    if current_day > days_in_month:
        current_month += 1
        current_day = 1

def isHealthDecreased():
    '''
        The game rules state that:

        Every day that passes, there should be a 5% chance that the player loses 1 health, 
        so get a random number between 1-100 and see if it's
        less than or equal to 5.

        Return true if health should decrease.
    '''
    return random.randint(1,100) <= 5

'''
    Required actions
'''
def travel():
    '''
        moves you randomly between 30-60 miles and 
                     takes 3-7 days (random).
    '''
    global player_distance
    travelled = random.randint(30,60)
    days = random.randint(3,7)

    print("Days Travelled:", days)
    print("Miles Travelled:", travelled)

    player_distance += travelled

    dailyUpdate(days)

def rest():
    '''
    increases health 1 level (up to 5 maximum) and 
                 takes 2-5 days (random).    
    '''
    global player_health
    days = random.randint(2,5)

    if player_health  < 5:
        player_health += 1

    dailyUpdate(days)

def hunt():
    '''
        adds 100 lbs of food and takes 2-5 days (random).
    '''
    global player_food
    days = random.randint(2,5)

    player_food += 100

    dailyUpdate(days)

def status():
    global player_name
    global player_distance
    global player_food
    global player_health
    global total_trip_distance
    global current_month
    global current_day
    
    print('''
    Oregon Trail Status
      Date     : {} / {}
      Player   : {}
      Distance : {} miles of {} miles
      Health   : {}
      Food     : {} lbs
    '''.format(current_month, current_day, player_name,player_distance, total_trip_distance, player_health, player_food))

def help():
    print('''
    Oregon Trail Help
      travel  : moves you randomly between 30-60 miles and takes 3-7 days.
      hunt    : Adds 100 lbs of food and takes 2-5 days
      rest    : Increases health 1 level (up to 5 maximum) and takes 2-5 days.    
      status  : Show game status
      help    : Show this menu
      quit    : Exit the game
    ''')





'''
    Now write the program here.....
'''

player_name = input("Enter your name > ")
player_action = input("{}, what do you do next? > ".format(player_name))

# Play until a quit signal is detected
while player_action not in ["Quit", "quit", "q"]:

    '''
        Look for the command that the user input. We know it's not quit. 
        If we don't understand it, default is to show help
    '''
    if player_action == "travel":
        travel()
    elif player_action == "hunt":
        hunt()
    elif player_action == "rest":
        rest()
    elif player_action == "status":
        status()
    else:
         help()

    '''
        See if the game ended by
            1. Player health == 0
            2. Player food == 0
            3. Player distance is enough
    '''
    if player_health <= 0:
        print("{} has died on the Oregon Trail".format(player_name))
        break
    elif player_food <= 0:
        print("{} has starved on the Oregon Trail".format(player_name))
        break
    elif player_distance >= total_trip_distance:
        print("{} has made it to Oregon, you win!".format(player_name))
        break
    
    player_action = input("{}, what do you do next? > ".format(player_name))

print("Oregon Trail is over")
status()
