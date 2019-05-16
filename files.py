#!/usr/bin/env python3
# files.py

# general instructions: 
#   - print a blank line between sections of output
#   - Add your comments using triple quotes. Example:
''' student comment'''

def main():
    # we want to see what is going on in the file system.
    # open file explorer and navigate to your working directory. 
    # you should see just the files in the repo.

    '''
    - creation
    '''
    # files are created with the open function.
    # look at the different modes that can be used with this function
    # https://docs.python.org/3/library/functions.html#open

    # We will use the following file name in this exercise
    fileName = "myFile.txt"

    # try the following code:
    try:
        infile = open(fileName)
    except Exception as error:
        print(type(error), error)
    print()

    # try the following code:
    try:
        infile = open(fileName, 'r')
    except Exception as error:
        print(type(error), error)
    print()

    # What errors did you get? Add a comment here with the output:
    ''' file does not exist errors '''
    # The default mode for open() is 'r', so the statements above are really
    # the same code. Logically a file must exist in order for us to read it.

    # Now write the same code but change the mode to 'a'
    # your code here
    try:
        infile = open(fileName, 'a')
    except Exception as error:
        print(type(error), error)
    print()
    # close the file
    infile.close()
    # run this program then look in the file explorer window. A new text 
    # file should be shown. Using a text editor, edit the text file to add 
    # some text - a few lines of gibberish. Don't forget to close the file
    # in the text editor.

    # Now write the same code but change the mode to 'w'
    # your code here. 
    try:
        infile = open(fileName, 'w')
    except Exception as error:
        print(type(error), error)
    print()
    # close the file
    infile.close()
    # run the program then open the text file in a text editor and view 
    # the contents
    # add a comment here describing the contents:
    ''' it would appear the data got destroyed with the 'w' '''

    '''
    - element access
    - traversal
    '''
    fileName = "sample.txt"
    # View the file in a text editor.

    # There are several ways to read a file

    # Method 1: read()
    # open your book to p. 161 and replicate the code at the center of 
    # the page that opens, reads, and prints the file. Use "infile" again
    # as the file handle
    fname = input("enter a filename: ")
    infile = open(fname,"r")
    data = infile.read()
    print(data)
    # compare the program output with what you see in a text editor.
    # are they the same? Add your answer in a comment here:
    ''' depending on what file I opened they appeared to be the same'''
    # add a print statement that prints the length of data
    print(len(data))
    print(type(data))
    # this demonstrates that data is one big string.
    # you might try counting the characters to see if the length includes
    # line feeds.

    # closing the file - uncomment the line below when you get here
    infile.close()

    # Method 2: readlines()
    # uncomment the code below and run this program
    
    infile = open(fileName)
    data = infile.readlines()
    print(data)
    print()
    infile.close()
    
    # answer the following questions:
    # what type is data?
    '''list'''
    # how is it different from the data in Method 1?
    ''' This prints it allas one big line and entire contents into memory'''
    # Do the strings have escape characters?
    '''it would appear so'''

    # write a for loop that uses data as the sequence and prints out
    # the text lines. What do you have to do in the print statement 
    # to make the ouput look like what you see in a text editor?

    # your code here
    for b in data:
        print(b)
    # closing the file - uncomment the line below when you get here
    infile.close()

    # Method 3: readline()
    # uncomment the following code, then add comments above each line
    # of code to describe what that line does
    #opens the file
    infile = open(fileName)
    # assigns infile.readline() to the varaible line
    line = infile.readline()
    #for loop that does something at the end of the line string
    while line != "":
        print(line[:-1])
        line = infile.readline()
    #closes the file
    infile.close()    
    

    # Method 4: using the file handle as a sequence
    # replicate the last section of code on p. 162 that uses infile as the
    # sequence in the for loop.
    # your code here

    infile = open(filename, "r")
    for i in range(5):
        line = infile.readline()
        print(line[:-1])
    '''
    - element insertion
    - element updates
    '''
    # these are really just writing to a file.
    # open "mydata.txt" for writing using the file handle "outfile"
    fileName = "myFile.txt"
    outfile = open(fileName, "w")
    # Write several lines of gibberish to the file and close it.
    print("I never saw a wild thing")
    print("Sorry for itself.")
    # view the new file in a text editor to verify that the program worked.
    '''i couldnt get it to work'''

main()