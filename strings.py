#!/usr/bin/env python3
# strings.py

# general instructions: 
#   - print a blank line between sections of output
#   - Add your comments using triple quotes. Example:
''' student comment'''

def main():
    '''
    - creation
    '''
    # create two strings named "s1" and "s2"
    # create s1 using a literal string with at least 3 words in it
    # create s2 using the input() function. Enter a string with at 
    #    least 3 words in it
    # your code below here
    s1 = " This is it"
    s2 = input("enter a string with at least 3 words in it: ")
    # print both strings
    print(s1, s2)

    '''
    - element access
    - traversal
    '''
    # this next section demonstrates both access and traversal
    # write a for loop that prints individual characters from s1, each on 
    # a separate line.
    # print every third character starting with the second one.
    # DO NOT hard code the stop value - use len()
    # your code should use indexing
    # the output line should contain the value of the index as well as 
    # the character
    # your code below here
    for i in range(len(s1)):
        print(s1[i])

    
    for i in range (1, len(s1), 3):
        print(s1[i])
        
    
    
    '''
    - element insertion
    '''
    # strings are immutable, but we can mimic changes using string operations
    # and forming a new string. For example insertion can be mimicked by using
    # slicing to split the original string into two parts and concatentation 
    # (+ operation) to form the new string with the inserted string between 
    # the two slices
    #
    # form two new string variables using slicing on s1
    sl1 = s1[:14]
    sl2 = s1[15:]
    # create a third variable with the string you want to insert
    s3 = " my droogies "

    # form a new string named "snew" using concatenation and print snew.
    snew = sl1 + s3 + sl2
    print(snew)
    '''
    - element deletion
    '''
    # the goal is to delete the word you just inserted from snew. But, we 
    # want to do everything programmatically. Follow the steps below to 
    # generate your two slices.
    # use the find() method to find the index of the word to delete.
    # see https://docs.python.org/3/library/stdtypes.html#string-methods
    # find the index of the beginning of the word you want to delte
    a = snew.find("m")
    # use the find() method to find the word after the one you are deleting.
    b = snew.find("e")
    # use the indexes to form two slices
    asnew = snew[0:a]
    bsnew = snew[b:]
    # use concatenation to form snew and print it
    print(asnew + bsnew)

    '''
    - element updates
    '''
    # one form of update is replacing an old word with a new word. This is
    # so common Python has a method for it. Use the replace() method to 
    # replace a word in s1. Assign the new string to snew and print it.
    snew = s1.replace("it", "confusing")
    print(snew)

    '''
    Last item
    '''
    # in this section we will illustrate the split() method. This is a lead-in
    # to the next program file "lists.py"
    # Set variable named "l" to s1.split()
    l = s1.split()
    # print l
    print(l)


main()