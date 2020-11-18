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
        Logger.add_log("Adding game : {}".format(game.name))
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
                Logger.add_log("User chose {} game option, load entry point".format(selection))

                # Get the game of choice (exception if bad, but caught and dealt with)
                game_entry = int(selection)
                entry_point = load_module(
                    game_configurations[game_entry].module,
                    game_configurations[game_entry].entry_point
                )

                if entry_point:
                    # We loaded a function from teh module, go for it!
                    os.system('cls')

                    # Execute the game (after clearing the screen for it)
                    entry_point()

                    # Let user know game is over
                    print("The game {} has ended, press any key to continue".format(game_configurations[game_entry].name))
                    input("")
                    os.system('cls')
                else:
                    # Let user know there was an error getting the game loaded
                    print("The game {} could not be loaded, try another game.".format(game_configurations[game_entry].name))
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
