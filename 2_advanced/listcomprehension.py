'''
    List comprehension is very much an advanced topic for a beginner. If you want to learn 
    about it, read on....

    https://data-flair.training/blogs/python-list-comprehension/
    
'''

# Crete a list of number
numberList = []
for i in range(20):
    numberList.append(i)

# Use list comprehension to get only odd numbers
# NOTE : Any number modulo 2 returns a 0 (even) or a 1 (odd), it's a good
#        way to find an odd or even number.
oddNumbers = [x for x in numberList if x % 2 > 0 ]
print(oddNumbers)

# Create a list of users
users = {}
user_names = ['Mary', 'Sue', 'Steve', 'Joe', 'Carolyn']
for i in range(5):
    users[user_names[i]] = i

# Using the keys in a dictionary, look for a key to get the value. 
# Of course, this is just an example, you would really use 
#       'Steve' in users.keys() 
# to see if Steve was actually in the list.
stevesNumber = [users[x] for x in users.keys() if x == 'Steve' ]
print("Steve = ", stevesNumber)
print(users)
