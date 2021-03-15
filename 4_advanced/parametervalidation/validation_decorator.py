"""
    Validating function/method inputs can prevent many problems down the road
    once software has been released. This quick and somewhat painless process
    can be achieved either through several lines of validation code in each 
    method or can be managed in Python by decorating a function with the 
    ParameterValidator below. 

    This class can be used with:
    - Stand alone methods 
    - Class methods
    - Regardless of method type, it can validate:
        - Methods with a set number of arguments
        - Methods that rely on kwargs for arguments. 
"""
import typing
from parameter_exception import ParameterTypeValidationException

class ParameterValidator:
    """
    Function decorator to validate arguments to a function. This can be used
    to ensure that parameters are (1) present, (2) meet a type requirement and
    (3) actually have a value and are not None (if desired)

    For functions that expect a set number of arguments, you seed the class with 
    a free formed list of tuples that are in the form
    (
        Argument expected type,
        Boolean - true = can be None, false = must be present
    )

    i.e. ( (int, True), (str, False), (list, True))

    For functions that expect to use the kwargs for variable arguments you can also
    validate that certain required fields are always in the input with a slight change
    to the above format, you set up kwargs using the name of the field expected with 
    the same format above.

    i.e. ( age=(int, True), name=(str, False), addresses=(list, True))
    """
    def __init__(self, *args, **kwargs):
        """
        Collect the parameters passed to this instance for future 
        validation against the calling function.
        """
        self.validation_args = args
        self.validation_kwargs = kwargs

    def __call__(self, func):
        """
        Returns a wrapper to the function that when called it will validate
        the parameters for the given call. 

        This works with both standalone and class methods.

        Parameters:
        func: The calling function

        Returns:
        wrapper function that will be called when the subscribed function
        is called.
        """
        def wrapper(*args, **kwargs):
            """
            Wraps an existing function and validates the parameters passed in meet
            the rules set forth when declaring the instance of ParameterValidator.

            Parameters:
            args: The list of arguments passed to the method
            kwargs: The dictionary of arguments passed into the method

            Returns:
            Whatever the original function returns.

            Throws:
            ParameterTypeValidationException if there is an issue 
            """
            args_to_validate = args
            if len(args) and func.__qualname__.startswith(args[0].__class__.__name__):
                # This is a class method and we do NOT want to validate self.
                args_to_validate = args[1:]

            if len(args_to_validate) and (len(args) != func.__code__.co_argcount):
                err = "Func {} in {} expects {} parameters but {} were given.".format(
                    func.__qualname__,
                    func.__module__,
                    func.__code__.co_argcount,
                    len(args)
                )
                raise ParameterTypeValidationException(err)
            
            if len(args_to_validate):
                self._validate_args_arguments(func, args_to_validate, self.validation_args)
            elif len(kwargs) and len(self.validation_kwargs):
                self._validate_kwargs_arguments(func,kwargs,self.validation_kwargs )
            else:
                err = "There are no present arguments for Func {} in {}".format(
                    func.__qualname__,
                    func.__module__
                )
                raise ParameterTypeValidationException(err)

            return func(*args, **kwargs)
        return wrapper

    def _validate_args_arguments(self, func : object, call_arguments : typing.List[object], validation_args : typing.List[tuple]):
        """
        Validation for functions that take in an *args set of arguments. These must be a 
        known set of arguments as defined in the method declaration.

        Parameters:
        func : The calling function
        call_arguments: The list of provided arguments to the method.
        validation_args: The list of tuples for validation, but cannot be the kwargs validation.

        Returns:
        None

        Throws:
        ParameterTypeValidationException if there is an issue 
        """
        param_index = 1
        for (argument, validation) in zip(call_arguments, validation_args):
            self._validate_argument(param_index, func, argument, validation)
            param_index += 1        

    def _validate_kwargs_arguments(self, func: object, call_arguments : typing.Dict[str, object], validation_args : typing.Dict[str,tuple]):
        """
        Validates the kwargs against the validation kwargs passed in.
        
        Parameters:
        func: The calling function
        call_arguments: The kwargs passed to the function
        validation_args: The kwargs passed to this instance

        Returns:
        None

        Throws:
        ParameterTypeValidationException if there is an issue 
        """
        param_index = 1
        for expected_arg in validation_args.keys():
            # Overload the boolean in the validation, if it's True and not present
            # this is not an error. 
            if (not validation_args[expected_arg][1]) and (expected_arg not in call_arguments):
                err = "Expected kwarg {} not present in call to func {} in {}".format(
                    expected_arg,
                    func.__qualname__,
                    func.__module__
                )
                raise ParameterTypeValidationException(err)
            elif validation_args[expected_arg][1] and (expected_arg not in call_arguments):
                # Allowed None (or not present) and not there. no error.
                pass
            else:
                self._validate_argument(
                    param_index, 
                    func, 
                    call_arguments[expected_arg],
                    validation_args[expected_arg])
            param_index += 1

    def _validate_argument(self, param_index : int, func : object, argument : object, validation : tuple):
        """
        Performs the actual validation on an incoming argument value and the corresponding
        validation tuple (holding type information and bool which identifies whether None
        values are accepted)

        Parameters:
        - param_index : Index of this parameter. Useful for args type calls, less so with
                        kwargs type calls. 
        - func : Calling function 
        - argument : Actual value passed in
        - validation : Tuple with type and None type acceptance

        Returns:
        None

        Throws:
        ParameterTypeValidationException if there is an issue 
        """
        if not validation[1] and (argument == None):
            # Not allowed None but is
            err = "Func {} in {}, parameter {} not allowed null but is.".format(
                func.__qualname__,
                func.__module__,
                param_index
            )
            raise ParameterTypeValidationException(err)
        elif validation[1] and argument == None:
            pass
        elif not isinstance(argument, validation[0]) :
                err = "Func {} in {}, parameter {} type does not match {} != {}.".format(
                    func.__qualname__,
                    func.__module__,
                    param_index,
                    str(type(argument)),
                    str(validation[0])
                )
                raise ParameterTypeValidationException(err)





"""
    Test this out with both a standalone function and a class with a method
    that is decorated.
"""        

# Test standalone method with a set number of arguments
@ParameterValidator((int, False), (str, False), (list, True))
def myfunc(num, str, list):
    print("Hello from standalone function")

# Splatting
single_args = [1,"hey", None]
print("Standalone Args Splatting -")
myfunc(*single_args)  

# Standard call
print("Standalone Args Standard -")
myfunc(1,"hey", None)

# Test standalone method with kwargs
@ParameterValidator(age=(int, False), name=(str, False), addresses=(list, True))
def mykwfunc(**kwargs):
    print("Hello from kwargs standalone function")
print("Standalone Kwargs Standard -")
mykwfunc(age=25, name="Fred Jones")

# Test with a class using both args and kwargs
class TestDecorator:
    def __init__(self):
        pass

    @ParameterValidator((int, False), (str, False), (list, True))
    def myfunc(self, num : int, str : str, list : typing.List[object]):
        print("Hello from class method")

    @ParameterValidator(age=(int, False), name=(str, False), addresses=(list, True))
    def mykwfunc(self, **kwargs):
        print("Hello from kwargs standalone function")

td = TestDecorator()
print("Class Args Standard -")
td.myfunc(1,"str", [])
print("Class Kwargs Standard -")
td.mykwfunc(age=25, name="Fred Jones")
