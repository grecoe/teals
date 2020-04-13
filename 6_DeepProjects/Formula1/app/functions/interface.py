'''
    Functionality called by the application are instances of IFunction derived
    classes. 

    Application functionality can be encapsulated with this template as it handles
    containing datasets, argument parsing and providing help. This means that
    the derived classes do NOT need to implement that. 

    The IFunction class encapsulates several useful features:
        - Contains the datasets needed for any functionality
        - Contains the arguments that the deriving function needs.
        - Manages printing out the help information.
        - Manages parsing additional parameters for a function. 
        - Identifies an 'abstract' call execute(args) for derived classes
          to implement the specific functionality.  
'''
import collections

argument_definition = collections.namedtuple("arg", 'arg required definition')

class IFunction:
    DRIVER_DATA = 'driver'
    RACE_DATA = 'races'
    RESULTS_DATA = 'results'
    STATUS_DATA = 'status'
    CONSTRUCTOR_DATA = 'constructor'

    def __init__(self,datasets, acceptable_arguments):
        self.arguments = acceptable_arguments
        self.datasets = datasets

    def execute(args):
        """
            Deriving functions must implement this function. This is where
            the actual work for the function resides. 
        """
        raise Exception("execute not implemented")

    def get_help(self, indent, command_list = None):
        """
            Using the internal self.arguments, prints out the
            help for the deriving function. 

            command_list, if present, is the path the application took 
            to get to this function. 

            indent is used to determine how much to indent the output. 

            Output consists of the parameters and the parameters definition
            identified by self.arguments (a list of argument_definition objects)        
        """
        indent_spaces = '   ' * indent
        parameters = self._format_help()

        if len(command_list):
            command_line = "Command : '{}'".format(' '.join(command_list))
            print(indent_spaces, command_line)
        print(indent_spaces, "Parameters:")

        for param in parameters:
            print(indent_spaces, param)

    def _format_help(self):
        """
            Internal function to format the arguments to be printed
            when help is called. 
        """
        return_args = []
        if len(self.arguments) == 0 :
            return_args.append("Option takes no parameters")
        else:
            for arg in self.arguments:
                return_args.append('  {} : {}'.format(arg.arg, arg.definition))

        return return_args

    def _parse_execute_arguments(self, args):
        """
            Internal function that will parse off the additional parameters
            passed to a specific function. 

            args represents the remaining command line that started the 
            function execution. 

            Returns a dictionary with arguments and optional values. 

            NOTE:
                The function determines if required parameters are present. If
                not an exception is thrown. 

                Further, if additional arguments are provided that the function 
                does not support, an exception is thrown. 
        """
        arguments = {}
        current_argument = None
        argument_list = []
        for arg in args:
            arg = arg.strip()
            if len(arg) == 0 :
                continue

            if arg.startswith('-'):
                if len(argument_list) and current_argument:
                    arguments[current_argument] = " ".join(argument_list)
                current_argument = arg.lower()
                arguments[arg] = None
                argument_list = []
            else:
                argument_list.append(arg)

        # Make sure we don't miss any....
        if len(argument_list) and current_argument:
            arguments[current_argument] = " ".join(argument_list)

        # Validate the arguments, if any requireds are not present
        # throw an exception
        # Make sure any required arg is there
        for arg in self.arguments:
            if arg.required and arg.arg not in arguments.keys():
                raise Exception("Required arg {} not present, try help".format(arg.arg))
        
        # Now make sure there isn't anything we didn't expect
        allowed_args = [arg.arg for arg in self.arguments]
        for provided_arg in arguments.keys():
            if provided_arg not in allowed_args:
                raise Exception("Invalid argument present : {} , try help".format(provided_arg))
        return arguments
