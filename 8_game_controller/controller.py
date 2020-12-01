import os
from utils.configuration import load_configuration
from utils.loader import load_module
from utils.tracer import TraceDecorator, Logger


@TraceDecorator
def load_game_configurations(configuration_file):
    # Load up configuration settings
    config = load_configuration(configuration_file)

    # Map all games to a number so we can print/select them
    game_configurations = {}
    game_count = 1
    for game in config:
        Logger.add_log("Loading game : {}".format(game.name))
        game.play_function = load_module(
            game.module,
            game.entry_point)

        if game.has_description():
            game.description_function = load_module(
                game.module,
                game.description)

        if game.play_function:
            game_configurations[game_count] = game
            game_count += 1

    return game_configurations


@TraceDecorator
def show_game_description(game):
    if game.description_function:
        print("**** {} Description ****".format(game.name))
        game.description_function()
        input("\n\nPress any key to play....")
        os.system('cls')


@TraceDecorator
def run_controller(game_configurations):

    # Now show them as options to the user
    loop_iteration = 0
    while True:

        # Make sure log is not too big
        Logger.clear_log()

        loop_iteration += 1
        Logger.add_log("Enter game loop - iter {}".format(loop_iteration))

        # Clear whatever is there.
        os.system('cls')

        # Let user know what games are available
        print("\nAvailable Games\n")
        for game in game_configurations:
            print("{} - {}".format(game, game_configurations[game].name))

        # Get the selection
        selection = input("\nEnter game selection (q) to quit > ")

        if selection.lower() == 'q':
            # User chose to quit....
            Logger.add_log("User chose 'q' option")
            print("Later.....")
            break
        else:
            # User made a selection, use it protected by exception.
            try:
                Logger.add_log("User chose {} game option".format(selection))

                # Get the game of choice (exception if bad, but caught and dealt with)
                current_game = game_configurations[int(selection)]

                # Optionally show description (if it has one)
                show_game_description(current_game)

                # Execute the game, would not be in list if no play function
                Logger.add_log(current_game.name, "gamehistory.log")
                current_game.play_function()

                # Let user know game is over
                input("The game {} has ended, press any key to continue\n".format(current_game.name))

            except Exception as ex:
                # Let user know there was an error executing the game
                Logger.add_log("Invalid selection : {}".format(str(ex)))
                input("Invalid selection! Press any key to continue\n")


# Execute the controller ./8_game_controller/
game_configurations = load_game_configurations("gameconfig.json")
run_controller(game_configurations)
