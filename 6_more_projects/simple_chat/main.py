"""
    Advanced using classes

    This is a program that mimics a very simple chat program. Several classes
    have been created for you to use:

    ChatUsers   - Class on top of file that holds all user names
    ChatUser    - A single user of the program. Provide a name and then you can
                  view thier inbox, sent folder and send messages.
    ChatHistory - Class on top of a file that holds all chat history from all users.
    ChatMessage - Class that represents a single message.
    Display     - Class used by ChatUser to show Inbox/SentItems

    Assignment:
        Write a program that a user would use to "chat" with other users.
        1. Ask for the user name
        2. Create a ChatUser from that name.
        3. Provide a menu for the user to:
            - Show inbox
                Display only shows headers, so allow them to choose a message to view. This can
                apply to sent items as well.
            - Show sent items
            - Send a message
            - Quit

        With this, you should be able to launch two instances of this application with
        two command prompts.

        For each instance, seed it with a different name and then send messages back and
        forth between them. You should be able to see inbox
"""
import json
from users.chat_users import ChatUsers, ChatUser
from users.chat_history import ChatHistory


CONFIG_FILE = "./configuration.json"
CONFIG_USERS = 'user_file'
CONFIG_HISTORY = "history"


def load_configuration():
    global CONFIG_FILE

    data = None
    with open(CONFIG_FILE, "r") as config:
        data = config.readlines()

    if data:
        data = json.loads("\n".join(data))

    return data


config = load_configuration()
all_history = ChatHistory(config[CONFIG_HISTORY])
all_users = ChatUsers(config[CONFIG_USERS])

user = ChatUser("Dan", all_users, all_history)
user2 = ChatUser("Sue", all_users, all_history)

# User 1 sends a message to user 2
# user.send_message(user2.name, "This is a another longer test test")

print("{} sent".format(user.name))
user.show_sent()
user.show_sent_msg(1)
print("{} recieved".format(user2.name))
user2.show_inbox()
user2.show_inbox_msg(1)
