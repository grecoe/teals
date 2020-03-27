'''
    Many languages have built in search functionality. Python itself
    can sort a iterable item for you with the built in function

    sorted(iterable, key=None, reverse=False)

    The return value is a sorted list of item. 

    However, how is sorting done? Why would you choose one over the other? 

    In Computer Science these are core topics because if you choose
    a poor sorting algorithm it can affect the way your program runs
    and responds. 

    This code will look at two different types of sorting algorighm, 
    although there are dozens.

    Bubble Sort 
    Insertion Sort
'''
import random

def get_sortable_list(list_size):
    '''
        Function to generate a list of numbers of any size
        you want to test your functions.
    '''
    return_list = []
    for iteration in range(list_size):
        return_list.append(random.randint(0,list_size * 2))
    return return_list

'''
    Bubble Sort

    This algorithm has an value of O(n*n) and operates as follows

    Given a list [4 , 2, 3, ....]

    You create nested for loops to iterate the list

           loop2
             |
        [4 , 2, 3, ....]
         |
       loop1

    The outer loop, loop1, goes over each item in the list at a slower
    rate than the inner loop, loop2. 

    Loop2 goes over every number and if it's lower than the value pointed
    to by loop1, the values are swapped. Otherwise, loop2 moves forward.

    When loop2 hits the end of the list, loop1 is then increased.

    This algorigthm performs better when the list is unsorted already.
'''
def bubbleSort(sortable_list):
    steps = 0
    for outer in range(len(sortable_list)):
        steps += 1
        for inner in range(outer + 1, len(sortable_list)):
            steps += 1
            if sortable_list[inner] < sortable_list[outer]:
                steps += 1
                sortable_list[outer], sortable_list[inner] = sortable_list[inner], sortable_list[outer]
                '''
                temp = sortable_list[outer]
                sortable_list[outer] = sortable_list[inner]
                sortable_list[inner] = temp
                '''
    return steps

    
'''
    Insertion sort 

    Given a list [4 , 2, 3, ....]

    You create nested for loops to iterate the list, just like
    with bubble sort. However the loops are reveresed.

           loop1
             |
        [4 , 2, 3, ....]
         |
       loop2

    In this approach, all items before loop2 are compared, starting
    at the begining of the list, to the value pointed to by loop1. 
    If the loop1 is less than loop2, the value from loop1 is inserted
    at loop2. 

    Surprisingly, this algorithm is much more efficient when the items 
    are unsorted, but performs worse when the items ARE sorted.  
'''
def insertionSort(arr): 
    steps = 0
    # Traverse through 1 to len(arr) 
    for i in range(1, len(arr)): 
        steps += 1
        key = arr[i] 
  
        # Move elements of arr[0..i-1], that are 
        # greater than key, to one position ahead 
        # of their current position 
        j = i-1
        while j >= 0 and key < arr[j] : 
            steps += 1
            arr[j + 1] = arr[j] 
            j -= 1
        arr[j + 1] = key 
    
    return steps



sort_list_size = 10

print("\nBubble Sort")
bubble_sort_list = get_sortable_list(sort_list_size)
iterations = bubbleSort(bubble_sort_list)
print("    {} unsorted items in {} steps.".format(len(bubble_sort_list), iterations))
iterations = bubbleSort(bubble_sort_list)
print("    {} sorted items in {} steps.".format(len(bubble_sort_list), iterations))

print("\nInsertion Sort")
insertion_sort_list = get_sortable_list(sort_list_size)
iterations = insertionSort(insertion_sort_list)
print("    {} unsorted items in {} steps.".format(len(insertion_sort_list), iterations))
iterations = insertionSort(insertion_sort_list)
print("    {} sorted items in {} steps.".format(len(insertion_sort_list), iterations))
