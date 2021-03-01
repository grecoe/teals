import os
import json


class FileBase:

    def __init__(self):
        self.file = None
        self.settings = None

    def load_file(self):
        self.verify_file(self.settings)

        with open(self.file, 'r') as settings_file:
            settings = settings_file.readlines()
            self.settings = json.loads("\n".join(settings))

    def verify_file(self, default_value):

        if not os.path.exists(self.file):
            path_parts = os.path.split(self.file)

            # Is it the directory?
            if not os.path.exists(path_parts[0]):
                os.makedirs(path_parts[0])

            # Is it the file?
            if not os.path.exists(self.file):
                with open(self.file, "w") as file_info:
                    file_info.writelines(json.dumps(default_value))

    def save(self):
        self.verify_file(self.settings)
        with open(self.file, "w") as file_info:
            file_info.writelines(json.dumps(self.settings, indent=4))
