'''
    If you write a stand along program you will most likely need to provide it with 
    some arguments. 

    You can, of course, parse them on your own out of sys.argv/sys.argc but there is a
    library that comes with Python to make your life easier - argparse. 

    Now, this library is widely documented, but below is a brief example on how you can 
    organize a program to take 2 required parameters and 1 optional one. 
'''
import sys
import argparse

# You prepare the parser the way you want it.....
parser = argparse.ArgumentParser(description='A tutorial of argparse!')
parser.add_argument("-id", required=True, type=str, help="User ID")
parser.add_argument("-org", required=True, type=str, help="User Organization")
parser.add_argument("-region", required=False, default="DEF_VAL", type=str, help="User Locale")

# Parse the command line....but remember, your script name is in location 0 so we take 
# the remainder of the command line to parse out. 
#
# What happens if you run this script without arguments?
programargs = parser.parse_args(sys.argv[1:])

# Now you can access your arguments as attributes. 
print("Hello ", programargs.id)
print("You are from: ", programargs.org, " in ", programargs.region)



