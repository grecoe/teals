'''
    Almost any application you ever write will include the need to save some sort of configuration.

    This example creates a base class GenericConfigurationArchive that will load/save ANY class
    to disk.

    We then create another simple configuration Configuration and practice with it.
'''

import json
import datetime
import os


class GenericConfigurationArchive:
    """
        Non instaniable base class. Configuration classes that want save/load functionlity
        just derive from this class and directly implement save/load

        I there they call GenericConfigurationArchive.XXX(self) to get to load/save here
        that requires the super class information (name/dict)

        A json file with the class name is is created in the current directory so many classes
        in the same application can create thier own saved state.
    """
    ARCHIVE_FMT_NAME = "{}.json"
    ARCHIVE_CLASS = "classname"
    ARCHIVE_DATA = "data"

    def __init__(self):
        """
            Do NOT allow this class to be called directly.
        """
        raise NotImplementedError("Cannot instantiate this class directly!")

    def save(self):
        """
            Create a json file with superclass class name.json with the contents
            of it's __dict__ in the output.
        """
        conf_name = GenericConfigurationArchive.ARCHIVE_FMT_NAME.format(
            type(self).__name__
        )

        self.__dict__['saved'] = str(datetime.datetime.utcnow())

        settings = {
            GenericConfigurationArchive.ARCHIVE_CLASS: type(self).__name__,
            GenericConfigurationArchive.ARCHIVE_DATA: json.dumps(self.__dict__)
        }

        with open(conf_name, "w") as archived:
            archived.writelines(json.dumps(settings, indent=4))

    def load(self):
        """
            Loads a json file with superclass class name.json. File should follow
            the expected format:

            1. Class is not of type of the same super class - ignore file
            2. File may not even exist.
            3. It exists and the type is correct, extend the class __dict__ with
            the content from the file.
        """
        return_config = False

        conf_name = GenericConfigurationArchive.ARCHIVE_FMT_NAME.format(
            type(self).__name__
        )

        if os.path.exists(conf_name):
            file_content = None
            with open(conf_name, "r") as archived:
                file_content = archived.readlines()
                file_content = "\n".join(file_content)

            if file_content:
                settings = json.loads(file_content)

                config_type = settings[GenericConfigurationArchive.ARCHIVE_CLASS]
                config_type = eval(config_type)

                # Is this the right type?
                if (isinstance(self, config_type)):
                    # We could create one like this...
                    # return_config = config_type()
                    loaded_dict = json.loads(settings[GenericConfigurationArchive.ARCHIVE_DATA])

                    # Check for type?
                    loaded_dict["loaded"] = str(datetime.datetime.utcnow())
                    self.__dict__.update(loaded_dict)
                    return_config = True

        return return_config


class Configuration(GenericConfigurationArchive):
    """
        First configuration file for testing. Extend the class variables that makes
        sense for your application.

        Creates Configuration.json
    """
    def __init__(self):
        self.Name = "Dan"
        self.Age = 99

    def save(self):
        GenericConfigurationArchive.save(self)

    def load(self):
        GenericConfigurationArchive.load(self)


class Configuration2(GenericConfigurationArchive):
    """
        Second configuration file for testing. Extend the class variables that makes
        sense for your application.

        Creates Configuration2.json
    """
    def __init__(self):
        self.Address = "123 main street"
        self.Number = 27

    def save(self):
        GenericConfigurationArchive.save(self)

    def load(self):
        GenericConfigurationArchive.load(self)


conf = Configuration()
conf2 = Configuration2()
# Load may or may not update. If conf file si not there
# or the format is for the wrong type, it's ignored.
conf.load()
conf2.load()
# Do work and save
print(conf.Name, conf2.Address)

# Whatever happened we are saving where we are now.
conf.save()
conf2.save()

# More work but don't save
conf.Name = "Steve"
conf2.Address = "456 High Street"

print(conf.Name, conf2.Address)

# Loading will overwrite the internal dict and put us back to where
# we were before the modifications above.
conf.load()
conf2.load()
print(conf.Name, conf2.Address)
