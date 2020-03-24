'''
    Binary search

    Items can be found in a list simply by traversing the list and checking
    each item. This is very inefficient if the numbers of items in your list 
    are sufficiently large (>10,000).

    In Computer Science the term binary search applies to something very specific. 
    That is, given an ordered list any item can be found in log2(N) where N is
    the length of the list or collection. 

    So what is a binary search? You can find all sorts online to describe it, but 
    you essentially are breaking down your list on each search by half.

    Lets say we had an alphabet and we wanted to find the index of 'l'. 

    We would check the character at the left index then the right index. If
    we don't find it, check the one at the midpoint. 

    If it's still not the midpoint then determine if what you are looking for 
    is less than the midpoint or greater than the midpoint. 

    Once you have that, change your left and right accordingly.

    Lets say we are looking for k in the alphabet
    ITERATION 1: l is less than mid point

        a b c d ....m...........   z
        ^           ^              ^
       left        mid           right

    ITERATION 2: Still havent found it but it's greater than the mid point 

        b c d.......g...........   l
        ^           ^              ^
       left        mid           right

    ITERATION 2: Still havent found it but it's greater than the mid point 

        h ..........i...........   k
        ^           ^              ^
       left        mid           right

       SOLUTION FOUND: We now have the target at the right index.

    As you can see it took us only 3 searches to find k, which is the 11th
    character in the alphabet. 

    log2(26) = 4.7

    So in this case binary search performed better than expected. Typically
    the answer will bobble around the log2(N) number. 
'''

import random
import math

global_binary_search_count = 0
global_binary_search_location = "Not Found"

def binary_search(ordered_list,left, right, target):
    '''
        Function that actually performs the binary search. 
    '''
    global global_binary_search_count
    global global_binary_search_location

    global_binary_search_count += 1

    if ordered_list[left] == target:
        global_binary_search_location = "ordered_list[left]"
        return left
    elif ordered_list[right] == target:
        global_binary_search_location = "ordered_list[right]"
        return right
    elif right > left :

        mid = (left + right - 1) // 2 # We want an index as integer

        if ordered_list[mid] == target:
            global_binary_search_location = "ordered_list[mid]"
            return mid
        elif ordered_list[mid] > target:
            # Try again with left half
            return binary_search(ordered_list, left + 1, mid-1, target)
        else:
            # Try again with right half
            return binary_search(ordered_list, mid+1, right - 1,  target)
    else:
        return -1
    
def get_sorted_list(max_size = -1):
    '''
        Create a sufficiently large ordered list of entries, they 
        can be anything, but I chose to use characters and arrange
        them in increasing order. 
    '''
    alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p']
    sorted_list = []
    for c1 in alphabet:
        for c2 in alphabet:
            for c3 in alphabet:
                for c4 in alphabet:
                    for c5 in alphabet:
                        sorted_list.append(c1 + c2 + c3 + c4 + c5)
                        if max_size != -1 and len(sorted_list) >= max_size:
                            return sorted_list

    # IN case they don't identify a max size                            
    return sorted_list

def perform_binary_search(ordered_list):
    '''
        Choose choose a random index. 
        Get the item at that random index and perform the binary
        search. You will get the same index returned from that function
        as well.  
    '''
    global global_binary_search_count
    global global_binary_search_location
    global_binary_search_count = 0
    global_binary_search_location = ''

    random_selection_index = random.randint(0, len(ordered_list) - 1)
    random_selection = ordered_list[random_selection_index]

    found_index = binary_search(ordered_list, 0, len(ordered_list) -1, random_selection)
    '''
       
        Now print out what it is we had, how many searches it took, etc.
    '''
    print("Ordered Set Size = ", len(ordered_list))
    print("Searching for:", random_selection)
    print("Random Index =", random_selection_index)
    print("Found Index =", found_index)
    print("Search Location = ", global_binary_search_location)

    '''
        Now compare the searches to the expected Log2(N)
    '''
    print("Search Time =", global_binary_search_count)
    print("Log2(N) = ", math.log(len(ordered_list),2))



'''
    Use random string of characters (sorted)
'''
print("\n***********************")
print("Random Strings - All")
print("***********************\n")
ordered_list = get_sorted_list()
perform_binary_search(ordered_list)

print("\n***********************")
print("Random Strings - 10000")
print("***********************\n")
ordered_list = get_sorted_list(10000)
perform_binary_search(ordered_list)

print("\n***********************")
print("Random Strings - 100")
print("***********************\n")
ordered_list = get_sorted_list(100)
perform_binary_search(ordered_list)
