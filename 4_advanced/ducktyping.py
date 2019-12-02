'''
    Python has something called "duck typing". It's not special, but the idea is

        "If it walks like a duck and quacks like a duck, it's a duck"

    Because nothing is strongly typed (like C, C++, C#, Java) you can pass anything
    anywhere you want. 

    This is super flexible for developers, but it's also sometimes difficult to figure out
    what you should be passing along.

    For flexibility, see the example below. If you want to understand classes, see classes.py
    first. 

    We will create two different classes of differnt types, than call a function on those
    interfaces....and they both will work.
'''

class Orange:
    def __init__(self):
        self.color = "orange"
    
class Elephant:
    def __init__(self):
        self.color = "gray"

# Now we'll iterate over a list of two different objects and 
# get the attribute "color". Since the both have a "color" attribute
# this works....
object_list = [Orange(), Elephant()]
for obj in object_list:
    print("Type = ", type(obj), " Color = ", obj.color)
