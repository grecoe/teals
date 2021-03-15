import typing


class ParameterValidationException(Exception):
    def __init__(self, message):
        self.message = message

    def __str__(self):
        return self.message


class ParameterNoneValidationException(ParameterValidationException):
    """
    Exception when incoming value is None but None is not allowed.
    """
    def __init__(self, func: typing.Callable[..., None], param: int):
        err = "Unexpected None value found in func {} in module {}, parameter {}.".format(
            func.__qualname__,
            func.__module__,
            param
        )
        super().__init__(err)


class ParameterTypeValidationException(ParameterValidationException):
    """
    Exception when the incoming type does not match the expected type
    """
    def __init__(self, func: typing.Callable[..., None], param: int, input_type: object, expected_type: object):
        err = "Arg type mismatch in func {} in module {}, parameter {} type does not match expected {} != {}.".format(
            func.__qualname__,
            func.__module__,
            param,
            str(input_type),
            str(expected_type)
        )
        super().__init__(err)


class ParameterKwargValidationException(ParameterValidationException):
    """
    Exception when an expected kwarg is not present
    """
    def __init__(self, func: typing.Callable[..., None], expected: str):
        err = "Missing required kwarg - {} - in func {} in module {}.".format(
            expected,
            func.__qualname__,
            func.__module__
        )
        super().__init__(err)


class ParameterCountValidationException(ParameterValidationException):
    """
    Exception when an expected kwarg is not present
    """
    def __init__(self, func: typing.Callable[..., None], recieved: int):
        err = "Expected {} args in func {} in module {} but {} were given.".format(
            func.__code__.co_argcount,
            func.__qualname__,
            func.__module__,
            recieved
        )
        super().__init__(err)
