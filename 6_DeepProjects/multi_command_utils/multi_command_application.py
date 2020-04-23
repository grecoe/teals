import os
from multi_command_utils.interface import IFunction
from multi_command_utils.menuutils import MenuUtils

class MultiCommandApp:
    def __init__(self, prompt, application_menu):
        self.prompt = prompt
        self.app_menu = application_menu

        # Add in default help/quit/clear if not there
        if 'help' not in self.app_menu.keys():
            self.app_menu['help'] = self._help
        if 'clear' not in self.app_menu.keys():
            self.app_menu['clear'] = self._clear
        if 'quit' not in self.app_menu.keys():
            self.app_menu['quit'] = quit


    def run(self):
        while True:   
            user_input = input("{} : > ".format(self.prompt))
            inputs = user_input.split(' ')

            if len(inputs) > 0 and inputs[0] in self.app_menu.keys():
                current_action = self.app_menu
                last_command_index = 0

                triggered = False
                for next_input in inputs:
        
                    next_input = next_input.strip()
                    if len(next_input) == 0 :
                        continue

                    last_command_index += 1
                    '''
                        Note that on an invalid command, a high level function, or 
                        an instance of IFunction, we want to break the loop once
                        we execute that if/elif segment as there are no more items 
                        to parse. 
                    '''
                    if next_input not in current_action.keys():
                        print("Invalid Command : ", " ".join(inputs))
                        MenuUtils.display_menu_help(self.app_menu)
                        triggered = True
                        break
                    elif callable(current_action[next_input]):
                        # Top level functions, typically quit and help
                        current_action[next_input]()
                        triggered = True
                        break
                    elif isinstance(current_action[next_input], IFunction):
                        # IFunction instance
                        current_action[next_input].execute(inputs[last_command_index:])
                        triggered = True
                        break
                    else:
                        current_action = current_action[next_input]

                if not triggered:
                    MenuUtils.display_menu_help(current_action, next_input)

            else:
                print("Invalid Command : ", " ".join(inputs))
                MenuUtils.display_menu_help(self.app_menu)

            

    def _help(self):
        '''
            Top level help function
        '''
        MenuUtils.display_menu_help(self.app_menu)

    def _clear(self):
        '''
            Clear the screen
        '''
        os.system('cls')
