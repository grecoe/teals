'''
    With a basic understanding of classes (classes.py), the next step is to
    show class derivation.

    That is, one class that derives from another.

    This approach can be very useful when you have similar types of objects, with
    similar properties and/or methods to act on them.

    For instance, lets take parts from a car. Every part has a part number, cost,
    name, etc. But each part is going to be different.

    But, we don't want to copy all the similar things from one class to the next.
    To solve that problem we derive classes.
'''


class BasePart:
    '''
        The base part class. Every part will 'derive' from this class
    '''
    def __init__(self, name, part_no, cost):
        self.name = name
        self.part_number = part_no
        self.cost = cost


class Muffler(BasePart):
    '''
        The muffler derived from BasePart
    '''
    def __init__(self):
        # Initialize the parent (BasePart) class
        super().__init__("Muffler", '12ab78t', 149.99)

        # Now what does a muffler have?
        self.length_inches = 60


'''
    Now create a muffler part, get it's name and length
'''
muf = Muffler()
print(muf.name, muf.length_inches)


'''
    Multiple inheritance works from one class through another
'''


class Base:
    def __init__(self):
        print("Base")

    def printme(self):
        print(self.d1)


class Derive1(Base):
    def __init__(self):
        super().__init__()
        print("Derive1")
        self.d1 = "Derive1"


class Derive2(Derive1):
    def __init__(self):
        super().__init__()
        print("Derive2")


'''
    Create a Derive2 instance.

    What do you think will be printed?
'''
cd2 = Derive2()
cd2.printme()
