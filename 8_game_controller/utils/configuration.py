import json
from utils.tracer import TraceDecorator, Logger


class GameEntry:
    def __init__(self, dict_object):
        for key in dict_object:
            setattr(self, key, dict_object[key])


@TraceDecorator
def load_configuration(configuration_file):
    Logger.add_log("Loading configuration from: {}".format(configuration_file))

    config_settings = []
    with open(configuration_file, "r") as configuration:
        file_data = configuration.readlines()
        file_data = json.loads("\n".join(file_data))

        for entry in file_data:
            config_settings.append(GameEntry(entry))

    return config_settings
