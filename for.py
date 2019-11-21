'''

    The for loop allows you to continue to execute statements while iterating over some sort of sequence. 

    The syntax :

    for <item> in <sequence> :
        <statements>

'''
import os

for val in range(5):
    print(val)


input("Press enter to continue.....")
os.system('cls')

myList = [1,2,3,4,5]
for listItem in myList:
    print(listItem)

input("Press enter to continue.....")
os.system('cls')
