'''
    This is a take on the ZORK game that was done in intro to computer science but
    using object oriented programming.

    The game has a hero meandering through a building where he/she needs to pick up
    items and kill monsters and a boss.

    In general, it is a very simple game, but with object oriented programming breaking
    down the funcitonlity it is a complex coding problem.

    The user has to collect all items and kill all of the monsters and the boss to
    complete the game. When it comes time to fight, the rules are:

        Fight rules,
            1. Win against monster ONLY if hero has sword.
            2. Win against Boss ONLY if hero has sword and jewels.

    Functionality is broken down into three classes
        Hero
        Building
        Floor

    The beginning of the file is all definitions, the actual program starts on
    line 221.

    For testing purposes, we can feed in all of the user input through a file that
    identifies the path to success. This file is the 500_zork_input.txt and you use it
    like this:

        cat 500_zork_input.txt | python 500_zork.py

    This will feed the file, line by line, to each of the input functions within the script
    meaning that you can test your path rapidly.

'''

import os
from enum import Enum


class legal_commands(Enum):
    '''
        Enumeration that describes directions the hero can move in,
        and the actions he/she can perform.
    '''
    right = 1
    left = 2
    up = 3
    down = 4
    grab = 5
    fight = 6
    quit = 7


class room_content(Enum):
    '''
        Enumeration that describes what can appear in a room.
    '''
    empty = 1
    sword = 2
    jewels = 3
    monster = 4
    boss = 5
    stairs_up = 6
    stairs_down = 7


'''
    Lookup table for getting room content descriptions
'''
room_content_description = {
    room_content.empty.value: "is empty",
    room_content.sword.value: "has a sword in the corner",
    room_content.jewels.value: "has jewels on the floor",
    room_content.monster.value: "has a monster!",
    room_content.boss.value: "has The Boss!",
    room_content.stairs_up.value: "has stairs going up",
    room_content.stairs_down.value: "has stairs going down"
}


class Hero:
    '''
        The Hero class contains everything (methods and properties) that the Hero
        will need to complete this quest.
    '''
    def __init__(self, name):
        self.name = name
        self.inventory = []
        self.victorious = False
        self.alive = True

    def getNextMove(self, building):
        '''
            Gets a visible description of
                - Where the hero is in the building.
                - The Hero's inventory
                - A list of possible actions
                - A prompt

            It will return a tuple that is [0] = prompt, [1] = legal moves
        '''
        os.system('cls')
        inventory_list = ""
        movement_list = ""
        current_building_floor = building.getCurrentFloor()
        movements = current_building_floor.getPossibleDirections()

        for inv in self.inventory:
            inventory_list += inv.name + " "

        for move in movements:
            movement_list += "\n   " + move

        statement = "Our hero " + self.name + " is on floor " + str(current_building_floor.floor_number)
        statement += " in room " + str(current_building_floor.current_room)
        statement += "\nHis inventory is  " + inventory_list
        statement += "\nThe room  " + current_building_floor.getRoomContentString()
        statement += "\nYour possible moves are:" + movement_list
        statement += "\nWhat are you going to do? > "
        return statement, movements

    def grabItem(self, room_contents):
        '''
            Hero action to pick up an item within the room. Supported Items are:
                room_content_jewels
                room_content_sword

            NOTE: Currently picking up only one item is supported so only put one
                  item in your room. This can easily be extended....try it!
        '''
        global room_content
        its_jewels = room_content.jewels in room_contents
        its_sword = room_content.sword in room_contents
        if its_jewels:
            self.inventory.append(room_content.jewels)
            room_contents.pop(room_contents.index(room_content.jewels))
        elif its_sword:
            self.inventory.append(room_content.sword)
            room_contents.pop(room_contents.index(room_content.sword))

    def doFight(self, room_contents):
        '''
            Fights either a monster or a Boss. Rules at the top of this code file.
        '''
        global room_content
        is_monster = room_content.monster in room_contents
        is_boss = room_content.boss in room_contents
        has_sword = room_content.sword in self.inventory
        has_jewels = room_content.jewels in self.inventory

        if is_monster:
            if has_sword:
                # Kill the monster and remove from room
                room_contents.pop(room_contents.index(room_content.monster))
                print("Our hero killed the monster!")
            else:
                # Kill the hero
                self.alive = False
                print("Our hero was killed by the monster!")

        if is_boss:
            if has_sword and has_jewels:
                # Kill the boss and remove from room
                room_contents.pop(room_contents.index(room_content.boss))
                print("Our hero killed The Boss!")
                self.victorious = True
            else:
                # Kill the hero
                self.alive = False
                print("Our hero was killed by The Boss!")


