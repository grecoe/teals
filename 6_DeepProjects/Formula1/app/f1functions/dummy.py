'''
    Simple implementation of the IFunction as an example.
'''

from app.utils.interface import IFunction, argument_definition

class DummyFunction(IFunction):
    def __init__(self, datasets):
        super().__init__(
            datasets,
            # Define the arguments you will accept, -h is a default for all.
            [
            argument_definition('-n',True, 'Name of driver'),
            argument_definition('-x',False, 'Something Else')
            ])

    def execute(self, args):
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

        except Exception as ex:
            print(str(ex))
