from users.file_base import FileBase
from uuid import uuid1
from datetime import datetime
from dateutil import parser


class ChatMessage:
    def __init__(self):
        self.read = False
        self.date = None
        self.sender = None
        self.recipient = None
        self.message = None

    def parse(self, dictmsg):
        self.read = dictmsg["read"]
        self.date = parser.parse(dictmsg["date"])
        self.sender = dictmsg["sender"]
        self.recipient = dictmsg["recipient"]
        self.message = dictmsg["message"]

    def to_storage(self):
        output = {
            "read": self.read,
            "date": str(self.date),
            "sender": self.sender,
            "recipient": self.recipient,
            "message": self.message
        }
        return output


class ChatHistory(FileBase):

    def __init__(self, history_file):
        self.file = history_file
        self.settings = {}
        self.load_file()

    def get_sent_history(self, user_name):
        """
        Sent items means that the user was the sender
        """
        history = [self.settings[x] for x in self.settings if self.settings[x]["sender"] == user_name]
        history.reverse()
        return self._parse_msg_list(history)

    def get_inbox_history(self, user_name):
        """
        Inbox items means that the user was the recipient
        """
        history = [self.settings[x] for x in self.settings if self.settings[x]["recipient"] == user_name]
        history.reverse()
        return self._parse_msg_list(history)

    def send_message(self, sender, recipient, message):
        """
        Create a new chat message to be sent and send(save) it
        """
        cm = ChatMessage()
        cm.date = str(datetime.utcnow())
        cm.sender = sender
        cm.recipient = recipient
        cm.message = message
        self.settings[str(uuid1())] = cm.to_storage()
        self.save()

    def _parse_msg_list(self, msg_list):
        """
        Parse the JSON from the list to ChatMessage
        instances.
        """
        return_list = []
        for msg in msg_list:
            cm = ChatMessage()
            cm.parse(msg)
            return_list.append(cm)
        return return_list
