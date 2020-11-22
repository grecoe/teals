from tkinter import Tk
from ui.window import InstructionalUi
from configuration.helpconfig import HelpConfig

# Load the configuration file
computer_help_configuration = HelpConfig('helpconfig.json')

# Create a window then an App using the window and the list of
# configurations that will display content.
program_window = Tk()
tkinter_application = InstructionalUi(program_window, computer_help_configuration.configurations)
tkinter_application.mainloop()
