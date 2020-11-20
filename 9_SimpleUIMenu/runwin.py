from tkinter import * 
from ui.window import InstructionalUi
from configuration.helpconfig import HelpConfig

'''
    1. Identify a settings yml
    2. Create ProjectConfiguration instance
    3. Create a Tk instance
    4. Create a SettingsUpdate instance with the ProjectConfiguration
       instance and Tk instance already created. 
'''

# Load the configuration file
hc = HelpConfig('helpconfig.json')

# Create a window then an App using the window and the list of 
# configurations that will display content.
window = Tk()
app = InstructionalUi(window, hc.configurations)
app.mainloop()
