from os import path
import json

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
        with open(config_file,'r') as data_file:
            file_data = data_file.readlines()

        file_data = json.loads("\n".join(file_data))

        # Find all parent nodes, i.e. 'parent' is null
        parent_nodes = [x for x in file_data if not x['parent']]

        # Build up topic configuraitons by pairing children with parent
        for parent in parent_nodes:
            topic_config = TopicConfiguration(GenericObject(parent))

            child_nodes = [x for x in file_data if x['parent'] == topic_config.parent.id]
            for child in child_nodes:
                topic_config.children.append(GenericObject(child))

            self.configurations.append(topic_config)