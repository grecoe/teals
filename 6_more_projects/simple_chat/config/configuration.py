import json


class Configuration:
    CONFIG_USERS = 'user_file'
    CONFIG_HISTORY = "history"

    def __init__(self, config_file):
        self.config_file = config_file
        self.data = None

        self._load()

    def get_history_file(self):
        return self.data[Configuration.CONFIG_HISTORY]

    def get_user_file(self):
        return self.data[Configuration.CONFIG_USERS]

    def _load(self):
        with open(self.config_file, "r") as config:
            self.data = config.readlines()

        if self.data:
            self.data = json.loads("\n".join(self.data))