class Building:
    '''
        The Building class deals with the layout of the floors
        contained within it.
    '''
    def __init__(self):
        self.floors = {}
        self.current_floor = None

    def addFloor(self, floor):
        '''
            Adds a floor to the floor list within the building.
        '''
        self.floors[floor.floor_number] = floor

    def setCurrentFloor(self, floor_number):
        '''
            Sets the current floor that the hero is on in the building.
        '''
        self.current_floor = self.floors[floor_number]

    def getCurrentFloor(self):
        '''
            Returns the current floor that the hero is on in the building.
        '''
        return self.current_floor

    def doAction(self, command):
        '''
            doAction is the entry point for all actions related to the building. These
            include moving up and down within the floors.
        '''
        current_room = self.current_floor.current_room
        if command.value == 3:  # up
            self.setCurrentFloor(self.current_floor.floor_number + 1)
            self.current_floor.current_room = current_room
        elif command.value == 4:  # down
            self.setCurrentFloor(self.current_floor.floor_number - 1)
            self.current_floor.current_room = current_room


class Floor:
    '''
        The Floor class contains rooms and the contents of the rooms that the Hero
        will traverse.
    '''
    def __init__(self, floor_number, floor_plan):
        self.floor_plan = floor_plan
        self.floor_number = floor_number
        self.current_room = 0

    def doAction(self, command, hero):
        '''
            doAction is the entry point for all actions and movements related to a floor.
            These are the movement left and right, picking up items, and fighting.
        '''
        global legal_commands

        if command.value == legal_commands.right.value:
            self.current_room += 1
        elif command.value == legal_commands.left.value:
            self.current_room -= 1
        elif command.value == legal_commands.grab.value:
            hero.grabItem(self.floor_plan[self.current_room])
        elif command.value == legal_commands.fight.value:
            hero.doFight(self.floor_plan[self.current_room])
            input("Press Enter to continue....")

        # In a couple of cases the room may have been emptied, make sure it isn't....
        if len(self.floor_plan[self.current_room]) == 0:
            self.floor_plan[self.current_room].append(room_content.empty)

    def getPossibleDirections(self):
        '''
            Determines what is available to our hero based on what is contained
            within a single room.
        '''
        returnDirections = []
        if self.current_room > 0:
            returnDirections.append(legal_commands.left.name)
        if self.current_room < (len(self.floor_plan) - 1):
            returnDirections.append(legal_commands.right.name)

        for content in self.floor_plan[self.current_room]:
            if content == room_content.sword or content == room_content.jewels:
                returnDirections.append(legal_commands.grab.name)
            if content == room_content.monster or content == room_content.boss:
                returnDirections.append(legal_commands.fight.name)
            if content == room_content.stairs_up:
                returnDirections.append(legal_commands.up.name)
            if content == room_content.stairs_down:
                returnDirections.append(legal_commands.down.name)

        # Always allow quit
        returnDirections.append(legal_commands.quit.name)

        return returnDirections

    def getRoomContentString(self):
        '''
            Get a visible description of what is in the room to show to the user.
        '''
        global room_content_description
        contents = self.floor_plan[self.current_room]
        returnContentValue = ""
        for content in contents:
            if returnContentValue != "":
                returnContentValue += " and "
            returnContentValue += room_content_description[content.value]
        return returnContentValue


'''
    Program starts here.....
'''

'''
    Build floor plans.

    Legend:
        ^ Stairs Up
        ! Stairs Down
        $ Jewels
        # Sword
        M Monster
        B Boss
        X Start

        -----------------
        | ! | $ | B | ! |
        -----------------
        | ^ |   | M | ^!|
        -----------------
        | X |   | # | ^ |
        -----------------
'''
fp = [
    [room_content.empty],
    [room_content.empty],
    [room_content.sword],
    [room_content.empty, room_content.stairs_up]
]
fp2 = [
    [room_content.empty, room_content.stairs_up],
    [room_content.empty],
    [room_content.monster],
    [room_content.empty, room_content.stairs_down, room_content.stairs_up]
]
fp3 = [
    [room_content.empty, room_content.stairs_down],
    [room_content.jewels],
    [room_content.boss],
    [room_content.empty, room_content.stairs_down]
]
f1 = Floor(1, fp)
f2 = Floor(2, fp2)
f3 = Floor(3, fp3)

# Create a building and add the floors to it
building = Building()
building.addFloor(f1)
building.addFloor(f2)
building.addFloor(f3)
building.setCurrentFloor(1)

# Create our hero
hero = Hero("Fred")

while True:
    statement, movements = hero.getNextMove(building)

    user_selection = input(statement)
    if user_selection in movements:
        if (legal_commands.quit.name == user_selection):
            input("You have chosen to quit....\nPress enter to exit the game....")
            break

        if (legal_commands.fight.name in movements) and (legal_commands.fight.name != user_selection):
            input("\n\nYou must fight!\n\nPress enter to continue....")
            user_selection = legal_commands.fight.name

        command = legal_commands[user_selection]
        if command in [legal_commands.up, legal_commands.down]:
            building.doAction(command)
        else:
            building.getCurrentFloor().doAction(command, hero)

        if hero.victorious:
            input("Our hero has won!\nPress enter to exit....")
            break
        if not hero.alive:
            input("Our hero has died!\nPress enter to exit....")
            break
    else:
        input("Invalid move...try again...press Enter to continue!")

