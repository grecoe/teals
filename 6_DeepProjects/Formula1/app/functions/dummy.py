'''
    Simple implementation of the IFunction as an example.
'''

from app.functions.interface import IFunction, argument_definition

class DummyFunction(IFunction):
    def __init__(self, datasets):
        super().__init__(
            datasets,
            [
            argument_definition('-n',True, 'Name of driver'),
            argument_definition('-x',False, 'Something Else')
            ])

    def execute(self, args):
        try:
            # This call validates inputs. If a required arg isn't there 
            # or an additional, unexpected, arg is present it will except.
            execute_args = super()._parse_execute_arguments(args)

            # At this point, you're clear and ready to go. 
            print(execute_args, "dummy execute")
        except Exception as ex:
            print(str(ex))
