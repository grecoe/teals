import os
from utils.configuration import load_configuration
from utils.loader import load_module
from utils.tracer import TraceDecorator, Logger


@TraceDecorator
def run_controller():
    # Load up configuration settings
    config = load_configuration("gameconfig.json")

    # Map all games to a number so we can print/select them
    game_configurations = {}
    game_count = 1
    for game in config:
        Logger.add_log("Loading game : {}".format(game.name))
        game.play_function = load_module(
            game.module,
            game.entry_point)

        if game.play_function:
            game_configurations[game_count] = game
            game_count += 1

    # Now show them as options to the user
    while True:
        Logger.add_log("Enter game loop")

        # Let user know what games are available
        print("\nAvailable Games\n")
        for game in game_configurations:
            print("{} - {}".format(game, game_configurations[game].name))

        # Get the selection
        selection = input("\nEnter game selection (q) to quit > ")

        # Validate the selection
        if selection.lower() == 'q':
            Logger.add_log("User chose 'q' option")
            print("Later.....")
            break
        else:
            try:
                Logger.add_log("User chose {} game option".format(selection))

                # Get the game of choice (exception if bad, but caught and dealt with)
                game_entry = int(selection)

                # We loaded a function from teh module, go for it!
                os.system('cls')

                # Execute the game (after clearing the screen for it)
                game_configurations[game_entry].play_function()

                # Let user know game is over
                print("The game {} has ended, press any key to continue".format(game_configurations[game_entry].name))
                input("")
                os.system('cls')

            except Exception as ex:
                # Let user know there was an error executing the game
                Logger.add_log("Invalid selection : {}".format(str(ex)))
                print("Invalid selection! Press any key to continue")
                input("")
                os.system('cls')


# Now run i
run_controller()
