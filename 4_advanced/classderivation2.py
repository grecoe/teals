'''
    Classes can derive from other classes to extend the functionality. While this works with any types of classes
    these examples extend the list ([]) and string (str) Python objects to return all of the indexes of a particular 
    entry contained within them.

    Why write somethign like this? Because the index() function in python will only give us the FIRST index of a 
    particular item in the sequence. What if you want the 2nd, 3rd or all of them? There is nothign baked into the language
    that supports that. 
'''
class SequenceExtender:
    '''
        Base class for a sequence that we want to get indexes of things. 
    '''
    def indexesOf(self, sequence, item, maxIndexes = -1):
        '''
            Get all of the indexes of 'item' in 'sequence'. You can optionally choose to return 
            only the first maxIndexes indexes. 

            Return value is a list of integer indexes.
        '''
        return_indexes = []
        current_position = 0

        '''
            Because string has no copy() funciton, protect with the try/except.
        '''
        working_sequence = sequence
        try:
            working_sequence = sequence.copy()
        except:
            pass

        while True:
            try:
                # Find the index of the item
                idx = working_sequence.index(item)
            
                # Since we are taking it apart, we hold onto the position so we get the 
                # correct index into the original sequence. 
                current_position = idx if current_position == 0 else (current_position + idx ) 
                return_indexes.append(current_position)

                # If the user only wanted the first N, then stop on N
                if maxIndexes != -1 and len(return_indexes) >= maxIndexes:
                    break

                # Regardless of what we have, we are going to move the position forward in the next 
                # statment and need to account for it in our positioning.
                current_position += 1

                # Move the sequence along past the current instance
                working_sequence = working_sequence[(idx+1):]
            except Exception as ex:
                break
        return return_indexes

    def getUniqueInstances(self, sequence, subsequence):
        '''
            Gets a list of the unique instances in 'sequence' of any item in 'subsequence'. 

            For example, you can get a list of the unique vowels in a string....
        '''
        return list(set([x for x in sequence if x in subsequence]))

class ListExtension(list, SequenceExtender) :
    '''
        A class that extends the Python type list ([]). You can use the instance of this 
        class just like any list, but is extended with the ability to get indexe of particular
        items in the list.
    '''
    def __init__(self, iterable):
        super().__init__(iterable)

    def indexesOf(self, object):
        return super().indexesOf(self, object)

class StringExtension(str, SequenceExtender) :
    '''
        A class that extends the Python type str. The limitation is you must initialize it with the string 
        you want to work with. 

        You can use this object instance as you would any other string object in python. 
    '''
    def indexesOf(self, character):
        '''
            Get all of the indexes of a particular character in a string.
        '''
        return super().indexesOf(self, character)

    def getUniqueVowels(self):
        '''
            Get a list of unique vowels in a string. 

            For example 'My car is wicked fast' would return ['y', 'a','i','e']
        '''
        return super().getUniqueInstances(self, 'aeiouy')

    def getVowelInstances(self):
        '''
            Gets all instances of individual vowels. 

            For example 'My car is wicked fast' would return {'e': [14], 'i': [7, 11], 'y': [1], 'a': [4, 18]}
        '''
        return_data = {}
        vowels = self.getUniqueVowels()

        for vowel in vowels:
            return_data[vowel] = self.indexesOf(vowel)

        return return_data

'''
    Extend list and get the indexes of a particular word. Notice that once the instance is created we can treat it
    just like a list usign the append() function but still have access to the indexesOf() function. 
'''
extended = ListExtension(["hello","hello","goodbye" ])
extended.append("hello")
print(type(extended), extended)
print("What are the indexes of 'hello'?", extended.indexesOf('hello'))

'''
    To show that ListExtension really is a list, we can ask for it's super classes to see what is available.
'''
print('What makes up the ListExtension class?')
for entry in ListExtension.mro():
    print("    ", entry.__name__)
    

'''
    Extend an str object and access the extended class functionality. However, we are still able to use str.count() on 
    the instance as it's base class is a string. 
'''
extended2 = StringExtension("My car is wicked fast.")
print(type(extended2), extended2)
print("\nHow many a's? :", extended2.count('a'))
print("What are the indexes of all a's?", extended2.indexesOf('a'))
print("What are the unique vowels?", extended2.getUniqueVowels())
print("What are the indexes of each vowel?", extended2.getVowelInstances())


'''
    To show that ListExtension really is a list, we can ask for it's super classes to see what is available.
'''
print('What makes up the StringExtension class?')
for entry in StringExtension.mro():
    print("    ", entry.__name__)