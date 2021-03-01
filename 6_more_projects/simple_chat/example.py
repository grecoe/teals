"""
    VERY simple chat program.

    Open two command prompts and start this file. Enter a different name for each one.

    Have one send a message to the other.
    Check out inbox/sent folders for both users
    Read the message.
"""

# Import all we need
import os
from users.chat_users import ChatUsers, ChatUser
from users.chat_history import ChatHistory
from config.configuration import Configuration

# Default configuration file name has user/history file names
CONFIG_FILE = "./configuration.json"

# Create items we need
config = Configuration(CONFIG_FILE)
all_history = ChatHistory(config.get_history_file())
all_users = ChatUsers(config.get_user_file())

"""
Program functions
"""


def show_folder(context):
    print("Folder View: ", context["current_folder"])
    if context["current_folder"] == 'inbox':
        context["chat_user"].show_inbox()
    else:
        context["chat_user"].show_sent()


def show_message(context, id):
    if context["current_folder"] == 'inbox':
        context["chat_user"].show_inbox_msg(id)
    else:
        context["chat_user"].show_sent_msg(id)


"""
Context and states

    State:
        0 - show folder list
            v - view "inbox" or "sent"
                Set current folder
            n - new message
                Show input for new message
        1 - View folder content
            s - show specific message
            b - go back
"""
context = {
    "chat_user": None,
    "current_folder": None,
    "state": 0
}

# Have to create a user....
user_name = input("Enter your name to start chatting: > ")
all_folders = ["inbox", "sent"]
context["chat_user"] = ChatUser(user_name, all_users, all_history)

state_0 = """View a folder or send a message by entering:
    inbox OR sent -> View one of these folders
    n             -> Create a new message
    q             -> Quit program"""
state_1 = """View a folder or send a message by entering:
    N             -> Message number to view
    b             -> Go back
    q             -> Quit program"""


# Start program
user_option = None
while user_option not in ['q', 'Q', 'quit', 'Quit', 'QUIT']:

    if context["state"] == 0:
        os.system('cls')
        print(state_0)
        user_option = input("Enter your option: > ")

        if user_option.lower() in all_folders:
            os.system('cls')
            context["current_folder"] = user_option.lower()
            context["state"] = 1
            show_folder(context)
        elif user_option.lower() == 'n':
            os.system('cls')
            recip = input("Who is this message to? > ")
            msg = input("Type message to user (no newlines):\n")
            context["chat_user"].send_message(recip, msg)

    elif context["state"] == 1:
        print(state_1)
        user_option = input("Enter your option: > ")

        if user_option.lower() == 'b':
            context["state"] = 0
        else:
            try:
                msg_num = int(user_option)
                os.system('cls')
                show_message(context, msg_num)
                input("Enter any key to continue...")
                os.system('cls')
                show_folder(context)
            except Exception as ex:
                pass