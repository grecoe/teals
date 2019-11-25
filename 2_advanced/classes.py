'''
    Classes are structures that contain it's own properties and methods. 

    This can be extremely useful for many scenarios, but is definitely way out of scope for
    an introduction class. 

    However, understanding them as your skills improve is never a bad thing. This example is 
    very very simple and we will not cover any of the deeper topics of classes. 
'''

# Create a class for a person
class Person:

    # Ever class function has a first parameter called 'self'. This function, __init__ is called
    # the constructor. Constructors are the first method called when the object is created.
    def __init__(self, name, age ):
        # We can just come up with names for variables (properties) as we want. These become available
        # to any external callers.
        self.name = name
        self.age = age

    # Set up a method on the class. Don't forget the self parameter and you can access inside the 
    # class.
    def canDrive(self):
        if self.age > 17:
            return True
        return False

# Now create some instances
person1 = Person("Pete", 15)
person2 = Person("Mary", 27)
person3 = Person("Agnes", 99)
person4 = Person("Joely", 10)

print(person1.name, "can drive?", person1.canDrive())

# Now add them to a list and figure out, use list comprehension who can drive....
people = [person1, person2, person3, person4]

# Use list comprehension
print("Who can drive?")
drivers = [x for x in people if x.canDrive()]
for driver in drivers:
    print(driver.name)