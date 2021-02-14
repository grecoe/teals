"""
    Configuration is used to save a python dictionary or string to a
    file in JSON format. Simply pass in the name of the file for
    your configuration and an object that can be serialized by the json
    library (dict, list)
"""

import json
import os


def load_configuration(config_file: str):
    return_object = None

    if os.path.exists(config_file):
        with open(config_file, 'r') as config:
            data = config.readlines()
            return_object = json.loads("\n".join(data))

    return return_object


def save_configuration(config_file: str, data: object):
    with open(config_file, 'w') as config:
        config.writelines(json.dumps(data, indent=4))


# Create objects to write
config_1 = [1, 2, 3, 4, 5]
config_2 = {"name": "Joe", "class": 2023}

# Write them out
save_configuration("config1.json", config_1)
save_configuration("config2.json", config_2)

# Load up what you wrote
loaded_config_1 = load_configuration("config1.json")
loaded_config_2 = load_configuration("config2.json")

# Compare them
print(config_1 == loaded_config_1)
print(config_2 == loaded_config_2)

