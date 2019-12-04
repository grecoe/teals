'''
    Multiple ways (some good some not) of how to reverse a string.
'''

word = "won emit loop"

'''
    Uses indexing...but only reverse indexing to new string object.
'''
def reverseWordRange(userWord):

    revVersion = ""
    length = (len(userWord)+1) * -1

    for i in range(-1, length, -1):
        revVersion += userWord[i]

    return revVersion

'''
    Uses forward and backward indexing into an array (cannot index strings in python).
'''
def reverseWordIndexOnly(userWord):
    start = 0
    end = len(userWord)-1

    revVersion = [None] * len(userWord)
    while start < end:
        tmp = userWord[start]
        revVersion[start] = userWord[end]
        revVersion[end] = tmp
        start += 1
        end -= 1

    # if odd length, we would miss the middle character....
    if start == end:
        revVersion[start] = userWord[end]

    return "".join(revVersion)



'''
    Uses list.reverse()
'''
def reverseWordArray(userWord):

    wordArr = [x for x in userWord]
    wordArr.reverse()
    return "".join(wordArr)


'''
    Uses list.pop() ...
'''
def reverseWordArray2(userWord):

    wordArr = [x for x in userWord]
    revVersion = ""
    while len(wordArr) > 0:
        revVersion += wordArr.pop() 

    return revVersion


revVer = reverseWordIndexOnly(word)
print(word, ' = ', revVer)
revVer = reverseWordRange(word)
print(word, ' = ', revVer)
revVer = reverseWordArray(word)
print(word, ' = ', revVer)
revVer = reverseWordArray2(word)
print(word, ' = ', revVer)

