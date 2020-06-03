from multi_command_utils.interface import IFunction, argument_definition

class CategoriesFunction(IFunction):
    def __init__(self, shopping_cart):
        super().__init__(
            shopping_cart,
            # Define the arguments you will accept, -h is a default for all.
            [
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
                print("Acceptable Categories :")

                for category in self.datasets.get_categories():
                    print("  {}".format(category))


        except Exception as ex:
            print(str(ex))
