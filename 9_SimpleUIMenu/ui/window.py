from os import path
import tkinter as tk
import tkinter.ttk as ttk
import tkinter.scrolledtext as st
import webbrowser


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
        self.current_online_content = {}

        # Set up some window options
        self.master_win.title("Computer Help")
        self.master_win.geometry('1100x675')
        self.master_win.resizable(width=tk.TRUE, height=tk.TRUE)
        self.master_win.configure(padx=10, pady=10)
        self.master_win.iconbitmap('./assets/settings.ico')

        # Set up the frames
        self.tree_frame.grid(column=0, row=0, sticky="ns")
        self.text_frame.grid(column=1, row=0, sticky="nwse")
        self.master_win.rowconfigure(0, weight=1)
        self.master_win.columnconfigure(1, weight=1)

        # UI Controls
        self.tree = None

        '''
            Populate the grid first with settings followed by the two buttons (cancel/save)
        '''
        # Insert a tree view and a window (text) to the right
        self.tree = ttk.Treeview(self.tree_frame)
        self.tree.pack(expand=True, fill='y')
        self.tree.bind("<Button-1>", self.selection_changed)
        self.treestyle = ttk.Style()
        self.treestyle.configure("Treeview.Heading", background="blue", font=("Helvetica", 16))

        # Run through the configurations in the

        for config in self.config.configurations:
            parent_id = self.tree.insert(parent='', index='end', iid=config.parent.id, text=config.parent.name, tags=config.parent.content)

            for child in config.children:
                self.tree.insert(parent=parent_id, index='end', iid=child.id, text=child.name, tags=child.content)

        # Set the heading (Attribute Names)
        self.tree.heading('#0', text='Topics')

        # Specify attributes of the columns (We want to stretch it!)
        self.tree.column('#0', stretch=tk.YES)

        self.master_win.pack_propagate()

    def selection_changed(self, event):
        """
        An item has been selected in the tree.
        """

        # Try to identify the item....
        item = self.tree.identify('item', event.x, event.y)
        if item:
            try:
                self.__show_topic(self.text_frame, self.tree.item(item))
            except Exception as ex:
                print("ERR", str(ex))

    def __show_topic(self, parent_frame, tree_item):
        """
            The right frame is broken down to

            LBL -> LBL (Topic name)
            LBL -> Text (description from text file)
        """
        online_content = False
        self.current_online_content = {}
        found_topic = self.config.find_topic(tree_item['text'])
        if found_topic:
            if hasattr(found_topic, 'online_resource'):
                online_content = found_topic.online_resource

        # Clear the frame
        for widget in parent_frame.winfo_children():
            widget.destroy()

        # this will clear frame and frame will be empty
        # if you want to hide the empty panel then
        parent_frame.pack_forget()

        # Keep track of the row identity
        row_identity = 0

        # First row is topic name
        lbl = tk.Label(parent_frame, text="Topic:", font=("Helvetica", 16))
        lbl.grid(row=row_identity, column=0, columnspan=1, sticky='w')
        lbl = tk.Label(parent_frame, text=tree_item['text'], font=("Helvetica", 16))
        lbl.grid(row=row_identity, column=2, columnspan=1, sticky='w', padx=15)

        row_identity += 1

        # Optional second row ONLY if there is any online content
        if online_content:
            """
                Content is either just a string of a URL OR
                A list of objects:
                {
                    name = Name of the link
                    resourdce = URL to go to
                }
            """
            lbl = tk.Label(parent_frame, text="Online Resource:", font=("Helvetica", 16))
            lbl.grid(row=row_identity, column=0, columnspan=1, sticky='w')

            # First, we have to see if this is a list or not
            if isinstance(online_content, list):
                # We have to unpack each one
                for item in online_content:
                    self.current_online_content[item['name']] = item['resource']
            else:
                # Its a single string.
                link_text = online_content
                if len(link_text) > 30:
                    link_text = "Online Help : {}".format(tree_item['text'])

                self.current_online_content[link_text] = online_content

            for link in self.current_online_content.keys():
                lbl = tk.Label(parent_frame, text=link, foreground="blue", font=("Helvetica", 16))
                lbl.grid(row=row_identity, column=2, columnspan=1, sticky='w', padx=15)
                lbl.bind('<Button-1>', self._callback)
                row_identity += 1

        # Second row is the content, we need to grab the tag which has the file
        # containing the content to display.
        lbl = tk.Label(parent_frame, text="Description: ", font=("Helvetica", 16))
        lbl.grid(row=row_identity, column=0, columnspan=1, sticky='nw', )
        txt = st.ScrolledText(parent_frame, wrap="word", height=40, width=100, font=("Helvetica", 13))
        txt.grid(row=row_identity, column=2, columnspan=2, sticky='nwse', pady=15, padx=15)

        # Now get the data to put it in if found
        output = "Content file could not be found:\n\n{}".format(tree_item['tags'])
        if len(tree_item['tags']) == 1:
            content_path = tree_item['tags'][0]
            if path.exists(content_path):
                with open(content_path, 'r') as content:
                    content_data = content.readlines()
                    output = "\n".join(content_data)

        txt.insert(tk.END, output)

    def _callback(self, *args):

        if isinstance(args[0].widget, tk.Label):
            label_text = args[0].widget.cget('text')

            if label_text in self.current_online_content.keys():
                webbrowser.open_new(self.current_online_content[label_text])