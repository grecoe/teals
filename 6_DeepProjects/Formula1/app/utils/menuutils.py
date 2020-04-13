from app.functions.interface import IFunction

class MenuUtils:
    MENU_TITLE = "F1 App"
    def __init__(self):
        pass

    @staticmethod
    def _menu_recurse(dictionary, indent, command_list):
        '''
            This function is a recursive funciton if a dictionary
            contains a dictionary called by display_menu_help
        '''
        indent_spaces = '   ' * indent
        for sub_command in dictionary:
            print(indent_spaces + sub_command)
            if isinstance(dictionary[sub_command], dict):
                command_list.append(sub_command)
                MenuUtils._menu_recurse(dictionary[sub_command], indent + 1, command_list)
            elif isinstance(dictionary[sub_command], IFunction):
                command_list.append(sub_command)
                dictionary[sub_command].get_help(indent + 1, command_list)
                # End of the line, so take the last command off or we end
                # up with invalid commands being printed in help.
                command_list = command_list[:command_list.index(sub_command)]
    
    @staticmethod
    def display_menu_help(menu_dictionary, args = None):
        '''
            This function starts the process of iterating over the 
            dictionary menu. A dictionary can only contain 
                1. Keys that identify another dictionary
                2. Keys that identify actual functions.
        '''
        print("{}:".format(MenuUtils.MENU_TITLE))
        for command in menu_dictionary.keys():
            print(command)
            if isinstance(menu_dictionary[command], dict):
                MenuUtils._menu_recurse(menu_dictionary[command], 1, [command])
            elif isinstance(menu_dictionary[command], IFunction):
                menu_dictionary[command].get_help(1 [command])
        print('')
