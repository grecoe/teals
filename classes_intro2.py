"""
    Now we've learned a few things about classes. Specifically

    - How to declare one
    - How to create one
    - Class methods ALWAYS take self as the first parameter
    - How to add members and intialize them with __init__

    Now some more extended functionality. In particular how to use
    some other overrides in Python classes, and further still, how
    a class can derive from another, which is called inheritance.
"""

"""
    Lets continue with the classes we already defined in the first class
    on classes, specifically Dog and DogPound.

    Dog remains unchanged, but look at DogPound with some pretty specific changes.

    1. __add__ overrides the default Python implementation
    2. __str__ which is called every time the object is accessed as a string
"""
class Dog:
    def __init__(self, dog_name, dog_sound):
        self.name = dog_name
        self.sound = dog_sound


class DogPound:
    def __init__(self):
        self.dogs_in_pound = []

    def __add__(self, dog):
        """ This allows you to add to the pound like

        pound += dog
        """
        self.dogs_in_pound.append(dog)
        return self

    def __str__(self):
        """ Called anytime someone wants a string of the class"""
        return_value = ""
        for dog in self.dogs_in_pound:
            return_value += "{} that says {}\n".format(
                dog.name,
                dog.sound
            )
        return return_value

"""
    Now lets test this out...very different from the last one.
    Notice we can use += on the pound to add a dog and we don't
    need to do anything to print out the pound as a string we
    just access it with print, which will call __str__
"""
pound = DogPound()
pound += Dog("Rover", "bark")
pound += Dog("Biff", "yelp")
print("Pound Content:\n{}".format(pound))

"""
    Ok, mind blown right? But like one of those TV adds....

    "Wait, theres more!"

    Inheritance, this is how a lot of programming problems are solved.
    We use something called a "base" class that holds common functionality
    of two similar things.

    For this example, lets keep going with dogs. We can have big dogs and
    little dogs..

    Inheritance is declared with the class declaration as

    class ClassName(DerivingClass)

    Now your class has all the same functionality of the base class.
"""

class BigDog(Dog):
    def __init__(self, name, sound):
        """ Because Dog has a constructor that takes arguments
        we have to call it's constructor.
        We do that by using super() which finds the deriving class
        and then we call it's __init__ directly.
        The only thing we change is the sound, big dogs are loud so
        we will upper case whatever it says.
        """
        super().__init__(name, sound.upper())


"""
 Now we'll do the following
 - Create a BigDog
 - Add it to the pound
 - Print the pound

 Note that we just add a big dog like a regular dog and the pound still
 has everything we added before.
"""
bd = BigDog("Ralf", "bark")
pound += bd
print("Pound Content:\n{}".format(pound))


"""
    BONUS - If time permits

    We can also use a python function to determine if the object we have
    is a type of object we want to work with.

    That is 'isinstance' and we give it two arguments
        1. The object we want to inspect
        2. The type we are checking for

    We can play with this using the dog pound - dogs_in_pound

    NOTE: This is a really advanced idea, so it is totally fine if this
    confuses you...some people in Computer Science programs struggle with
    this....
"""

for dog in pound.dogs_in_pound:
    print("{} is of type {}, and is instance of a dog? {}".format(
        dog.name,
        type(dog),
        isinstance(dog, Dog)
    ))

"""
    Takeaway - Ralf is a BigDog, but BigDog derives (inherits) from
    Dog....so Ralf is a Dog after all because Dog is in the inheritance
    chain.
"""
