"""
    Typing helps your API/SDK users know what they should be expecting to pass 
    and recieve from calling a method.

    Unlike languages like C#, Java, etc.... Python won't enforce method types. 
    Including typing is just a HINT.

    A HINT because Python uses duck typing. 
    
    If it's critical for your code to have something specific you SHOULD validate it. 
"""
import typing


def validated_check(selector : int, message : typing.Dict[str,str]) -> None:
    if not isinstance(selector, int):
        print("This should THROW because of a type mismatch - selector")
        return
    if not isinstance(message, dict):
        print("This should THROW because of a type mismatch - message")
        return

    print("All looks good here!")        

# Uh-oh......
validated_check(3, "Foo bar")
# OK
validated_check(3, {"some" : "value"})
