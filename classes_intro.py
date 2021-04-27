
"""
    To now we've used parameters, but those aren't really efficient
    if we want to track multiples. Imagine if we had 3 dogs we were
    trying to keep track of...it gets complicated to go after
    the right variables...what happens when we get to 10?
"""

dog1_name = "Fido"
dog1_sound = "Woof"
dog2_name = "Rover"
dog2_sound = "Woof"
dog3_name = "Steve"
dog3_sound = "Woof"




"""
    Classes are another data structure that we can use to hold both
    members (data) and methods (functions) that relate to one specific
    type of thing.

    You create a class by using the 'class' keyword in Python
"""
class Animal:
    """ Represents an animal """

"""
    You create an 'instance' of a class just by using the class name
    followed by parenthesis.
"""
firstanimal = Animal()

"""
    Python "magic" allows us to just add properties to our animal using
    dot notation and setting a value. This is very much like adding something
    to a dictionary
"""
firstanimal.name = "Fred"
print("Our first animal name is:")
print("firstanimal.name = ", firstanimal.name)

"""
    Now, that's your first class you've made....but the Animal class isn't
    very useful for anyone because it's declaration (where we defined it)
    doesn't include any members (data) so a user has NO idea how to use it.

    Here is another important part, a class is "constructed" when we use it's
    name and parenthesis.

    When we do so, Python is looking for a function on the object called __init__
    which is called the class "constructor". If the class has one, it's called.

    BUT for every function, including __init__ on a class we MUST have the first
    argument be 'self'. This instructs Python that we want to work on ourself
    (the instance of the class) when we do anything.

    With this in mind, lets create a new class called Dog that has a constructor.
    The constructor is going to take in the name and sound that the animal makes
    as parameters to __init__.
"""
class Dog:
    def __init__(self, dog_name, dog_sound):
        self.name = dog_name
        self.sound = dog_sound

"""
    With the new declaration we can then create a dog with a name and a sound.

    Then, we can access the members (data) from the class using dot notation.
"""
first_dog = Dog("Rover", "woof")
print("Our first dog is:")
print(first_dog.name, first_dog.sound)


"""
    Great, now we have a class that has a constructor AND anyone who uses our
    class will KNOW what it's SUPPOSED to have. In this case a name and a sound.

    Going back to the first example at the top of the file, we can now track
    dogs with classes instead of global variables.
"""
dog1 = Dog("Fido", "woof")
dog2 = Dog("Rover", "WOOF")
dog3 = Dog("Steve", "Bark")

"""
    Now we have 3 dogs. Lets add them to a list and then
    run through each one
"""
print("Our list of dogs has:")
dog_list = [dog1, dog2, dog3]
for dog in dog_list:
    print("{} that says  {}".format(
        dog.name,
        dog.sound
    ))


"""
    Cool, so we've now created a class that holds onto information.

    How about a class that has another method (function) other than __init__

    Remember, ALL class functions MUST take self as the first argument
"""
class DogPound:
    def __init__(self):
        """This class takes no parameters but we can still set up a member"""
        self.dogs_in_pound = []

    def add_dog(self, dog):
        """ This function adds a dog to the pound, note that the first
        argument is self (which python will do for us) and the second is
        a dog, or a variable called dog"""
        self.dogs_in_pound.append(dog)

    def list_pound(self):
        """ This funciton will show who's in our pound, and we'll just copy
        our code from before but we will use the list dogs_in_pound to list """

        print("The Dog Pound has:")
        for dog in self.dogs_in_pound:
            print("{} that says  {}".format(
                dog.name,
                dog.sound
            ))

"""
    Granted the above class is more complicated than Animal or Dog, but
    the concepts of a constructor, members (data), and methods (functions)
    has not changed from either of those.

    Lets add our dog list to the pound and then have the pound list out
    what it has.

    This shows how we
    1. Create a pound (class construction)
    2. Add dogs to the pound (class method == function)
    3. List the pound (class method == function)
"""
pound = DogPound()      # Construct a dog pound
for dog in dog_list:    # Lets use the list from before
    pound.add_dog(dog)  # Call add_dog on the DogPound

pound.list_pound()      # Call list_pound on the DogPound


"""
    The most important things to remember here is that a class
    - Is defined using the word class before the name
    - Can have a constructor that MUST be called __init__
    - Can hold members which you SHOULD define in __init__
    - Every class function, including __init__ MUST have a first
      parameter called self.

    If the list above doesn't make sense, that's OK, classes are
    a big topic in any programming language.

    BUT, go bac to the top of this file and start reading through
    the comments again. Then, run the code, you should be able to find
    where things are getting printed and really look and try and
    understand what is going on.
"""