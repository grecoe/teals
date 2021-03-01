from users.file_base import FileBase
from visual.display import Display


class ChatUser:
    def __init__(self, name, users, history):
        self.user_util = users
        self.msg_history = history
        self.name = name

        if not self.user_util.user_known(self.name):
            self.user_util.add_user(self.name)

    def show_inbox(self):
        """
        Get and display inbox message
        """
        msgs = self._load_messages(True)
        Display.display_message_list(msgs, True)

    def show_inbox_msg(self, msg_num):
        """
        Show an individual inbox message
        """
        msgs = self._load_messages(True)
        Display.display_message(msgs[msg_num - 1])

    def show_sent(self):
        """
        Get and display sent messages
        """
        msgs = self._load_messages(False)
        Display.display_message_list(msgs, False)

    def show_sent_msg(self, msg_num):
        """
        Show an individual sent items message
        """
        msgs = self._load_messages(False)
        Display.display_message(msgs[msg_num - 1])

    def send_message(self, user_name, message):
        """
        Send a message to a user
        """
        self.msg_history.send_message(self.name, user_name, message)

    def _load_messages(self, inbox=True):
        msgs = []
        if inbox:
            msgs = self.msg_history.get_inbox_history(self.name)
        else:
            msgs = self.msg_history.get_sent_history(self.name)

        return msgs


class ChatUsers(FileBase):

    def __init__(self, user_file):
        self.file = user_file
        self.settings = []
        self.load_file()

    def user_known(self, user_name):
        return user_name in self.settings

    def add_user(self, user_name):
        if not self.user_known(user_name):
            self.settings.append(user_name)
            self.save()
