from multi_command_utils.interface import IFunction, argument_definition

class ExampleFunction(IFunction):
    def __init__(self):
        super().__init__(
            # We are NOT going to pass additional information to the IFunction
            # base class for this example. 
            None,
            # Define the arguments you will accept, -h is a default for all.
            [
                argument_definition('-o',False, 'Option 1'),
                argument_definition('-o2',False, 'Option 2')
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
                print(execute_args, "ExampleFunction.execute()")

        except Exception as ex:
            print(str(ex))
