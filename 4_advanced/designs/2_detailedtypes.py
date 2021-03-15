"""
    For methods that take discrete values for method parameters, 
    consider forcing that selection with an enum. 
"""
import typing
from enum import Enum

class Selector(Enum):
    """
    Discrete selections for XXX
    """
    FileSystem = 1
    AppInsights = 2


def validated_check(selector : Selector, message : typing.Dict[str,str]) -> None:
    if not isinstance(selector, Selector):
        print("This should THROW because of a type mismatch - selector")
        return
    if not isinstance(message, dict):
        print("This should THROW because of a type mismatch - message")
        return

    print("All looks good here!")        

validated_check(3, "Foo bar")
validated_check(Selector.FileSystem, {"some" : "value"})