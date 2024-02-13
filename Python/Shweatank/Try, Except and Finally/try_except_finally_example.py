def AbyB(a , b):
    try:
        c = ((a+b) / (a-b))
    except ZeroDivisionError:
        print ("a/b result in 0")
    else:
        print (c)
    finally:
        print("everything is done !")
# Driver program to test above function
AbyB(2.0, 3.0)
AbyB(3.0, 3.0)

def fun(a):
    if a < 4:
    # throws ZeroDivisionError for a = 3
        b = a/(a-3)
    # throws NameError if a >= 4
    print("Value of b = ", b)
try:
    fun(3)
    fun(5)
# note that braces () are necessary here for 
# multiple exceptions
except ZeroDivisionError:
    print("ZeroDivisionError Occurred and Handled !")
except NameError:
    print("NameError Occurred and Handled")
finally:
    print("everything is done !")


# Python program to read character by character from a file

def getcharacters(filename):
    file = open(filename, "r")
    characterlist = []
    for i in file.read():
        characterlist.append(i)
    return characterlist

def getlines(filename):
    file = open(filename, "r")
    characterlist = []
    for i in file.readlines():
        characterlist.append(i)
    return characterlist
            
try: 
    filename = "Try, Except and Finally/characters.txt"
    characterlist = getcharacters(filename)
    linelist = getlines(filename)
    
    print("All Characters:", characterlist)
    print("Total Amount of Characters: ", len(characterlist))
    print("Amount of Spaces: ", characterlist.count(' '))    
    print("Number of Lines: ", len(linelist))
    
except Exception as e:
    print("An Error Occured: ", e) 
    
# Python – Get number of characters, words, spaces and lines in a file
# Python program to Count the Number of occurrences of a key-value pair in a text file

