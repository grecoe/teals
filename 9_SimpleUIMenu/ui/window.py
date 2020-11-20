#from tkinter import * 
import tkinter as tk 
import tkinter.ttk as ttk
from tkinter import messagebox
from os import path


# https://www.askpython.com/python-modules/tkinter/tkinter-treeview-widget#:~:text=So%2C%20what%20TreeView%20allows%20us,lot%20of%20your%20GUI%20applications.

# HTML
# https://stackoverflow.com/questions/37084313/how-to-display-rendered-html-content-in-text-widget-of-tkinter-in-python-3-4-x
# pip3 install tkinterhtml

class InstructionalUi(tk.Frame):
    '''
        UI Wrapper for project configuration settings. 

        Provide a configuraiton file as described in configuration.ProjectConfiguration.

        A UI is built using a grid where each row consists of:
            setting_description | Text control to show accept values

        Final row of the grid has a save and cancel button. 

        Save updates the configuration file with any settings put on the UI.
    '''
    def __init__(self, master, help_config):
        tk.Frame.__init__(self, master=master)
        '''
            self.master_win     = Instance of Tk application. 
            self.settings       = Will be a dictionary where
                                    key = Setting name
                                    value = Text control   
        '''
        self.master_win = master
        self.tree_frame = tk.Frame(self.master_win)
        self.text_frame = tk.Frame(self.master_win)
        self.config = help_config

        # Set up some window options
        self.master_win.title("Computer Help")
        self.master_win.geometry('650x500')
        self.master_win.resizable(width=tk.TRUE, height=tk.TRUE)
        self.master_win.configure(padx = 10, pady = 10)

        # Set up the frames
        self.tree_frame.grid(column=0, row=0, sticky="ns")
        self.text_frame.grid(column=1, row=0, sticky="nse")
        self.master_win.rowconfigure(0, weight=1)
        
        # UI Controls
        self.tree = None
        self.description = None


        '''
            Populate the grid first with settings followed by the two buttons (cancel/save)
        '''
        current_row = 0

        # Insert a tree view and a window (text) to the right
        self.tree = ttk.Treeview(self.tree_frame)
        self.tree.pack(expand=True, fill='y')
        self.tree.bind("<Button-1>", self.selection_changed)

        # Run through the configurations in the 
        
        for config in self.config:
            parent_id = self.tree.insert(parent='', index='end', iid=config.parent.id, text=config.parent.name, tags=config.parent.content)

            for child in config.children:
                self.tree.insert(parent=parent_id, index='end', iid=child.id, text=child.name, tags=child.content)

        # Set the heading (Attribute Names)
        self.tree.heading('#0', text='Topics')
 
        # Specify attributes of the columns (We want to stretch it!)
        self.tree.column('#0', stretch=tk.YES)
        
        # Set up the text box
        self.description =  tk.Text(self.text_frame)
        self.description.pack(expand=True, fill='y')

        # Add in the save/cancel buttons
        """
        current_row += 1
        close_button = tk.Button(self.master_win, text="Cancel", command=self.cancel)
        close_button.grid(row=current_row, column=2, columnspan=1, sticky='nwse' )
        """

    def cancel(self):
        '''
            Cancel clicked, just close the window.
        '''
        self.master_win.destroy()

    def selection_changed(self, event):
        '''
            Save clicked
                - For each row, collect the setting name and user input.
                    - Clean user input
                - Set values for all settings
                - Save configuration
                - Close window
        '''
        # Clear text box
        self.description.delete('1.0', tk.END)

        item = self.tree.identify('item',event.x,event.y)

        output = "Content could not be read"
        if item:
            if self.tree.item(item)['tags']:
                print("Have the tag")
        
                if len(self.tree.item(item)['tags']) == 1:
                    content_path = self.tree.item(item)['tags'][0]
                    if path.exists(content_path):
                        with open(content_path, 'r') as content:
                            content_data = content.readlines()
                            output = "\n".join(content_data)

        #print("Calculated item -> ", item)
        #print("CLICKED", type(item), item, self.tree.item(item))

        #output = self.tree.item(item)['text'] + '\nTags:\n'
        # tag is list
        # output += '\n' + self.tree.item(item)['tags']
        #if self.tree.item(item)['tags']:
        #    output += "\n".join(self.tree.item(item)['tags'])


        #output = "<html><body>{}</body></html>".format(output)
        print(output)

        try:
            self.description.insert(tk.END, output)
        except Exception as ex:
            print("ERR", str(ex))
        #self.description.insert(tk.END, output)
