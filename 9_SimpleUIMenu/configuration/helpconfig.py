import json
from os import path
from uuid import uuid4


class GenericObject:
    def __init__(self, dict_settings):
        for key in dict_settings:
            setattr(self, key, dict_settings[key])


class TopicConfiguration:
    def __init__(self, parent):
        self.parent = parent
        self.children = []


class HelpConfig:
    def __init__(self, config_file):
        self.config_file = config_file
        self.configurations = []

        # If configuration object doesn't exist, throw
        if not path.exists(config_file):
            raise Exception("Config file {} does not exist".format(config_file))

        # Load data and create a JSON object
        file_data = None
        with open(config_file, 'r') as data_file:
            file_data = data_file.readlines()

        file_data = json.loads("\n".join(file_data))

        for parent in file_data:
            parent['id'] = str(uuid4())
            topic_config = TopicConfiguration(GenericObject(parent))

            for child in parent['children']:
                child['id'] = str(uuid4())
                topic_config.children.append(GenericObject(child))

            self.configurations.append(topic_config)

    def find_topic(self, topic_name):

        return_result = None
        for topic in self.configurations:
            if topic.parent.name == topic_name:
                return_result = topic.parent
                break

            found = [x for x in topic.children if x.name == topic_name]
            if len(found):
                return_result = found[0]
                break

        return return_result
