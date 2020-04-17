'''
    Simple implementation of the IFunction as an example.
'''
import sys
from multi_command_utils.interface import IFunction, argument_definition

class DummyFunction(IFunction):
    def __init__(self, datasets):
        super().__init__(
            datasets,
            # Define the arguments you will accept, -h is a default for all.
            [
            argument_definition('-n',False, 'Name of driver'),
            argument_definition('-o',False, 'Something Else'),
            argument_definition('-t',False, 'Something Else'),
            argument_definition('-i',False, 'Something Else'),
            argument_definition('-m',False, 'Something Else'),
            argument_definition('-p',False, 'Something Else'),
            ])

    def execute(self, args):
        output_file = None
        orig_output = sys.stdout

        try:
            # This call validates inputs. If a required arg isn't there 
            # or an additional, unexpected, arg is present it will except.
            execute_args = super()._parse_execute_arguments(args)

            if IFunction.GLOBAL_HELP in execute_args.keys():
                # Regardless of anything else, if help is there, show it and quit
                self.get_help(1)
            else:

                # At this point, you're clear and ready to go. 
                # This is where all your logic goes. 
                print(execute_args, "dummy execute")

                if '-o' in execute_args.keys():
                    output_file = open(execute_args['-o'], 'w')
                    sys.stdout = output_file
                
                print("This is a test")

        except Exception as ex:
            print(str(ex))

        finally:
            if output_file:
                output_file.close()
                sys.stdout = orig_output
