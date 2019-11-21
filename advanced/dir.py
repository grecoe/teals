'''
    dir() gives you a directory of what is in an object and can be incredibly useful for 
    determining what the object offers.

    dir() returns a collection of attributes to iterate over

    These items are attribute names which can then further be investigated. 


    Keywords:
        dir(), getattr(), type()
'''

# Create an object to investigate
integer_value = 1

# Iterate over the attributes of the object
print("Object Attributes:")
print(type(integer_value))
for object_attribute in dir(integer_value):
    print(object_attribute)

# Investigate a little more what the attribute type is
len_less_than_7 = "\t\t\t"
len_more_than_14 = "\t"
standard = '\t\t'

print("Object Attributes With Type:")
for object_attribute in dir(integer_value):
    attribute = getattr(integer_value, object_attribute)

    # Just so printing looks OK
    spacer = standard
    if len(object_attribute) < 7:
        spacer = len_less_than_7
    if len(object_attribute) > 14:
        spacer = len_more_than_14
    # Just so printing looks OK

    print(object_attribute, spacer, type(attribute))

# From the attributes, we can figure out what class an object is
print(integer_value.__class__.__name__)