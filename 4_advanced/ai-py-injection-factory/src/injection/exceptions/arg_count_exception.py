"""
(c) Microsoft. All rights reserved.
"""
import typing
from .factory_exception import FactoryException


class FactoryArgCountException(FactoryException):
    """
    Exception when the incoming type does not match the expected type
    """
    def __init__(self, klass, expected: int, actual: int):
        err = "Invalid arg count for {} - expected {} but have {}".format(
            str(type(klass)),
            expected,
            actual
        )
        super().__init__(err)
