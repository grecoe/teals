"""
(c) Microsoft. All rights reserved.
"""
import typing
from .factory_exception import FactoryException


class FactoryMissingArgException(FactoryException):
    """
    Exception when the incoming type does not match the expected type
    """
    def __init__(self, klass, arg: str):
        err = "Missing argument {} for for {}".format(
            arg,
            str(type(klass))
        )
        super().__init__(err)
